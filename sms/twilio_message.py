# Twilio credentials
account_sid = "your_account_sid_id"
auth_token = "your_auth_token"

# Twilio API endpoint for sending messages
url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Messages.json"


# Parameters for the message
data = {
    "From": "+12394499993",  # Twilio phone number (sender)
    "To": "+88017777777",  # Recipient phone number
    "Body": "Hello, this is a test message from Twilio!",
}

# Sending a POST request with Basic Authentication
response = requests.post(url.format(AccountSID=account_sid),auth=HTTPBasicAuth(account_sid, auth_token), data=data)

# Check if the request was successful
if response.status_code == 201:  # Status code 201 indicates success for resource creation (sending message)
    print("Message sent successfully!")
else:
    print(f"Failed to send message. Status code: {response.status_code}")
    print(response.json())  # Prints error details
