from flask import Blueprint, request, make_response, jsonify
from flask.views import MethodView

from project.server import bcrypt, db
from project.server.models import User

index_blueprint = Blueprint('user', __name__)

class IndexAPI(MethodView):

    def get(self):
        response = []

        for user in User.query.all():
            responseObject = {
                "admin": user.admin,
                "email": user.email,
                "id": user.id,
                "registered_on": user.registered_on
            }
            response.append(responseObject)
        return make_response(jsonify(response)), 201

# define the API resources
index_view = IndexAPI.as_view('register_api')

# add Rules for API Endpoints
index_blueprint.add_url_rule(
    '/users/index',
    view_func=index_view,
    methods=['GET']
)