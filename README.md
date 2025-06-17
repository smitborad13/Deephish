# 🛡️ DeepPhish Armor

A complete, beginner-friendly phishing detection system using Machine Learning + Flask + Chrome Extension + LIME explainability + threat feed integration.

---

## 🚀 Features

- ✅ Detects phishing URLs using a Random Forest classifier
- 🌐 Real-time Flask API for prediction
- 🧩 Chrome extension that blocks malicious websites on load
- 🧠 LIME explainability for decision transparency
- 📡 Auto-submits phishing URLs to VirusTotal and abuse.ch

---

## 📁 Project Structure

model/ → ML model + training code
flask_api/ → Real-time prediction API
chrome_extension/ → Browser extension to block phishing
data/ → CSV training dataset
explainability/ → LIME explainable AI visualizer
threat_feed/ → Threat feed auto-submitter

yaml
Copy
Edit

---

## ⚙️ Installation

1. Clone the repo:
```bash
git clone https://github.com/yourusername/DeepPhish_Armor.git
cd DeepPhish_Armor
Create a virtual environment and install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the ML model trainer:

bash
Copy
Edit
python model/train_model.py
Start the API:

bash
Copy
Edit
python flask_api/app.py
🧪 Chrome Extension Setup
Open Chrome → go to chrome://extensions

Enable Developer mode

Click Load unpacked

Select the chrome_extension/ folder

🔍 Explainable AI
To see why a URL was flagged:

bash
Copy
Edit
python explainability/lime_explainer.py
📡 Threat Feed Submission
Submit flagged URLs to VirusTotal and abuse.ch:

bash
Copy
Edit
python threat_feed/threat_submitter.py
🙌 Author
Smit Borad — cybersecurity + ML enthusiast.
