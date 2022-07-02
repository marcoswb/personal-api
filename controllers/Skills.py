from flask import request, Response
from flask_restful import Resource
from dotenv import load_dotenv
from os import getenv

from models.Skills import Skills as ModelSkills

class Skills(Resource):
    def post(self):
        load_dotenv()

        token = request.headers['Authorization']
        expected_token = getenv('TOKEN')
        if token == expected_token:
            args = request.json
            
            database_drop = ModelSkills()
            database_drop.drop_table()

            for item in args:

                database = ModelSkills()
                database.connect()

                database.name = item['name']
                database.link_icon = item['link_icon']
                
                database.save()
        else:
            return Response("{'status': 'Unauthorized'}", status=401, mimetype='application/json')