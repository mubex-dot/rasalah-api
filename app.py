from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    # Import and register routes
    from .routes.init_route import bp
    from .routes.ussd_routes import ussd_bp
    from .routes.sms_routes import sms_bp
    from .routes.payment_routes import payment_bp

    app.register_blueprint(bp)
    app.register_blueprint(ussd_bp)
    app.register_blueprint(sms_bp)
    app.register_blueprint(payment_bp)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
