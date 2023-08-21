import requests
from dotenv import load_dotenv
from os import getenv

from models.General import General
from models.Skills import Skills
from models.Experience import Experience
from models.Formation import Formation
from models.Projects import Project
from models.Blog import Blog


class Controller:

    def __init__(self):
        load_dotenv()

    def get_data(self, number_tab):
        if number_tab == 0:
            return self.get_data_general()
        elif number_tab == 1:
            return self.get_data_skills()
        elif number_tab == 2:
            return self.get_data_experience()
        elif number_tab == 3:
            return self.get_data_formation()
        elif number_tab == 4:
            return self.get_data_projects()
        elif number_tab == 5:
            return self.get_data_blog()
        else:
            return []

    @staticmethod
    def get_data_general():
        database = General()
        database.connect()
        result = database.select()

        data = []
        if result:
            data.append((
                result[0]['name'],
                result[0]['full_name'],
                result[0]['short_description'],
                result[0]['about'],
                result[0]['email'],
                result[0]['number_phone'],
                result[0]['github_link'],
                result[0]['linkedin_link']
            ))

        database.close_connection()
        return data

    @staticmethod
    def get_data_skills():
        database = Skills()
        database.connect()
        result = database.select()
        
        data = []
        for line in result:
            data.append((line['name'], line['link_icon']))

        database.close_connection()
        return data
    
    @staticmethod
    def get_data_experience():
        database = Experience()
        database.connect()
        result = database.select()
        
        data = []
        for line in result:
            data.append((line['company'], line['ocuppation'], line['period']))

        database.close_connection()
        return data

    @staticmethod
    def get_data_formation():
        database = Formation()
        database.connect()
        result = database.select()
        
        data = []
        for line in result:
            data.append((line['institution'], line['formation'], line['period']))

        database.close_connection()
        return data

    @staticmethod
    def get_data_projects():
        database = Project()
        database.connect()
        result = database.select()
        
        data = []
        for line in result:
            data.append((line['name'], line['description'], line['link'], line['languages']))

        database.close_connection()
        return data

    @staticmethod
    def get_data_blog():
        database = Blog()
        database.connect()
        result = database.select()
        
        data = []
        for line in result:
            data.append((line['name'], line['description'], line['link'], line['categories']))

        database.close_connection()
        return data

    @staticmethod
    def save_data(data, number_tab):
        try:
            endpoint_dict = {
                0: '/',
                1: '/skills',
                2: '/experience',
                3: '/formation',
                4: '/projects',
                5: '/blog',
            }

            endpoint = endpoint_dict[number_tab]
            headers = {
                'Authorization': getenv('TOKEN')
            }

            response = requests.post(f"{getenv('ENDPOINT_API')}{endpoint}", json=data, headers=headers)
            if response.status_code == 200:
                return True, ''
            elif response.status_code == 401:
                return False, 'Unauthorized'
            
            return False, ''
        except Exception as e:
            return False, e
