from flask_restful import Resource
from flask import request, Response, jsonify
from dotenv import load_dotenv
from os import getenv

from models.General import General
from models.Skills import Skills


class Root(Resource):
    @staticmethod
    def get():
        general_db = General()
        general_db.connect()
        result = general_db.select()
        general_db.close_connection()
        
        skills_db = Skills()
        skills_db.connect()
        result_skills = skills_db.select()
        skills_db.close_connection()
        
        result[0]['skills'] = []
        for skill in result_skills:
            result[0]['skills'].append(skill)

        return jsonify(result[0])

    @staticmethod
    def post():
        load_dotenv()

        token = request.headers['Authorization']
        expected_token = getenv('TOKEN')
        if token == expected_token:
            args = request.json

            general_db = General()
            general_db.connect()
            general_db.clear_table()

            for item in args:
                data = {
                    'name': item.get('name'),
                    'full_name': item.get('full_name'),
                    'short_description': item.get('short_description'),
                    'about': item.get('about'),
                    'email': item.get('email'),
                    'number_phone': item.get('number_phone'),
                    'github_link': item.get('github_link'),
                    'linkedin_link': item.get('linkedin_link'),
                }
                general_db.insert_line(data)
        else:
            return Response("{'status': 'Unauthorized'}", status=401, mimetype='application/json')
