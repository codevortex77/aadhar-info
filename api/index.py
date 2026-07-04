import requests
from flask import Flask, request, jsonify
import json
from datetime import datetime

app = Flask(__name__)

# --- Configuration ---
ALLOWED_KEY = "July"
# 30 days validity from today (Expires Aug 3, 2026)
EXPIRY_DATE = datetime(2026, 8, 3)

@app.route('/', methods=['GET'])
def clone_api():
    client_key = request.args.get('key')
    query_param = request.args.get('query', '')

    # Check Key Authentication
    if client_key != ALLOWED_KEY:
        return jsonify({"error": "Unauthorized: Invalid API Key"}), 401

    # Check 30-Day Validity
    if datetime.now() > EXPIRY_DATE:
        return jsonify({"error": "Unauthorized: API Key Expired"}), 403

    # Construct the upstream URL
    # Replace api.example.com with the actual endpoint you are authorized to proxy
    upstream_url = f"https://rootx-osint.in/?type=hiteck_aadhar&key=swayam&query={query_param}"

    try:
        response = requests.get(upstream_url)
        data = response.json()
    except Exception as e:
        return jsonify({"error": "Failed to fetch or parse data from upstream API"}), 500

    # Convert to string for easy global replacement of the developer's handle
    data_str = json.dumps(data)
    data_str = data_str.replace("@simpleguy444", "@RichUniversal")
    
    # Convert back to dictionary
    data = json.loads(data_str)

    # Remove the unwanted keys
    keys_to_remove = ["req_left", "req_total", "expiry", "developer"]
    for k in keys_to_remove:
        data.pop(k, None)

    # Add the new custom credit
    data["Credit"] = "@RichUniversal"

    return jsonify(data)

