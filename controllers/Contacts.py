from flask import jsonify
from flask_restful import Resource
from models.General import General

class Contacts(Resource):
    def get(self):
        database = General()
        database.connect()
        result = database.select(
            General.linkedin_link,
            General.github_link,
            General.email,
            General.number_phone
        ).dicts()

        return jsonify(result[0])