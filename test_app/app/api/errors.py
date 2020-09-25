# -*- coding: utf-8 -*-
#########################################################
from flask import jsonify

from app.api import api
from app.exceptions import (InternalServerError, BadRequest, NotFound)


@api.errorhandler(InternalServerError)
def internal_server_error(e):
    response = jsonify(
        {
            'status': 500,
            'error': 'internal server error',
            'message': str(e.args[0])
        }
    )
    response.status_code = 500
    return response


@api.errorhandler(BadRequest)
def bad_request(e):
    response = jsonify(
        {
            'status': 400,
            'error': 'bad request',
            'message': str(e.args[0])
        }
    )
    response.status_code = 400
    return response


@api.errorhandler(NotFound)
def not_found(e):
    response = jsonify(
        {
            'status': 404,
            'error': 'not found',
            'message': str(e.args[0])
        }
    )
    response.status_code = 404
    return response
