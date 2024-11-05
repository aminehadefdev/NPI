import os
from dotenv import load_dotenv
from pathlib import Path

from peewee import MySQLDatabase, Model

dotenv_path = Path(".env")
load_dotenv(dotenv_path=dotenv_path)

class config:
    MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")
    MYSQL_USER = os.getenv("MYSQL_USER")
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
    MYSQL_ADRESS = os.getenv("MYSQL_ADRESS")
    MYSQL_PORT = int(os.getenv("MYSQL_PORT"))

    ORIGINS = [
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ]

    DOWLOAD_PATH = "/app/Dowload/"
    
    @staticmethod
    def get_attr(attr):
        return getattr(config, attr, None)

