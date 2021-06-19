from flask_restful import Api, Resource

from src.handlers.user import UsersHandler, UserHandler


def init_resources(app):
    api = Api()

    api.add_resource(HealthCheckHandler, "/workshop/health-check")
    api.add_resource(UsersHandler, "/workshop/users/v1")
    api.add_resource(UserHandler, "/workshop/users/v1/<id>")

    api.init_app(app)


class HealthCheckHandler(Resource):

    @staticmethod
    def get():
        return 'ok'
