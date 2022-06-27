from models.Skills import Skills

class Controller:

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
        print(data)