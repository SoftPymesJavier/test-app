# coding=utf-8
#########################################################
from flask import request, jsonify
from app.api import api
from app.controllers import CrudController


@api.route('/eliminar', methods=['GET'])
def eliminar():
    Exampleid=request.args.get('id')
    message= CrudController.eliminar_example(Exampleid)
    return jsonify(data=message)
