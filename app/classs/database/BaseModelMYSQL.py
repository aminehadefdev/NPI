##script de connection a la base de donnée

import os
from dotenv import load_dotenv
from pathlib import Path

from peewee import MySQLDatabase, Model

dotenv_path = Path(".env")
load_dotenv(dotenv_path=dotenv_path)

db = MySQLDatabase(os.getenv("MYSQL_DATABASE"), user=os.getenv("MYSQL_USER"), password=os.getenv("MYSQL_PASSWORD"), host=os.getenv("MYSQL_ADRESS"), port=3306)
class BaseModelMYSQL(Model):
    class Meta:
        database = db