##script de migration

from app.classs.database.BaseModelMYSQL import db
from app.classs.entities.Calcul import Calcul

db.connect()
db.drop_tables([Calcul])
db.create_tables([Calcul], safe=True)
db.close()

