from models.Projects import Project

class Controller:

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
        print(data)