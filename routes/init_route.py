from flask import Blueprint

bp = Blueprint("health", __name__)

@bp.route("/", methods=["GET"])
def health():
    return {"message": "risala_api_v1"}
