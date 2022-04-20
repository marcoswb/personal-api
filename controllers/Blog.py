from flask import jsonify
from flask_restful import Resource

class Blog(Resource):
    def get(self):
        blog_posts = []
        
        return jsonify(blog_posts)