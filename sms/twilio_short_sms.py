from twilio.rest import Client

account_sid = 'your_account_sid'
auth_token = 'your_auto_token'
client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+8801682148802",
    from_="+12075798097",
    body="Hello from Python!"
)

print(message.sid)

