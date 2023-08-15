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
        result = experience_db.select()
        experience_db.close_connection()

        if result:
            experiences = []
            for experience in result:
                experiences.append(experience)
                
            return jsonify(experiences)
        else:
            return jsonify([])

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
        else:
            return Response("{'status': 'Unauthorized'}", status=401, mimetype='application/json')