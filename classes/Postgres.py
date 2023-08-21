import psycopg2
from dotenv import load_dotenv
from os import getenv

load_dotenv()


class Postgres:
    def __init__(self, table_name):
        self.__connection = None
        self.__table_name = str(table_name)

    def connect(self):
        self.__connection = psycopg2.connect(
                                dbname=getenv('DB_DATABASE'),
                                user=getenv('DB_USER'),
                                password=getenv('DB_PASSWORD'),
                                host=getenv('DB_HOST'),
                                port=5432
                            )

    def insert_line(self, data: dict):
        pass

    def select(self):
        cursor = self.__connection.cursor()

        cursor.execute(f'SELECT * FROM {self.__table_name}')
        result_db = cursor.fetchall()
        header = [desc[0] for desc in cursor.description]

        list_result = []
        for line in result_db:
            list_result.append(dict(zip(header[1:], line[1:])))

        cursor.close()
        return list_result

    def clear_table(self):
        cursor = self.__connection.cursor()

        sql_script = f'DELETE FROM {self.__table_name}'
        cursor.execute(sql_script)

        cursor.close()
        self.__connection.commit()

    def close_connection(self):
        self.__connection.close()
