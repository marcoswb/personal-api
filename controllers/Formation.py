from flask_restful import Resource
from flask import jsonify

from models.Formation import Formation as ModelFormation


class Formation(Resource):
    @staticmethod
    def get():
        formation_db = ModelFormation()
        formation_db.connect()
        result = formation_db.select_by_language()
        formation_db.close_connection()

        formations = {}
        if result:
            for formation in result:
                formations.setdefault(formation.get('language'), [])
                formations[formation.get('language')].append(formation)

        return jsonify(formations)
