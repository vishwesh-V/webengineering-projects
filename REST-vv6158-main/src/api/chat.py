from flask import json,request
from flask.globals import session
from flask_restful import Resource, reqparse
from db import chat_db

parser = reqparse.RequestParser()
session_key = 0

class List_All_Users(Resource):
    """return all the the rows and columsn from the users table"""
    def get(self):
        return json.jsonify(chat_db.list_all_users())


class List_All_Communities_and_Channels(Resource):
    """return all data related to communities, including channels that are part of a community"""
    def get(self):
        return json.jsonify(chat_db.list_all_communities_and_channels())

class List_All_Specific_Messages(Resource):
    """return details on one specific channel"""
    def get(self):
        channel_name = request.args.get("channel_name")
        community_name = request.args.get("community_name")

        return json.jsonify(chat_db.list_messages_specific_channel(channel_name,community_name))
    
class Register(Resource):
    """Registers a new user"""

    def post(self):
        email = request.form['email']
        password = request.form['pass_word']

        return json.jsonify(chat_db.create_user(email, password))


class Login_User(Resource):
    """Logs a user in given email and password"""

    def post(self):
        global session_key

        email = request.form['email']
        password = request.form['pass_word']

        res = chat_db.generate_session_key(email, password)

        session_key = res[0]
        
        return json.jsonify(res)


class Logout_User(Resource):
    """Logs out user given session key"""

    def post(self):
        global session_key

        current_session_key = session_key

        session_key = 0

        return json.jsonify(chat_db.logout(current_session_key))


class UpdateUserInfo(Resource):
    """Updates user info given valid session key"""

    def put(self):
        global session_key

        new_email = request.form['email']
        new_password = request.form['pass_word']

        return json.jsonify(chat_db.edit_user(session_key, new_email, new_password))

    


class UserAPI(Resource):
    """UserAPI for create and delete CRUD methods"""

    def post(self):
        """Create new User"""
        global session_key

        new_email = request.form['email']
        new_password = request.form['pass_word']

        return json.jsonify(chat_db.create_user(new_email, new_password))

    def delete(self):
        """Deletes user"""
        global session_key

        parser.add_argument('email', type = str)
        args = parser.parse_args()

        return json.jsonify(chat_db.delete_user(args['email'], session_key))


class GetDirectMessages(Resource):
    """get dms for a given user"""

    def get(self):

        user = request.args.get("receiver")
        texts = request.args.get("number_of_messages", type= int)

        return json.jsonify(chat_db.get_direct_messages(user, (texts)))
