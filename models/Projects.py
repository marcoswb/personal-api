from classes.Postgres import Postgres


class Project(Postgres):
    def __init__(self):
        super().__init__('project')

    def insert_line(self, data: dict):
        cursor = self.__connection.cursor()

        base_sql = f'INSERT INTO {self.__table_name}(name, description, link, languages) VALUES (%s, %s, %s, %s)'
        cursor.execute(base_sql, (data.get('name'), data.get('description'), data.get('link'), data.get('languages')))

        cursor.close()
        self.__connection.commit()
