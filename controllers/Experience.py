from flask import jsonify
from flask_restful import Resource

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
