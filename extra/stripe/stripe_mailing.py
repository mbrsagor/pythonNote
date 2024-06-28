import stripe
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

stripe.api_key = 'sk_api_key'


# Function to retrieve payment details and send an invoice
def send_receipt_email_to_customer(payment_intent_id, customer_email):
    # Retrieve the payment intent
    payment_intent = stripe.PaymentIntent.retrieve(payment_intent_id)

    # Create the invoice details
    invoice_details = f"""
    Hello,

    Thank you for your payment. Here are your payment details:

    Amount: {payment_intent['amount_received'] / 100} {payment_intent['currency'].upper()}
    Description: {payment_intent['description']}
    Payment Method: {payment_intent['payment_method_types'][0].upper()}

    Best regards,
    Your Company Name
    """

    # Email configuration
    sender_email = 'your@gmail.com'
    sender_password = 'password'
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = customer_email
    msg['Subject'] = 'Your Payment Invoice'
    msg.attach(MIMEText(invoice_details, 'plain'))

    # Send the email
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)
        server.quit()
        print('Invoice sent successfully!')
    except Exception as e:
        print(f'Failed to send invoice: {e}')
