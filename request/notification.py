# Create a new OneSignal app

import requests

url = "https://onesignal.com/api/v1/notifications/"

API_KEY = "NGYyMDFiYzYtZDJjNi00OWNiLWI4ODEtNDk1YWE0ZGM2MjZl"
APP_ID = "3428af54-41f6-454f-ad10-112ab455eeb1"
authorization = "NDIwNTQxOGMtZDdlNC00ZmQ0LTk5YzItZGM5ZGExNDU2Y2Ex"

payload = {
    "device_type": 0,
    "language": "en",
}

body = {
    "app_id": APP_ID,
    "app_name": "Hercules",
    "included_segments": ["Subscribed Users"],
    # "include_player_ids": ["8b2df38d-62cc-48a9-bad0-407bdc80b820"],
    "android_sound": "notification",
    "large_icon": "https://res.cloudinary.com/mbrsagor/image/upload/v1640713048/booking_bg_wzssss.jpg",
    "big_picture": "https://res.cloudinary.com/mbrsagor/image/upload/v1640713048/booking_bg_wzssss.jpg",
    "headings": {"en": "Hello, delivery Mama"},
    "contents": {"en": 'Welcome Hercules App!'},
}

headers = {
    "accept": "text/plain",
    "Content-Type": "application/json",
    "Authorization": f"Basic {authorization}"
}

response = requests.post(url, json=body, headers=headers)
print(response.text)
