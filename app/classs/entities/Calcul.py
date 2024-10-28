##entité qui represente un calcule
from peewee import CharField
from app.classs.database.BaseModelMYSQL import BaseModelMYSQL

class Calcul(BaseModelMYSQL):
    calcul = CharField()
    result = CharField()