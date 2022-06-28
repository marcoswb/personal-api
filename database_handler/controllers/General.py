import requests
from dotenv import load_dotenv
from os import getenv

from models.General import General

class Controller:

    def __init__(self):
        load_dotenv()

    def get_data(self):
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
    
    def save_data(self, data):
        try:
            headers = {
                'Authorization': getenv('TOKEN')
            }
            response = requests.post(getenv('ENDPOINT_API'), json=data[0], headers=headers)
            if response.status_code == 200:
                return True, ''
            elif response.status_code == 401:
                return False, 'Unauthorized'
            
            return False, ''
        except:
            return False, ''