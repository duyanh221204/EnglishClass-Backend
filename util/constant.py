import os

from dotenv import load_dotenv

load_dotenv()


class Constant:
    DB_USERNAME = os.getenv("DB_USERNAME")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")
    DB_DATABASE = os.getenv("DB_DATABASE")

    SECRET_KEY = os.getenv("SECRET_KEY")
    ALGORITHM = os.getenv("ALGORITHM")
    ACCESS_TOKEN_EXPIRED_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRED_MINUTES")

    ADMIN_USERNAME = os.getenv("ADMIN_USERNAME")
    ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")
    ADMIN_FIRST_NAME = os.getenv("ADMIN_FIRST_NAME")
    ADMIN_LAST_NAME = os.getenv("ADMIN_LAST_NAME")
    ADMIN_EMAIL = os.getenv("ADMIN_EMAIL")
    ADMIN_PHONE = os.getenv("ADMIN_PHONE")
    ADMIN_DOB = os.getenv("ADMIN_DOB")
