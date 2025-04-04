from flask import jsonify
from flask_restful import Resource

from models.Blog import Blog as ModelBlog


class Blog(Resource):

    @staticmethod
    def get():
        blog_db = ModelBlog()
        blog_db.connect()
        result = blog_db.select_by_language()
        blog_db.close_connection()

        blog_posts = {}
        if result:
            for post in result:
                blog_posts.setdefault(post.get('language'), [])

                blog_posts[post.get('language')].append({
                    'id': post.get('id'),
                    'name': post.get('name'),
                    'description': post.get('description'),
                    'link': post.get('link'),
                    'categories': post.get('categories').split(',')
                })

        return jsonify(blog_posts)
