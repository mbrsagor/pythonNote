# Create a new OneSignal app

import requests

url = "https://onesignal.com/api/v1/notifications/"

APP_ID = "APP_ID"
authorization = "AUTHORIZATION_TOKEN"

body = {
    "app_id": APP_ID,
    "app_name": "HerculesDev",
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
