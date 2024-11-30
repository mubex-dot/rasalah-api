from flask import request
from ..services.mock_payments import simulate_payment
from ..utils.helpers import generate_response

def process_payment():
    """
    Process a payment.
    """
    phone_number = request.json.get("phone_number")
    amount = request.json.get("amount")
    if not phone_number or not amount:
        return generate_response(False, "Missing 'phone_number' or 'amount'.")
    # Simulate payment
    payment_response = simulate_payment(phone_number, amount)
    return generate_response(payment_response["success"], payment_response["message"], payment_response)
