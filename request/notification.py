# Create a new OneSignal app

import requests

url = "https://onesignal.com/api/v1/apps"

payload = {
    "name": "NAME_OF_NEW_APP",
    "apns_env": "ENVIRONMENT",
    "apns_p12": "CONVERTED_P12",
    "apns_p12_password": "P12_PASSWORD",
    "gcm_key": "FCM_KEY",
    "android_gcm_sender_id": "FCM_ID",
    "chrome_web_origin": "URL",
    "chrome_web_default_notification_icon": "DEFAULT_ICON",
    "chrome_web_sub_domain": "SUBDOMAIN",
    "chrome_key": "AUTH_KEY",
    "site_name": "SITE_NAME",
    "safari_site_origin": "URL",
    "safari_apns_p12": "CONVERTED_P12",
    "safari_apns_p12_password": "P12_PASSWORD",
    "safari_icon_256_256": "ICON_URL",
    "additional_data_is_root_payload": False,
    "organization_id": "ORG_ID"
}
headers = {
    "accept": "text/plain",
    "Content-Type": "application/json",
    "Authorization": "Basic YOUR_USER_AUTH_KEY"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)

