// Force-block known phishing test domains (for demo)
const hardBlockList = [
  "neverssl.com",
  "paypal-login-fake.com"
];

chrome.webRequest.onBeforeRequest.addListener(
  function(details) {
    const url = details.url;

    // Skip internal and localhost
    if (
      url.startsWith("chrome-extension://") ||
      url.includes("127.0.0.1:5000") ||
      url.includes("localhost")
    ) {
      return { cancel: false };
    }

    // Force-block from hardcoded list
    if (hardBlockList.some(domain => url.includes(domain))) {
      console.warn("🚫 HARD BLOCKED (instant):", url);
      return { cancel: true };
    }

    // Just log + allow for async ML
    fetch("http://127.0.0.1:5000/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ url: url })
    }).then(response => response.json())
      .then(data => {
        if (data.prediction === "phishing") {
          console.warn("⚠️ PHISHING DETECTED (logged only):", url);
        }
      }).catch(err => console.error("API error:", err));

    return { cancel: false }; // let request continue
  },
  { urls: ["<all_urls>"] },
  ["blocking"]
);
