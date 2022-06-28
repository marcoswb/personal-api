import requests
from dotenv import load_dotenv
from os import getenv

from models.Projects import Project

class Controller:

    def __init__(self):
        load_dotenv()

    def get_data(self):
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
    
    def save_data(self, data):
        try:
            headers = {
                'Authorization': getenv('TOKEN')
            }
            response = requests.post(f"{getenv('ENDPOINT_API')}/projects", json=data, headers=headers)
            if response.status_code == 200:
                return True, ''
            elif response.status_code == 401:
                return False, 'Unauthorized'
            
            return False, ''
        except:
            return False, ''