from classes.Postgres import Postgres


class Skills(Postgres):
    def __init__(self):
        super().__init__('skills')

    def insert_line(self, data: dict):
        cursor = self.connection.cursor()

        base_sql = f'INSERT INTO {self.__table_name}(name, link_icon) VALUES (%s, %s)'
        cursor.execute(base_sql, (data.get('name'), data.get('link_icon')))

        cursor.close()
        self.connection.commit()
