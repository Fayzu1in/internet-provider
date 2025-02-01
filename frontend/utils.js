export function getUTMParameters() {
  const params = new URLSearchParams(window.location.search);
  const utmParams = {
    utm_source: params.get("utm_source"),
    utm_medium: params.get("utm_medium"),
    utm_campaign: params.get("utm_campaign"),
    utm_term: params.get("utm_term"),
    utm_content: params.get("utm_content"),
  };
  return Object.fromEntries(Object.entries(utmParams).filter(([_, v]) => v));
}
