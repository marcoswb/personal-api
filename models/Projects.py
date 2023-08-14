# import psycopg2
# from dotenv import load_dotenv
# from os import getenv
#
# load_dotenv()
#
#
# class Postgres:
#     def __init__(self):
#         self.__connection = None
#
#     def connect(self):
#         psycopg2.connect(
#             dbname=getenv('DB_DATABASE'),
#             user=getenv('DB_USER'),
#             password=password,
#             host=host,
#             port=port
#         )
#
#     name = peewee.CharField(max_length=50)
#     description = peewee.CharField(max_length=200)
#     link = peewee.CharField(max_length=100)
#     languages = peewee.CharField(max_length=100)
#
#     class Meta:
#         database = db
#
#     @staticmethod
#     def connect():
#         try:
#             Project.create_table()
#         except peewee.OperationalError:
#             pass
#
#     @staticmethod
#     def close_connection():
#         db.close()

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