from classes.Postgres import Postgres


class Formation(Postgres):
    def __init__(self):
        super().__init__('formation')

    def insert_line(self, data: dict):
        cursor = self.connection.cursor()

        base_sql = f'INSERT INTO {self.__table_name}(institution, formation, period) VALUES (%s, %s, %s)'
        cursor.execute(base_sql, (data.get('institution'), data.get('formation'), data.get('period')))

        cursor.close()
        self.connection.commit()

    def select_by_language(self):
        cursor = self.connection.cursor()

        cursor.execute(f"""SELECT formation.id,
                                  formation_translate.language,
                                  formation_translate.institution,
                                  formation_translate.formation,
                                  formation_translate.period
                            FROM teste.formation
                            INNER JOIN teste.formation_translate
                            ON formation_translate.fk_formation = formation.id
                            ORDER BY formation.id
        """)
        result_db = cursor.fetchall()
        header = [desc[0] for desc in cursor.description]

        list_result = []
        for line in result_db:
            list_result.append(dict(zip(header, line)))

        cursor.close()
        return list_result
