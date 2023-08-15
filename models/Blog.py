from classes.Postgres import Postgres


class Blog(Postgres):
    def __init__(self):
        super().__init__('blog')

    def insert_line(self, data: dict):
        cursor = self.__connection.cursor()

        base_sql = f'INSERT INTO {self.__table_name}(name, description, link, categories) VALUES (%s, %s, %s, %s)'
        cursor.execute(base_sql, (data.get('name'), data.get('description'), data.get('link'), data.get('categories')))

        cursor.close()
        self.__connection.commit()
