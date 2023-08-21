from classes.Postgres import Postgres


class General(Postgres):
    def __init__(self):
        super().__init__('general')

    def insert_line(self, data: dict):
        cursor = self.__connection.cursor()

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
        self.__connection.commit()
