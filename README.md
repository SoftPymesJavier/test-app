# TEST-PYTHON

### Instalación

> **Docker**
>
> **Docker Compose**
>
> **Docker Machine**

1. Crear Docker Machine
    ```
        - docker-machine create --driver virtualbox testapp
    ```

1. Generar Docker Compose
   ```
       - eval "$(docker-machine env testapp)"
       - make compile-local
   ```

1. Ejecutar
   ```
       - eval "$(docker-machine env testapp)"
       - make run-local
   ```

### Requerimientos:
