# coding=utf-8
#########################################################
from app.models import Example


class CrudController:

    @staticmethod
    def eliminar_example(id):
        example = Example.query.get(id) #encontrar el dato con el id indicado
        db.session.delete(example) #eliminar un dato por su id
        db.session.commit()
        #example.delete() se usa esta funcion?
        return 'datos eliminados'
    
    @staticmethod
    def actualizar_example(id,title,description):
        example= Example.query.get(id) #encontrar el dato con el id indicado
        example.title = title #asignar el titulo
        example.description = description #asignar la nueva descripcion
        db.session.commit()
        #example.update() #se usa esta funcion?
        return 'datos actualizados'

    @staticmethod
    def insertar_example(titulo,desc):
        example= Example(title=titulo,description=desc)
        db.session.add(example)
        db.session.commit()
        #example.save() se usa esta funcion?
        return 'datos insertados'

    @staticmethod
    def consultar_example():
        all_data= db.session.query(Example).all() #traer todos los datos
        #all_data = Example.query.all() 
        return all_data

    @staticmethod
    def filtrar_example(filtro):
        example=Example.query.filter_by(title=filtro).all()
        return example