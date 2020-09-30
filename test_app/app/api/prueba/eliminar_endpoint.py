# coding=utf-8
#########################################################
from flask import request, jsonify
from app.api import api
from app.controllers import CrudController


@api.route('/eliminar', methods=['GET'])
def eliminar():
    id=request.args.get('id')
    message = 'dato a eliminar con id: ' + id
    #datos= CrudController.eliminar_example(id)
    return jsonify(data=message)
