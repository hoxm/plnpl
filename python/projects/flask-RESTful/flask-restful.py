from flask import Flask, make_response, jsonify
from flask.ext.restful import Api, Resource, reqparse
from flask.ext.httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()

@auth.verify_password
def get_password(username, password):
    if username == 'root' and password == 'root':
        return True
    return False

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 403)

app = Flask(__name__)
api = Api(app)

class FriendsAPI(Resource):
    decorators = [auth.login_required]
    def get(self):
        return "Show all friends!"

class FriendAPI(Resource):
    def __init__(self):
        self.parse = reqparse.RequestParser()
        self.parse.add_argument('name', type = str, required = True,
                help = 'Name of the friend', location = 'json')
        self.parse.add_argument('alias', type = str, location = 'json')
        self.parse.add_argument('commnad', type = bool, location = 'json')
        super(FriendAPI, self).__init__()

    def get(self, name):
        return "Get one friend: " + name

    #curl -i -H "Content-Type: application/json" -X PUT 
    #     -d '{"name":"hoxm", "alias":"test1"}'
    #     http://localhost:5000/api/v1.0/friend/hoxm
    def put(self, name):
        args = self.parse.parse_args()
        rstr = "Update friend: " + name 
        for k, v in args.iteritems():
            rstr += " %s:%s" %(k, v)
        return rstr

    def delete(self, name):
        return "Delete friend: " + name

api.add_resource(FriendsAPI, '/api/v1.0/friends', endpoint = 'friends')
api.add_resource(FriendAPI, '/api/v1.0/friend/<name>', endpoint = 'friend')

if __name__ == '__main__':
    app.run(debug=True)
