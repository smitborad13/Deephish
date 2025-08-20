from flask import Flask, request, jsonify
import pickle
import tldextract
import re

# Initialize the Flask app
app = Flask(__name__)

# Load the trained model
model = pickle.load(open("../model/phishing_model.pkl", "rb"))

# Function to extract features from a URL
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

# API route to receive and scan URLs
@app.route("/predict", methods=["POST"])
def predict():
    data = request.json  # Get data from user
    url = data.get("url")

    if not url:
        return jsonify({"error": "URL is required"}), 400

    # Extract features
    features = extract_features(url)
    X = [[features[k] for k in sorted(features.keys())]]

    # Predict
    prediction = model.predict(X)[0]
    probability = model.predict_proba(X)[0][1]

    return jsonify({
        "url": url,
        "prediction": "phishing" if prediction else "benign",
        "confidence": round(probability, 2)
    })

# Run the server
if __name__ == "__main__":
    app.run(debug=True)
