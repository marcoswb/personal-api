from flask import request, Response, jsonify
from flask_restful import Resource
from dotenv import load_dotenv
from os import getenv

from models.Experience import Experience as ModelExperience

class Experience(Resource):
    def get(self):
        database = ModelExperience()
        database.connect()
        result = database.select(
            ModelExperience.company,
            ModelExperience.ocuppation,
            ModelExperience.period
        ).dicts()

        if result:
            experiences = []
            for experience in result:
                experiences.append(experience)
                
            return jsonify(experiences)
        else:
            return jsonify([])

    def post(self):
        load_dotenv()

        token = request.headers['Authorization']
        expected_token = getenv('TOKEN')
        if token == expected_token:
            args = request.json
            print(args)
        else:
            return Response("{'status': 'Unauthorized'}", status=401, mimetype='application/json')