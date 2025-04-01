from classes.Postgres import Postgres


class Blog(Postgres):
    def __init__(self):
        super().__init__('blog')

    def insert_line(self, data: dict):
        cursor = self.connection.cursor()

        base_sql = f'INSERT INTO {self.__table_name}(name, description, link, categories) VALUES (%s, %s, %s, %s)'
        cursor.execute(base_sql, (data.get('name'), data.get('description'), data.get('link'), data.get('categories')))

        cursor.close()
        self.connection.commit()

    def select_by_language(self):
        cursor = self.connection.cursor()

        cursor.execute(f"""SELECT blog.id,
                                  blog_translate.language,
                                  blog_translate.name,
                                  blog_translate.description,
                                  blog_translate.categories,
                                  blog.link
                           FROM {self.schema}.blog
                           INNER JOIN {self.schema}.blog_translate
                           ON blog_translate.fk_blog = blog.id
                           ORDER BY blog.id
        """)
        result_db = cursor.fetchall()
        header = [desc[0] for desc in cursor.description]

        list_result = []
        for line in result_db:
            list_result.append(dict(zip(header, line)))

        cursor.close()
        return list_result
