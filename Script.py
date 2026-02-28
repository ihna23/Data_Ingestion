import requests


WEBHOOK_URL = "URL_FROM_MAKE.COM"

incident_data = {
    "station_id": "FRA-099",
    "raw_error": "Voltage drop to 180V. System overheating. Cooling fan at 0 RPM.",
    "status": "Fault"
}

def send_test_fault():
    print(f"Sending fault data to Make.com...")
    response = requests.post(WEBHOOK_URL, json=incident_data)
    if response.status_code == 200:
        print("Make.com received the data.")
    else:
        print(f"Error: {response.status_code}")

if __name__ == "__main__":
    send_test_fault()