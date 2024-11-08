import firebase_admin
from firebase_admin import credentials, messaging

# Initialize the Firebase Admin SDK with the service account key
cred = credentials.Certificate("path/to/serviceAccountKey.json")
firebase_admin.initialize_app(cred)


# Function to send a notification
def send_fcm_message(registration_token, title, body):
    # Create the message payload
    message = messaging.Message(
        notification=messaging.Notification(
            title=title,
            body=body,
        ),
        token=registration_token,
    )

    # Send the message
    response = messaging.send(message)
    print("Successfully sent message:", response)


# Usage example
registration_token = "YOUR_DEVICE_REGISTRATION_TOKEN"
title = "Hello"
body = "This is a test notification"
send_fcm_message(registration_token, title, body)

