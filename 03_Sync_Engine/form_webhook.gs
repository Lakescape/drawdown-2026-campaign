/**
 * DRAWDOWN 2026 — Google Form → Railway webhook bridge (T-09)
 *
 * Fires on every submission of the "Lake Drawdown Project Request Form"
 * and POSTs a normalized lead payload to `POST /webhooks/form`, so the
 * submission starts a 5-minute SLA clock, posts a card to
 * `#drawdown-inbound`, and writes a Linear event — same as T-01..T-08.
 *
 * Contract (SALES_CRM_SLA_AutomationSpecs_v1_FINAL.md):
 *   - Idempotency key: `form:{responseId}`  (§1 dedupe rules)
 *   - Signed: HMAC-SHA256 over the raw body, `X-Drawdown-Signature` (§7 auth table)
 *   - Retried 3x, then alerted — "a send without a ledger entry is a failed send"
 *   - Carries ZERO numeric scarcity fields (§6 rule 3)
 *
 * SETUP (once, in the form's bound Apps Script project):
 *   1. Project Settings → Script Properties, add:
 *        WEBHOOK_URL     = https://insightengine-production-b307.up.railway.app/webhooks/form
 *        WEBHOOK_SECRET  = <shared secret, also set on Railway>
 *        ALERT_EMAIL     = nate@atxlakescapes.com
 *   2. Run `installTrigger()` once and approve the auth prompt.
 *   3. Submit a test response; check Executions + the Railway logs.
 */

// Form question title → payload key. Match is case/space/punctuation-insensitive.
// A question renamed in the form UI lands in `unmapped` instead of silently vanishing.
var FIELD_MAP = {
  "client name": "name",
  "property address": "address",
  "primary phone number": "phone",
  "email address": "email",
  "primary type of work needed": "work_type",
  "please provide a brief description of the requested project": "description",
  "have you obtained any necessary permits for this work": "permit_status",
  "how urgent is this project": "urgency",
  "upload photos of the affected area required for assessment": "photos",
  "are there any specific access constraints to your shoreline": "access_constraints",
  // Fields not on the form yet — mapped ahead of time so adding them needs no code change.
  "how did you hear about us": "source",
  "who referred you": "referrer",
  "cove or street name": "cove",
  "are you the property decision maker": "decision_maker",
  "best time to reach you": "best_time",
  "may we text you at this number": "sms_consent",
  "what are you seeing on your shoreline": "shoreline_signals",
};

function onFormSubmit(e) {
  var props = PropertiesService.getScriptProperties();
  var url = props.getProperty("WEBHOOK_URL");
  var secret = props.getProperty("WEBHOOK_SECRET");
  if (!url || !secret) throw new Error("WEBHOOK_URL / WEBHOOK_SECRET not set in Script Properties");

  var payload = buildPayload(e);
  var body = JSON.stringify(payload);

  var res = postWithRetry(url, body, sign(body, secret));
  if (!res.ok) {
    alertFailure(payload, res.detail);
    throw new Error("webhook failed after retries: " + res.detail); // surfaces in Executions
  }
}

function buildPayload(e) {
  var response = e.response;
  var out = { unmapped: {} };

  response.getItemResponses().forEach(function (ir) {
    var item = ir.getItem();
    var key = FIELD_MAP[normalize(item.getTitle())];
    var value = readAnswer(ir, item);
    if (key) out[key] = value;
    else out.unmapped[item.getTitle()] = value;
  });

  return {
    // §1 idempotency: {channel}:{external_message_id}
    idempotency_key: "form:" + response.getId(),
    channel: "form",
    external_id: response.getId(),
    submitted_at: response.getTimestamp().toISOString(),
    respondent_email: response.getRespondentEmail() || null, // set only while the form collects emails
    form_title: FormApp.getActiveForm().getTitle(),
    lead: out,
  };
}

function readAnswer(itemResponse, item) {
  if (item.getType() === FormApp.ItemType.FILE_UPLOAD) {
    // Response is an array of Drive file IDs. Send IDs + links; the backend fetches
    // them with a service account. Sharing is deliberately NOT mutated here.
    return [].concat(itemResponse.getResponse()).map(function (id) {
      var f = DriveApp.getFileById(id);
      return { file_id: id, name: f.getName(), url: f.getUrl(), bytes: f.getSize() };
    });
  }
  return itemResponse.getResponse(); // string, or array for checkbox items
}

function postWithRetry(url, body, signature) {
  var detail = "";
  for (var attempt = 1; attempt <= 3; attempt++) {
    try {
      var res = UrlFetchApp.fetch(url, {
        method: "post",
        contentType: "application/json",
        payload: body,
        headers: { "X-Drawdown-Signature": signature },
        muteHttpExceptions: true,
        followRedirects: false,
      });
      var code = res.getResponseCode();
      if (code >= 200 && code < 300) return { ok: true };
      detail = "HTTP " + code + " — " + res.getContentText().slice(0, 500);
      if (code >= 400 && code < 500 && code !== 429) return { ok: false, detail: detail }; // won't fix itself
    } catch (err) {
      detail = String(err);
    }
    if (attempt < 3) Utilities.sleep(1000 * Math.pow(2, attempt)); // 2s, 4s
  }
  return { ok: false, detail: detail };
}

function sign(body, secret) {
  return Utilities.computeHmacSha256Signature(body, secret)
    .map(function (b) {
      return ("0" + (b & 0xff).toString(16)).slice(-2);
    })
    .join("");
}

function alertFailure(payload, detail) {
  var to = PropertiesService.getScriptProperties().getProperty("ALERT_EMAIL");
  if (!to) return;
  MailApp.sendEmail({
    to: to,
    subject: "🚨 DRAWDOWN form webhook FAILED — lead not in the pipeline",
    body:
      "A form submission did not reach Railway. No SLA clock started. Work it by hand.\n\n" +
      "Error: " + detail + "\n\n" + JSON.stringify(payload, null, 2),
  });
}

function normalize(s) {
  return String(s).toLowerCase().replace(/[^a-z0-9 ]/g, "").replace(/\s+/g, " ").trim();
}

/** Run once. Installable trigger — the simple trigger can't call UrlFetchApp. */
function installTrigger() {
  var form = FormApp.getActiveForm();
  ScriptApp.getProjectTriggers().forEach(function (t) {
    if (t.getHandlerFunction() === "onFormSubmit") ScriptApp.deleteTrigger(t);
  });
  ScriptApp.newTrigger("onFormSubmit").forForm(form).onFormSubmit().create();
}
