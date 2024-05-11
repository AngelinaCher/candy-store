import os

from dotenv import load_dotenv

load_dotenv()

# Подключение к БД
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

# Секретный ключ приложения
SECRET_KEY = os.getenv("SECRET_KEY")
# Секретный ключ для jwt-токена
SIGNING_KEY = os.getenv("SIGNING_KEY_JWT")

# Настройка почты
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL')
