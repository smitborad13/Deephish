import pandas as pd
import tldextract
import re
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle

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

# Load CSV data
df = pd.read_csv("../data/urls.csv")  # path from model/ folder
df["label"] = df["label"].map({"phishing": 1, "benign": 0})

# Extract features
X = pd.DataFrame([extract_features(url) for url in df["url"]])
y = df["label"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

# Save model
with open("phishing_model.pkl", "wb") as f:
    pickle.dump(model, f)
