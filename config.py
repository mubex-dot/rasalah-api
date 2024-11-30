import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    AT_USERNAME = os.getenv("AT_USERNAME")
    AT_API_KEY = os.getenv("AT_API_KEY")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
