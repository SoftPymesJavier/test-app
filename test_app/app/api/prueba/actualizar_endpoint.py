# coding=utf-8
#########################################################
from flask import request, jsonify
from app.api import api
from app.controllers import CrudController


@api.route('/actualizar', methods=['GET','POST'])
def actualizar():
    Exampleid=request.args.get('id')
    title=request.args.get('title')
    description=request.args.get('description')
    message=CrudController.actualizar_example(Exampleid,title,description)
    return jsonify(data=message)
