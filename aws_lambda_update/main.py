import psycopg2
from controllers.update_blog import UpdateBlog
from controllers.update_projects import UpdateProjects

def start(event, context):
    UpdateBlog().update()
    UpdateProjects().update()
