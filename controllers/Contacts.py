from flask import jsonify
from flask_restful import Resource

from models.General import General


class Contacts(Resource):
    @staticmethod
    def get():
        general_db = General()
        general_db.connect()
        result = general_db.select()
        general_db.close_connection()

        return jsonify(result[0])
