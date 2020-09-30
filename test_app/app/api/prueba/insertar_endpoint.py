# coding=utf-8
#########################################################
from flask import request, jsonify
from app.api import api
from app.controllers import CrudController


@api.route('/insertar', methods=['GET','POST'])
def insertar():
    title=request.args.get('title')
    description=request.args.get('description')
    message = CrudController.insertar_example(title,description)
    return jsonify(data=message)
