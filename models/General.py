from classes.Postgres import Postgres


class General(Postgres):
    def __init__(self):
        super().__init__('general')

    def insert_line(self, data: dict):
        cursor = self.connection.cursor()

        base_sql = f"""INSERT INTO {self.__table_name}(name,
                                                       full_name,
                                                       short_description,
                                                       about,
                                                       email,
                                                       number_phone,
                                                       github_link,
                                                       linkedin_link)
                            VALUES (%s,
                                    %s,
                                    %s,
                                    %s,
                                    %s,
                                    %s,
                                    %s,
                                    %s)
        """
        cursor.execute(base_sql, (
            data.get('name'),
            data.get('full_name'),
            data.get('about'),
            data.get('email'),
            data.get('number_phone'),
            data.get('number_phone'),
            data.get('linkedin_link'))
        )

        cursor.close()
        self.connection.commit()

    def select_by_language(self):
        cursor = self.connection.cursor()

        cursor.execute(f"""SELECT general.id,
                                  general_translate.language,
                                  general.name,
                                  general.full_name,
                                  general_translate.short_description,
                                  general_translate.about,
                                  general.email,
                                  general.number_phone,
                                  general.github_link,
                                  general.linkedin_link
                           FROM teste.general
                           INNER JOIN teste.general_translate
                           ON general_translate.fk_general = general.id
                           ORDER BY general.id
        """)
        result_db = cursor.fetchall()
        header = [desc[0] for desc in cursor.description]

        list_result = []
        for line in result_db:
            list_result.append(dict(zip(header, line)))

        cursor.close()
        return list_result
