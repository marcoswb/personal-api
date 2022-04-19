import peewee
from dotenv import load_dotenv
from os import getenv

load_dotenv()
db = peewee.PostgresqlDatabase(
    getenv('DB_DATABASE'),
    user=getenv('DB_USER'),
    password=getenv('DB_PASSWORD'),
    host=getenv('DB_HOST')
)

class Formation(peewee.Model):
    institution = peewee.CharField()
    formation = peewee.CharField()
    period = peewee.CharField()

    class Meta:
        database = db 

    def connect(self):
        try:
            Formation.create_table()
        except peewee.OperationalError:
            pass
