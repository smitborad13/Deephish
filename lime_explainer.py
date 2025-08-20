import pickle
import pandas as pd
import tldextract
import re
import webbrowser
import os
from lime.lime_tabular import LimeTabularExplainer

# Load model
model = pickle.load(open("../model/phishing_model.pkl", "rb"))

# Feature extraction (same as training)
def extract_features(url):
    ext = tldextract.extract(url)
    return {
        "url_length": len(url),
        "has_ip": bool(re.search(r"\d+\.\d+\.\d+\.\d+", url)),
        "domain_entropy": sum([ord(c) for c in ext.domain]) / len(ext.domain) if ext.domain else 0,
        "contains_login": "login" in url.lower(),
        "contains_secure": "secure" in url.lower(),
        "brand_spoof": any(brand in url.lower() for brand in ["paypal", "apple", "bank", "amazon"])
    }

# Input URL to explain
input_url = "http://paypal-login-verify.com"
features = extract_features(input_url)
X = pd.DataFrame([features])

# LIME explainer setup
explainer = LimeTabularExplainer(
    training_data=X.values,
    feature_names=X.columns.tolist(),
    class_names=["benign", "phishing"],
    mode="classification"
)

# Generate explanation
explanation = explainer.explain_instance(
    data_row=X.iloc[0].values,
    predict_fn=model.predict_proba,
    num_features=6
)

# ✅ Ensure output directory exists
output_dir = os.path.join(os.path.dirname(__file__), "lime_outputs")
os.makedirs(output_dir, exist_ok=True)

# ✅ Save the explanation as HTML
output_path = os.path.join(output_dir, "lime_explanation.html")
with open(output_path, "w", encoding="utf-8") as f:
    f.write(explanation.as_html())

# ✅ Open it in the default browser
webbrowser.open(f"file://{output_path}")
