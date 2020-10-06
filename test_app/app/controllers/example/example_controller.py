# coding=utf-8
#########################################################
from app.models import Example


class ExampleController():

    @staticmethod
    def get_example():
        return 'Hello from Flask'

    #nuevo example
    @staticmethod
    def create_example():
    	title = Example.title
    	description = Example.description
    	new_example = Example(title, description)
    	session.add(new_example)
    	session.commit()
    	return new_example

    # Listar los example 
    @staticmethod
    def example_listed():
    	examples = Example.objects.all()
    	return examples

    # Filtrar los examples por tiitul
    @staticmethod
    def example_filtered(title):
    	result = Example.objects.filter(title=title)
    	return result

    # actualizar example
    @staticmethod
    def update_example(exampleId):
    	example = Example.objects.get(exampleId=exampleId)
    	title = request.json['title']
    	description = request.json['description']
    	example.title = title
    	example.description = description
    	session.commit()
    	return example

    # eliminar un ecxample
    @staticmethod
    def delete_example(exampleId):
    	example = Example.objects.get(exampleId=exampleId)
    	session.delete(example)
    	session.commit()
    	return example