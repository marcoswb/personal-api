from models.Blog import Blog

class Controller:

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
        print(data)