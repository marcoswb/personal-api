import psycopg2
from dotenv import load_dotenv
from os import getenv

load_dotenv()


class Postgres:
    def __init__(self):
        self.__connection = None
        self.__table_name = 'project'

    def connect(self):
        self.__connection = psycopg2.connect(
                                dbname=getenv('DB_DATABASE'),
                                user=getenv('DB_USER'),
                                password=getenv('DB_PASSWORD'),
                                host=getenv('DB_HOST'),
                                port=5432
                            )

    def insert_project(self, name, description, link, languages):
        cursor = self.__connection.cursor()

        base_sql = f'INSERT INTO {self.__table_name} (name, description, link, languages) VALUES (%s, %s, %s, %s)'
        cursor.execute(base_sql, (name, description, link, languages))

        cursor.close()
        self.__connection.commit()

    def clear_table(self):
        cursor = self.__connection.cursor()

        sql_script = f'DELETE FROM {self.__table_name}'
        cursor.execute(sql_script)

        cursor.close()
        self.__connection.commit()

    def close_connection(self):
        self.__connection.close()
