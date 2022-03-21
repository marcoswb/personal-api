from flask import Flask
from flask_restful import Api

from classes.Root import Root

app = Flask(__name__)
api = Api(app)

api.add_resource(Root, '/')

if __name__ == '__main__':
    app.run()