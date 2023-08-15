from flask_restful import Resource
from flask import request, Response, jsonify
from dotenv import load_dotenv
from os import getenv

from models.Formation import Formation as ModelFormation


class Formation(Resource):
    @staticmethod
    def get():
        formation_db = ModelFormation()
        formation_db.connect()
        result = formation_db.select()
        formation_db.close_connection()

        if result:
            formations = []
            for formation in result:
                formations.append(formation)
                
            return jsonify(formations)
        else:
            return jsonify([])

    @staticmethod
    def post():
        load_dotenv()

        token = request.headers['Authorization']
        expected_token = getenv('TOKEN')
        if token == expected_token:
            args = request.json
            
            formation_db = ModelFormation()
            formation_db.clear_table()
            formation_db.connect()

            for item in args:
                data = {
                    'institution': item['institution'],
                    'formation': item['formation'],
                    'period': item['period']
                }
                formation_db.insert_line(data)
            formation_db.close_connection()
        else:
            return Response("{'status': 'Unauthorized'}", status=401, mimetype='application/json')
