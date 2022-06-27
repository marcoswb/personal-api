from models.Experience import Experience

class Controller:

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
        print(data)