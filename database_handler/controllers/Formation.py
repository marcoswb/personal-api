import requests
from dotenv import load_dotenv
from os import getenv

from models.Formation import Formation

class Controller:

    def __init__(self):
        load_dotenv()

    def get_data(self):
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
    
    def save_data(self, data):
        try:
            headers = {
                'Authorization': getenv('TOKEN')
            }
            response = requests.post(f"{getenv('ENDPOINT_API')}/formation", json=data, headers=headers)
            if response.status_code == 200:
                return True, ''
            elif response.status_code == 401:
                return False, 'Unauthorized'
            
            return False, ''
        except:
            return False, ''