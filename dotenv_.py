import os

import dotenv

dotenv.load_dotenv()

APP_POSTGRES_HOST = os.getenv(
    "APP_POSTGRES_HOST", ""
)
APP_POSTGRES_PORT = os.getenv(
    "APP_POSTGRES_PORT", ""
)
APP_PROTOKOL = os.getenv(
    "APP_PROTOKOL", ""
)
APP_POSTGRES_PASS = os.getenv(
    "APP_POSTGRES_PASS", ""
)
APP_POSTGRES_LOGIN = os.getenv(
    "APP_POSTGRES_LOGIN", ""
)
APP_POSTGRES_DBNAME = os.getenv(
    "APP_POSTGRES_DBNAME", ""
)
DATABASE_URL = f"postgresql://{APP_POSTGRES_LOGIN}:{APP_POSTGRES_PASS}@{APP_POSTGRES_HOST}/{APP_POSTGRES_DBNAME}"