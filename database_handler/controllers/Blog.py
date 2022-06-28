import requests
from dotenv import load_dotenv
from os import getenv

from models.Blog import Blog

class Controller:

    def __init__(self):
        load_dotenv()

    def get_data(self):
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
    
    def save_data(self, data):
        try:
            headers = {
                'Authorization': getenv('TOKEN')
            }
            response = requests.post(f"{getenv('ENDPOINT_API')}/blog", json=data, headers=headers)
            if response.status_code == 200:
                return True, ''
            elif response.status_code == 401:
                return False, 'Unauthorized'
            
            return False, ''
        except:
            return False, ''