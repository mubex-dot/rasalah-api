from flask import Blueprint
from ..controllers.payment_controller import process_payment

payment_bp = Blueprint("payments", __name__)

payment_bp.route("/process", methods=["POST"])(process_payment)
