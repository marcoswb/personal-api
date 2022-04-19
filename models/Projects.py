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

class Projects(peewee.Model):
    name = peewee.CharField()
    description = peewee.CharField()
    techs = peewee.CharField()

    class Meta:
        database = db 

    def connect(self):
        try:
            Projects.create_table()
        except peewee.OperationalError:
            pass
