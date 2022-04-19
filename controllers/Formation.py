from flask import jsonify
from flask_restful import Resource

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