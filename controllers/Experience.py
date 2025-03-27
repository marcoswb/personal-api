from flask import request, Response, jsonify
from flask_restful import Resource
from dotenv import load_dotenv
from os import getenv

from models.Experience import Experience as ModelExperience


class Experience(Resource):
    @staticmethod
    def get():
        experience_db = ModelExperience()
        experience_db.connect()
        result = experience_db.select_by_language()
        experience_db.close_connection()

        experiences = {}
        if result:
            for experience in result:
                experiences.setdefault(experience.get('language'), [])
                experiences[experience.get('language')].append(experience)
                
        return jsonify(experiences)

    @staticmethod
    def post():
        load_dotenv()

        token = request.headers['Authorization']
        expected_token = getenv('TOKEN')
        if token == expected_token:
            args = request.json
            
            experience_db = ModelExperience()
            experience_db.connect()
            experience_db.clear_table()

            for item in args:
                data = {
                    'company': item['company'],
                    'occupation': item['occupation'],
                    'period': item['period']
                }
                experience_db.insert_line(data)
            experience_db.close_connection()
        else:
            return Response("{'status': 'Unauthorized'}", status=401, mimetype='application/json')
