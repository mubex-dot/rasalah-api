from flask import jsonify

def generate_response(success, message, data=None):
    """
    Helper function to generate a consistent JSON response.
    """
    return jsonify({
        "success": success,
        "message": message,
        "data": data
    })
