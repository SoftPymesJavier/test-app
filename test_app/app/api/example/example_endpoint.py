# coding=utf-8
#########################################################
from flask import request, jsonify
from app.api import api
from app.controllers import ExampleController
from app.models import Example

@api.route('/example', methods=['GET'])
def example():
    message = ExampleController.get_example()
    return jsonify(data=message)

#nuevo example
@api.route('/example', methods=['POST'])
def create_example2():
	new_example = ExampleController.create_example()

	return jsonify(data=new_example)

# Listar los example 
@api.route('/examples', methods=['GET'])
def example_listed2():
	examples = ExampleController.example_listed()

	return jsonify(data=examples)

# Filtrar los examples por tiitulo
@api.route('/example/<title>', methods=['GET'])
def example_filtered2(title):
	result = ExampleController.example_filtered(title)
	
	return jsonify(data=result)

# actualizar example
@api.route('/example/<id>', methods=['PUT'])
def update_example2(id):
	example = ExampleController.update_example(id)

	return jsonify(data=example)


# eliminar example
@api.route('/example/<id>', methods=['DELETE'])
def delete_example2(id):
	example = ExampleController.delete_example(id)

	return jsonify(data=example)