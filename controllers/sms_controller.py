from flask import request
import africastalking
from ..utils.helpers import generate_response
import os

# Initialize Africa's Talking API
africastalking.initialize(
    username=os.getenv("AT_USERNAME", "sandbox"), 
    api_key=os.getenv("AT_API_KEY", "your_api_key")
)
sms = africastalking.SMS

def send_sms(to, message):
    if not to or not message:
        return generate_response(False, "Missing 'to' or 'message' parameter.")

    try:
        # Send SMS via Africa's Talking
        response = sms.send(message=message, recipients=to)
        return generate_response(True, "SMS sent successfully", response)
    except Exception as e:
        return generate_response(False, "Failed to send SMS", {"error": str(e)})
