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

class Experience(peewee.Model):
    company = peewee.CharField()
    ocuppation = peewee.CharField()
    period = peewee.CharField()

    class Meta:
        database = db 

    def connect(self):
        try:
            Experience.create_table()
        except peewee.OperationalError:
            pass
