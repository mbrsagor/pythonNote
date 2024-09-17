import http.client
import json

conn = http.client.HTTPSConnection("api.infobip.com")
payload = json.dumps(
    {
        "name": "2fa test application",
        "enabled": True,
        "configuration": {
            "pinAttempts": 10,
            "allowMultiplePinVerifications": True,
            "pinTimeToLive": "15m",
            "verifyPinLimit": "1/3s",
            "sendPinPerApplicationLimit": "100/1d",
            "sendPinPerPhoneNumberLimit": "10/1d",
        },
    }
)
headers = {
    "Authorization": "App 1ee422ebcbc7469e687e3bdddad677a8-14d5e435-a013-44db-a0fe-34d9fc31f92d",
    "Content-Type": "application/json",
    "Accept": "application/json",
}
conn.request("POST", "/2fa/2/applications", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
