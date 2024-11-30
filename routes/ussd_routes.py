from flask import Blueprint
from ..controllers.ussd_controller import handle_ussd

ussd_bp = Blueprint("ussd", __name__)

ussd_bp.route("/ussd", methods=["POST"])(handle_ussd)
