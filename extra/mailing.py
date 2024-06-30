import smtplib, ssl
from datetime import datetime

# Create a secure SSL context
context = ssl.create_default_context()


def sendmail(smtp_server, sender_email, password, port=587):
    # Try to log in to server and send email
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()  # Can be omitted
        server.starttls(context=context)  # Secure the connection
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        # TODO: Send email here
    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        server.quit()


# Finally send mail to the user
sendmail(smtp_server="smtp.gmail.com", sender_email="my@gmail.com", password="<PASSWORD>", port=587)


now = datetime.now()  # current date and time
date_time = now.strftime("%Y-%m-%d %I:%M %p")
print(date_time)
