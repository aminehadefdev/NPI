##script de connection a la base de donnée
from app.config.config import config


db = MySQLDatabase(config.get_attr("MYSQL_DATABASE"), user=config.get_attr("MYSQL_USER"), password=config.get_attr("MYSQL_PASSWORD"), host=config.get_attr("MYSQL_ADRESS"), port=config.get_attr("MYSQL_PORT"))
class BaseModelMYSQL(Model):
    class Meta:
        database = db