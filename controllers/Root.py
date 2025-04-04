from flask_restful import Resource
from flask import jsonify

from models.General import General
from models.Skills import Skills


class Root(Resource):
    @staticmethod
    def get():
        general_db = General()
        general_db.connect()
        result = general_db.select_by_language()
        general_db.close_connection()
        
        skills_db = Skills()
        skills_db.connect()
        result_skills = skills_db.select()
        skills_db.close_connection()

        result_dict = {}
        if result:
            for line in result:
                line.setdefault('skills', [])
                for skill in result_skills:
                    line['skills'].append(skill)

                result_dict[line.get('language')] = line

        return jsonify(result_dict)
