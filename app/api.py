from flask_restful import Api

from app.resources.Directory import GETRoot, GETDir

def build_api(app):
    api = Api()

    api.add_resource(GETRoot, '/api/directory')
    api.add_resource(GETDir, '/api/directory/<path:content>')

    api.init_app(app)

    return api
