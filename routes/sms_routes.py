from flask import Blueprint
from ..controllers.sms_controller import send_sms

sms_bp = Blueprint("sms", __name__)

sms_bp.route("/send", methods=["POST"])(send_sms)
