from google.oauth2 import service_account
import google.auth.transport.requests
import requests

fsm_scope = 'https://www.googleapis.com/auth/firebase.messaging'
fcm_url = 'https://fcm.googleapis.com/v1/projects/rackinup-1054f/messages:send'

def _get_access_token():
    credentials = service_account.Credentials.from_service_account_file(
        'utils/service-account.json',
        scopes=[fsm_scope]
    )
    request = google.auth.transport.requests.Request()
    credentials.refresh(request)
    return credentials.token



#  This function allows sending a notification with additional data payload.
#  The payload can include any additional information that needs to be sent with the notification.
#  The `title` and `message` keys are used for the notification block, while
def send_notification_fcm(payload, device_token):
    access_token = _get_access_token()
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json; UTF-8',
    }

    # Extract title and message for the notification block
    title = payload.get("title", "")
    message = payload.get("message", "")

    # All other keys are sent in the `data` block
    data_payload = {k: str(v) for k, v in payload.items() if k not in ['title', 'message']}

    body = {
        "message": {
            "token": "/topics/all" if device_token == "all" else device_token,
            "notification": {
                "title": title,
                "body": message
            },
            "data": data_payload,
            "android": {
                "priority": "high",
                "notification": {
                    "sound": "default"
                }
            },
            "apns": {
                "payload": {
                    "aps": {
                        "alert": {
                            "title": title,
                            "body": message
                        },
                        "sound": "default"
                    }
                }
            }
        }
    }

    response = requests.post(fcm_url, json=body, headers=headers)
    print(response.status_code, response.text)
    return response


payload = {
    "title": "Congratulations! You’ve Earned 100 Points!",
    "message": "A new user signed up with your referral code. You've earned 100 points as a reward. Keep sharing to earn more!",
    "is_read": False,
    "link": "",
    "route": "",
    "banner": None,
    "data": "",
    "user": 23,
    "device_type": 1,
    "notification_type": 1
}

send_notification_fcm(payload, device_token="all")

