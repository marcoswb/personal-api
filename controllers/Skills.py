from flask import request, Response
from flask_restful import Resource
from dotenv import load_dotenv
from os import getenv

from models.Skills import Skills as ModelSkills


class Skills(Resource):
    @staticmethod
    def post():
        load_dotenv()

        token = request.headers['Authorization']
        expected_token = getenv('TOKEN')
        if token == expected_token:
            args = request.json
            
            skills_db = ModelSkills()
            skills_db.connect()
            skills_db.clear_table()

            for item in args:
                data = {
                    'name': item['name'],
                    'link_icon': item['link_icon'],
                }
                skills_db.insert_line(data)
            skills_db.close_connection()
        else:
            return Response("{'status': 'Unauthorized'}", status=401, mimetype='application/json')
