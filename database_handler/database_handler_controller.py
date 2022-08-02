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

    def get_data_general(self):
        database = General()
        database.connect()
        result = database.select(
            General.name,
            General.short_description,
            General.number_phone,
            General.about,
            General.linkedin_link,
            General.github_link,
            General.email,
            General.full_name
        ).dicts()
        
        data = [(
            result[0]['name'],
            result[0]['full_name'],
            result[0]['short_description'],
            result[0]['about'],
            result[0]['email'],
            result[0]['number_phone'],
            result[0]['github_link'],
            result[0]['linkedin_link']
        )]
        return data

    def get_data_skills(self):
        database = Skills()
        database.connect()
        result = database.select(
            Skills.name,
            Skills.link_icon
        ).dicts()
        
        data = []
        for line in result:
            data.append((line['name'], line['link_icon']))
            
        return data
    
    def get_data_experience(self):
        database = Experience()
        database.connect()
        result = database.select(
            Experience.company,
            Experience.ocuppation,
            Experience.period
        ).dicts()
        
        data = []
        for line in result:
            data.append((line['company'], line['ocuppation'], line['period']))
            
        return data

    def get_data_formation(self):
        database = Formation()
        database.connect()
        result = database.select(
            Formation.institution,
            Formation.formation,
            Formation.period
        ).dicts()
        
        data = []
        for line in result:
            data.append((line['institution'], line['formation'], line['period']))
            
        return data

    def get_data_projects(self):
        database = Project()
        database.connect()
        result = database.select(
            Project.name,
            Project.description,
            Project.link,
            Project.languages
        ).dicts()
        
        data = []
        for line in result:
            data.append((line['name'], line['description'], line['link'], line['languages']))
            
        return data

    def get_data_blog(self):
        database = Blog()
        database.connect()
        result = database.select(
            Blog.name,
            Blog.description,
            Blog.link,
            Blog.categories
        ).dicts()
        
        data = []
        for line in result:
            data.append((line['name'], line['description'], line['link'], line['categories']))
            
        return data

    def save_data(self, data, number_tab):
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