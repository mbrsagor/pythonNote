import stripe
from django.shortcuts import render
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY  # Set your secret key in settings.py

def success_view(request):
    session_id = request.GET.get('session_id')
    
    if session_id:
        # Retrieve the Checkout Session using the session ID
        session = stripe.checkout.Session.retrieve(session_id)

        # Get the payment intent ID from the session
        payment_intent_id = session.payment_intent  # This is the transaction ID

        # Optionally, you can retrieve more details about the payment intent
        payment_intent = stripe.PaymentIntent.retrieve(payment_intent_id)

        # Now you can access payment information, e.g. amount, currency, etc.
        amount_received = payment_intent.amount_received
        currency = payment_intent.currency

        context = {
            'payment_intent_id': payment_intent_id,
            'amount_received': amount_received,
            'currency': currency,
            # Add other relevant information you want to show
        }
    else:
        context = {
            'error': 'Session ID not found.'
        }

    return render(request, 'success.html', context=context)
