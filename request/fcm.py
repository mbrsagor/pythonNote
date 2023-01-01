import requests

url = "https://fcm.googleapis.com/fcm/send"
authorization = "Your key"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"key={authorization}"
}


device_token = "e3b6mA0wTw-xzXUtG5yMg1:APA91bGJ6lunearRRBL573-PGDl1pDeMkzzuE6-A7czjVxRnpYKPZx9hdXvInqf3UKIoorqDC3n0mZV57oEzcpcgI4Zu0Fsq0pHnfKwUY5wgVtvhcG6xArN9RftM5vE-x-ezpE7XuA8w"

def send_notification(send_to, title, message):
    # to = send_to
    to = '/topics/all'
    data = {
        'title': title,
        'message': message
    }
    body = {
        'to': to,
        'data': data
    }
    response = requests.post(url, json=body, headers=headers)
    return response


notification = send_notification(device_token, "Welcome", "Welcome to our website.")
print(notification)
