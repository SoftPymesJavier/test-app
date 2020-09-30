# coding=utf-8
#########################################################
from flask import request, jsonify
from app.api import api
from app.controllers import CrudController


@api.route('/consultar', methods=['GET'])
def consultar():
    #message = 'consultando datos'
    message= CrudController.consultar_example()
    return jsonify(data=message)
