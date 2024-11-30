from models import db

class Delivery(db.Model):
    __tablename__ = "deliveries"

    id = db.Column(db.Integer, primary_key=True)
    package_id = db.Column(db.String(50), unique=True, nullable=False)
    driver_id = db.Column(db.String(50), nullable=False)
    customer_id = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(50), default="In Transit")
    payment_status = db.Column(db.String(50), default="Pending")
