from flask_restful import Resource
from flask import request, Response, jsonify
from dotenv import load_dotenv
from os import getenv

from models.Formation import Formation as ModelFormation

class Formation(Resource):
    def get(self):
        database = ModelFormation()
        database.connect()
        result = database.select(
            ModelFormation.institution,
            ModelFormation.formation,
            ModelFormation.period
        ).dicts()

        if result:
            formations = []
            for formation in result:
                formations.append(formation)
                
            return jsonify(formations)
        else:
            return jsonify([])

    def post(self):
        load_dotenv()

        token = request.headers['Authorization']
        expected_token = getenv('TOKEN')
        if token == expected_token:
            args = request.json
            
            database_drop = ModelFormation()
            database_drop.drop_table()

            for item in args:

                database = ModelFormation()
                database.connect()

                database.institution = item['institution']
                database.formation = item['formation']
                database.period = item['period']
                
                database.save()
        else:
            return Response("{'status': 'Unauthorized'}", status=401, mimetype='application/json')