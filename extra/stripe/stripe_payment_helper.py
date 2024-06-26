import requests
import stripe

# Stripe API key
stripe_api_key = "YOUR_STRIPE_SECRET_KEY"

# URLS
customer_url = 'https://api.stripe.com/v1/customers'
ephemeral_key_url = 'https://api.stripe.com/v1/ephemeral_keys'
payment_intents_url = 'https://api.stripe.com/v1/payment_intents'
payment_info_url = 'https://api.stripe.com/v1/payment_intents'

# This header will use for global.
headers = {
    'Authorization': f'Bearer {stripe_api_key}',
    'Content-Type': 'application/x-www-form-urlencoded'
}
headers_with_stripe_version = {
    'Authorization': f'Bearer {stripe_api_key}',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Stripe-Version': '2022-08-01'
}


def send_customer_data(name, email, phone):
    """
    Name: Send payment data to customer.
    Description: Requested customer user information send to stripe customer API.
    :param name:
    :param email:
    :param phone:
    :return:
    method: POST request
    """

    data = {
        'name': name,
        'email': email,
        'phone': phone,
    }
    response = requests.post(customer_url, headers=headers, data=data)
    return response.text


def set_customer_ephemeral_key(customer):
    """
    Name: Set customer ephemeral keys.
    :param customer:
    :return:
    Method: POST request
    """
    data = {
        'customer': customer
    }
    response = requests.post(ephemeral_key_url, headers=headers_with_stripe_version, data=data)
    return response.text


def payment_intent(customer, amount, currency):
    """
    Name: Payment intent
    :param customer:
    :param amount:
    :param currency:
    :return:
    """

    data = {
        'customer': customer,
        'amount': amount,
        'currency': currency
    }
    response = requests.post(payment_intents_url, headers=headers, data=data)
    return response.text


def get_payment_information(payment_intent_id):
    """
    Name: Get payment information.
    :return: payment_intent_id
    """
    url = f"{payment_info_url}/{payment_intent_id}"
    response = requests.get(url, headers=headers)
    return response.text


customer = stripe.Customer.create(
    idempotency_key='KG5LxwFBepaKHyUSD',
    name='Bozlur Rosid Sagor', email='mbrsagor@gmail.com',
    phone='123456789', address='Dhaka'
)
print(customer)


