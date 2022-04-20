from flask import jsonify
from flask_restful import Resource

from models.Blog import Blog as ModelBlog

class Blog(Resource):
    def get(self):
        database = ModelBlog()
        database.connect()
        result = database.select(
            ModelBlog.title,
            ModelBlog.description,
            ModelBlog.tags,
            ModelBlog.link
        ).dicts()

        if result:
            blog_posts = []
            for posts in result:
                blog_posts.append(posts)
                
            return jsonify(blog_posts)
        else:
            return jsonify([])