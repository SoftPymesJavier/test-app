# coding=utf-8
#########################################################
from flask import request, jsonify
from app.api import api
from app.controllers import CrudController


@api.route('/actualizar', methods=['GET','POST'])
def actualizar():
    id=request.args.get('id')
    title=request.args.get('title')
    description=request.args.get('description')
    #message=CrudController.actualizar_example(id,title,description)
    message = 'id a actualizar ' + id +' con los datos: ' + title + description
    return jsonify(data=message)
