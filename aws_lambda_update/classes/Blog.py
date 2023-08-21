import libs.peewee as peewee
import os

db = peewee.PostgresqlDatabase(
    os.environ['DB_DATABASE'],
    user=os.environ['DB_USER'],
    password=os.environ['DB_PASSWORD'],
    host=os.environ['DB_HOST'],
    autorollback=True
)

class Blog(peewee.Model):
    name = peewee.CharField()
    description = peewee.CharField()
    link = peewee.CharField()
    categories = peewee.CharField()

    class Meta:
        database = db 

    def connect(self):
        try:
            Blog.create_table()
        except:
            pass
