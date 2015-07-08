from flask.ext.restful import Resource, reqparse
from .. import api
from . import make_api_url

class FriendsAPI(Resource):
    #decorators = [auth.login_required]
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

api.add_resource(FriendsAPI, make_api_url('friends'), endpoint = 'friends')
api.add_resource(FriendAPI, make_api_url('friend/<name>'), endpoint = 'friend')
