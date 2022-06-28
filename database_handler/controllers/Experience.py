import requests
from dotenv import load_dotenv
from os import getenv

from models.Experience import Experience

class Controller:

    def __init__(self):
        load_dotenv()

    def get_data(self):
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