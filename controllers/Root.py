from flask import jsonify
from flask_restful import Resource

from models.General import General
from models.Skills import Skills

class Root(Resource):
    def get(self):
        database = General()
        database.connect()
        result = database.select(
            General.name,
            General.occupation,
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