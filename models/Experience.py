from classes.Postgres import Postgres


class Experience(Postgres):
    def __init__(self):
        super().__init__('experience')

    def insert_line(self, data: dict):
        cursor = self.__connection.cursor()

        base_sql = f'INSERT INTO {self.__table_name}(company, ocuppation, period) VALUES (%s, %s, %s)'
        cursor.execute(base_sql, (data.get('company'), data.get('occupation'), data.get('period')))

        cursor.close()
        self.__connection.commit()
