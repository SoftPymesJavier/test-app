# coding=utf-8
#########################################################
from app.models import Example
from app import db


class CrudController:

    @staticmethod
    def eliminar_example(id):
        example = Example.query.get(id) #encontrar el dato con el id indicado
        example.delete() 
        return example.export_data()
    
    @staticmethod
    def actualizar_example(id,title,description):
        example= Example.query.get(id) #encontrar el dato con el id indicado
        example.title = title #asignar el titulo
        example.description = description #asignar la nueva descripcion
        example.save() 
        return example.export_data()

    @staticmethod
    def insertar_example(titulo,desc):
        example= Example(title=titulo,description=desc)
        #db.session.add(example)
        #db.session.commit()
        example.save()
        return example.export_data()

    @staticmethod
    def consultar_example():
        examples = db.session.query(Example).all() #traer todos los datos
        response=[example.export_data() for example in examples]
        #all_data = Example.query.all() 
        return response

    @staticmethod
    def filtrar_example(filtro):
        examples=Example.query.filter_by(title=filtro).all()
        response=[example.export_data() for example in examples]
        return response