from flask import request, Response
from .sms_controller import send_sms

def handle_ussd():
    session_id = request.form.get("sessionId")
    service_code = request.form.get("serviceCode")
    phone_number = request.form.get("phoneNumber")
    text = request.form.get("text", "")

    if text == "":
        response = "CON Welcome to Rasalah Logistics.\n"
        response += "1. Start Delivery\n"
        response += "2. Update Status\n"
        response += "3. Report Issue"

    elif text == "1":
        response = "CON Enter Order ID to start delivery:"

    elif text.startswith("1*"):
        package_id = text.split("*")[1]
        response = f"END Delivery for Order ID {package_id} started successfully.\n"
        response += "Recipient will receive an SMS shortly."
        send_sms(
            to=[phone_number],
            message=f"Hello, your delivery for Order ID: {package_id} has started successfully and will arrive in 10 minutes. If there's any problem or you want to contact the courier, here's the number: {phone_number}"
        )

    elif text == "2":
        response = "CON Enter Order ID to update status:"

    elif text.startswith("2*"):
        parts = text.split("*")
        if len(parts) == 2: 
            package_id = parts[1]
            response = "CON Update status for Order ID " + package_id + ":\n"
            response += "1. Delivered\n"
            response += "2. Attempted Delivery\n"
            response += "3. Issue Reported"

        elif len(parts) == 3: 
            package_id = parts[1]
            status_option = parts[2]
            if status_option == "1":
                response = "END Status updated: Delivered.\n"
                response += "Recipient will receive an SMS shortly."
                send_sms(
                    to=[phone_number],
                    message=f"Your delivery for Order ID {package_id} has been delivered."
                )
            elif status_option == "2":
                response = "END Status updated: Attempted Delivery.\n"
                response += "Recipient will receive an SMS shortly."
                send_sms(
                    to=[phone_number],
                    message=f"An attempt was made to deliver your order with ID: {package_id}, but it was unsuccessful. Please contact the courier via {phone_number} for more details."
                )
            elif status_option == "3":
                response = "END Status updated: Issue Reported.\n"
                response += "Recipient will receive an SMS shortly."
                send_sms(
                    to=[phone_number],
                    message=f"There was an issue reported with your delivery for Order ID {package_id}."
                )
            else:
                response = "END Invalid option. Please try again."
        else:
            response = "END Invalid input format. Please try again."

    elif text == "3":
        response = "CON Enter Order ID and issue details (separated by asterisk '*'):\nExample: OrderID*Issue"

    elif text.startswith("3*"):
        parts = text.split("*")
        if len(parts) >= 3:
            package_id = parts[1]
            issue_details = " ".join(parts[2:]) 
            response = f"END Issue reported for Order ID {package_id}.\n"
            response += "We will investigate and get back to you shortly."
            send_sms(
                to=[phone_number],
                message=f"Hello, an issue has been reported for Order ID {package_id}. Details: {issue_details}. Please contact courier {phone_number} for more info."
            )
        else:
            response = "END Invalid input format. Please try again."

    else:
        response = "END Invalid input. Please try again."

    return Response(response, mimetype="text/plain")
