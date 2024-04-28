import os

from dotenv import load_dotenv

load_dotenv()

# Подключение к БД
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")

secret_key = os.getenv("SECRET_KEY")
signing_key = os.getenv("SIGNING_KEY_JWT")

redis_url = os.getenv("REDIS_URL")
