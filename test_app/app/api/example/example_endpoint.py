# coding=utf-8
#########################################################
from flask import request, jsonify
from app.api import api
from app.controllers import ExampleController


@api.route('/example', methods=['GET'])
def example():
    message = ExampleController.get_example()
    return jsonify(data=message)

