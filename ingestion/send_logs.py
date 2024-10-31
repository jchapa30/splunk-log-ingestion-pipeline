import requests
import json

SPLUNK_HEC_URL = 'http://127.0.0.1:8088/services/collector'
SPLUNK_HEC_TOKEN = '8ac5b187-c96d-465c-b34c-d78238c145e5'

headers = {
    'Authorization': f'Splunk {SPLUNK_HEC_TOKEN}',
    'Content-Type': 'application/json'
}

def send_log(data):
    response = requests.post(SPLUNK_HEC_URL, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        print("Log sent successfully.")
    else:
        print("Failed to send log:", response.text)

# Sample log data
log_data = {
    "event": {
        "message": "User login attempt",
        "username": "jdoe",
        "status": "success",
        "ip": "192.168.1.1"
    },
    "sourcetype": "_json"
}

send_log(log_data)
