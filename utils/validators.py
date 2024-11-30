def validate_phone_number(phone):
    if not phone.startswith("+") or len(phone) < 10:
        return False
    return True
