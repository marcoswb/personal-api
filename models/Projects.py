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


class Project(peewee.Model):
    name = peewee.CharField()
    description = peewee.CharField()
    link = peewee.CharField()
    languages = peewee.CharField()

    class Meta:
        database = db 

    @staticmethod
    def connect():
        try:
            Project.create_table()
        except peewee.OperationalError:
            pass

    @staticmethod
    def close_connection():
        db.close()
