from flask_restful import Resource, request
from managers.auth_manager import get_authentication, TokenManger
from models.user_register import AllUsers


class RefreshToken(Resource):
    def get(self):
        received_token = get_authentication()
        user_information = TokenManger.decode_refresh_token(received_token['token'])
        user = AllUsers.query.filter_by(id=user_information["sub"]).first()
        return TokenManger.encode_access_token(user)