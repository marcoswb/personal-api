from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from controllers.Root import Root
from controllers.Experience import Experience
from controllers.Formation import Formation
from controllers.Projects import Projects
from controllers.Blog import Blog
from controllers.Contacts import Contacts
from controllers.Skills import Skills

app = Flask(__name__)
CORS(app)

api = Api(app)

api.add_resource(Root, '/')
api.add_resource(Experience, '/experience')
api.add_resource(Formation, '/formation')
api.add_resource(Projects, '/projects')
api.add_resource(Blog, '/blog')
api.add_resource(Contacts, '/contacts')
api.add_resource(Skills, '/skills')

if __name__ == '__main__':
    app.run()