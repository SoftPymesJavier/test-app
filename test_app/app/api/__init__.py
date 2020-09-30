# -*- coding: utf-8 -*-
#########################################################
from flask import Blueprint

api = Blueprint('api', __name__)

from. import errors
from.example import example_endpoint
from.prueba import insertar_endpoint
from.prueba import eliminar_endpoint
from.prueba import actualizar_endpoint
from.prueba import consultar_endpoint
from.prueba import filtrar_endpoint

@api.before_request
def before_request():
    pass


@api.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers',
                         'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response

