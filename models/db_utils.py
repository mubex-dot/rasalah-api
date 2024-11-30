from models import db

def init_db(app):
    """
    Initialize the database.
    """
    with app.app_context():
        db.create_all()
