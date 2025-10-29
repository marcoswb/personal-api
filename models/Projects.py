from classes.Postgres import Postgres


class Project(Postgres):
    def __init__(self):
        super().__init__('project')

    def insert_line(self, data: dict):
        cursor = self.connection.cursor()

        base_sql = f'INSERT INTO {self.__table_name}(name, description, link, languages) VALUES (%s, %s, %s, %s)'
        cursor.execute(base_sql, (data.get('name'), data.get('description'), data.get('link'), data.get('languages')))

        cursor.close()
        self.connection.commit()

    def select_by_language(self):
        cursor = self.connection.cursor()

        cursor.execute(f"""SELECT project.id,
                                  project_translate.language,
                                  project_translate.name,
                                  project_translate.description,
                                  project_translate.languages,
                                  project.link
                            FROM {self.schema}.project
                            INNER JOIN {self.schema}.project_translate
                            ON project_translate.fk_project = project.id
                            ORDER BY project.order
        """)
        result_db = cursor.fetchall()
        header = [desc[0] for desc in cursor.description]

        list_result = []
        for line in result_db:
            list_result.append(dict(zip(header, line)))

        cursor.close()
        return list_result
