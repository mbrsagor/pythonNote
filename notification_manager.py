import requests

url = "https://onesignal.com/api/v1/players"

payload = {
    "device_type": 0,
    "language": "en",
    "timezone": "-28800",
    "game_version": "1.1.1",
    "device_model": "iPhone5,1",
    "device_os": "15.1.1",
    "session_count": 600,
    "tags": {
        "first_name": "Jon",
        "last_name": "Smith",
        "level": "99",
        "amount_spent": "6000",
        "account_type": "VIP"
    },
    "amount_spent": "100.99",
    "playtime": 600,
    "notification_types": 1,
    "lat": 37.563,
    "long": 122.3255,
    "country": "US",
    "timezone_id": "Europe\/Warsaw"
}
headers = {
    "accept": "application/json",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)
print(response.text)
