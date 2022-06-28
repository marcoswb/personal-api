from flask import request, Response
from flask_restful import Resource
from dotenv import load_dotenv
from os import getenv

from models.Skills import Skills

class Skills(Resource):
    def post(self):
        load_dotenv()

        token = request.headers['Authorization']
        expected_token = getenv('TOKEN')
        if token == expected_token:
            args = request.json
            print(args)
        else:
            return Response("{'status': 'Unauthorized'}", status=401, mimetype='application/json')