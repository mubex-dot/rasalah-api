import random

def simulate_payment(phone_number, amount):
    """
    Simulates a payment for testing purposes.
    """
    transaction_id = f"TXN{random.randint(100000, 999999)}"
    return {
        "success": True,
        "message": "Payment processed successfully.",
        "transaction_id": transaction_id,
        "amount": amount
    }
