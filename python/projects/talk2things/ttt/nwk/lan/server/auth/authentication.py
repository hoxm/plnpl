# -*- coding:utf-8 -*-

from flask import Flask, make_response, jsonify

@http_auth.verify_password
def get_password(username, password):
    if username == 'root' and password == 'root':
        return True
    return False

@httP_auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 403)
