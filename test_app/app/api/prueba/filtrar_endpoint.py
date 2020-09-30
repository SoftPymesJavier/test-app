# coding=utf-8
#########################################################
from flask import request, jsonify
from app.api import api
from app.controllers import CrudController


@api.route('/filtrar', methods=['GET'])
def filtrar():
    filtro=request.args.get('filter')
    message = 'el filtro es ' + filtro
    #message = CrudController.filtrar_example(filtro)
    return jsonify(data=message)
