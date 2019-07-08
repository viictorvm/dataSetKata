from os import environ
from pathlib import Path

from dotenv import load_dotenv

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

API_PORT = environ.get("API_PORT")
DB_POSTGRES = environ.get("DB")
