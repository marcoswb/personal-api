from flask_restful import Resource
from flask import request, Response, jsonify
from dotenv import load_dotenv
from os import getenv

from models.General import General
from models.Skills import Skills

class Root(Resource):
    def get(self):
        database = General()
        database.connect()
        result = database.select(
            General.name,
            General.short_description,
            General.number_phone,
            General.about,
            General.linkedin_link,
            General.github_link,
            General.email,
            General.full_name
        ).dicts()
        
        database = Skills()
        database.connect()
        result_skills = database.select(
            Skills.name,
            Skills.link_icon
        ).dicts()
        
        result[0]['skills'] = []
        for skill in result_skills:
            result[0]['skills'].append(skill)

        return jsonify(result[0])

    def post(self):
        load_dotenv()

        token = request.headers['Authorization']
        expected_token = getenv('TOKEN')
        if token == expected_token:
            args = request.json

            database_drop = General()
            database_drop.drop_table()

            for item in args:

                database = General()
                database.connect()

                database.name = item['name']
                database.full_name = item['full_name']
                database.short_description = item['short_description']
                database.about = item['about']
                database.email = item['email']
                database.number_phone = item['number_phone']
                database.github_link = item['github_link']
                database.linkedin_link = item['linkedin_link']
                
                database.save()
        else:
            return Response("{'status': 'Unauthorized'}", status=401, mimetype='application/json')