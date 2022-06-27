from models.Formation import Formation

class Controller:

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
        print(data)