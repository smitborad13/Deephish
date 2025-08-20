import requests
import time

# VirusTotal API key — replace this with your real one if you register (optional)
VT_API_KEY = "your_virustotal_api_key"

# Sample phishing URL to submit (you can loop through your blocked list here)
url_to_submit = "http://paypal-login-verify.com"

def submit_to_virustotal(url):
    print("📡 Submitting to VirusTotal...")
    vt_url = "https://www.virustotal.com/api/v3/urls"

    try:
        response = requests.post(
            vt_url,
            headers={"x-apikey": VT_API_KEY},
            data={"url": url}
        )
        if response.status_code == 200:
            analysis_url = response.json()["data"]["id"]
            print("✅ Submitted to VT: ", analysis_url)
            return analysis_url
        else:
            print("❌ VT submission failed:", response.status_code, response.text)
    except Exception as e:
        print("❌ VT error:", e)

def submit_to_abuse_ch(url):
    print("📡 Submitting to abuse.ch...")
    abuse_url = "https://urlhaus-api.abuse.ch/v1/"

    try:
        data = {
            "url": url,
            "anonymous": "1"  # set to "0" if you want to show your submitter identity
        }

        response = requests.post(
            abuse_url,
            data=data
        )
        if response.status_code == 200:
            print("✅ Submitted to abuse.ch")
        else:
            print("❌ Abuse.ch submission failed:", response.status_code, response.text)
    except Exception as e:
        print("❌ abuse.ch error:", e)

# 🚀 Call the submitters
submit_to_virustotal(url_to_submit)
time.sleep(1)  # avoid rate limits
submit_to_abuse_ch(url_to_submit)
