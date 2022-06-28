import requests
from dotenv import load_dotenv
from os import getenv

from models.Skills import Skills

class Controller:

    def __init__(self):
        load_dotenv()

    def get_data(self):
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
    
    def save_data(self, data):
        try:
            headers = {
                'Authorization': getenv('TOKEN')
            }
            response = requests.post(f"{getenv('ENDPOINT_API')}/skills", json=data, headers=headers)
            if response.status_code == 200:
                return True, ''
            elif response.status_code == 401:
                return False, 'Unauthorized'
            
            return False, ''
        except:
            return False, ''