from classes.Postgres import Postgres


class Formation(Postgres):
    def __init__(self):
        super().__init__('formation')

    def insert_line(self, data: dict):
        cursor = self.__connection.cursor()

        base_sql = f'INSERT INTO {self.__table_name}(institution, formation, period) VALUES (%s, %s, %s)'
        cursor.execute(base_sql, (data.get('institution'), data.get('formation'), data.get('period')))

        cursor.close()
        self.__connection.commit()
