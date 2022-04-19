from flask import jsonify
from flask_restful import Resource

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