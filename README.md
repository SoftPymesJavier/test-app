# TEST-PYTHON

### Instalación

> **Docker**
>
> **Docker Compose**
>
> **Docker Machine**
>
> **VirtualBox**

1. Crear Docker Machine

   ```
       - docker-machine create --driver virtualbox testapp
   ```

2. Generar Docker Compose

   ```
       - eval "$(docker-machine env testapp)"
       - make compile-local
   ```

3. Ejecutar

   ```
       - eval "$(docker-machine env testapp)"
       - make run-local
   ```
   
4. Ejemplo petición existente:

   ```
       - Para visualizar el HOST del Docker Machine ejecutar:
           - docker-machine ls 
           - Columna URL
       - GET -> http://HOTS_DOCKER_MACHINE:5000/api/v1/example
   ```    

### Prueba:

> **Hacer Fork**
>
> **Crear Pull Request**

1. Implementar endpoint que permita insertar un registro en la tabla _'example'_
2. Implementar endpoint que permita consultar todos los registros de la tabla _'example'_ de forma paginada.
3. Implementar endpoint que permita consultar filtrando por _'title'_ los registros de la tabla _'example'_ de forma paginada.
4. Implementar endpoint que permita actualizar un registro de la tabla _'example'_.
5. Implementar endpoint que permita eliminar un registro de la tabla _'example'_.
