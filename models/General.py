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

class General(peewee.Model):
    name = peewee.CharField()
    full_name = peewee.CharField()
    short_description = peewee.CharField()
    about = peewee.TextField()
    email = peewee.CharField()
    number_phone = peewee.CharField()
    github_link = peewee.CharField()
    linkedin_link = peewee.CharField()

    class Meta:
        database = db 

    def connect(self):
        try:
            General.create_table()
        except peewee.OperationalError:
            pass
