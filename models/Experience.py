from classes.Postgres import Postgres


class Experience(Postgres):
    def __init__(self):
        super().__init__('experience')

    def insert_line(self, data: dict):
        cursor = self.connection.cursor()

        base_sql = f'INSERT INTO {self.__table_name}(company, ocuppation, period) VALUES (%s, %s, %s)'
        cursor.execute(base_sql, (data.get('company'), data.get('occupation'), data.get('period')))

        cursor.close()
        self.connection.commit()

    def select_by_language(self):
        cursor = self.connection.cursor()

        cursor.execute(f"""SELECT experience.id,
                                  experience_translate.language,
                                  experience_translate.company,
                                  experience_translate.ocuppation,
                                  experience_translate.period
                            FROM teste.experience
                            INNER JOIN teste.experience_translate
                            ON experience_translate.fk_experience = experience.id
                            ORDER BY experience.id
        """)
        result_db = cursor.fetchall()
        header = [desc[0] for desc in cursor.description]

        list_result = []
        for line in result_db:
            list_result.append(dict(zip(header, line)))

        cursor.close()
        return list_result
