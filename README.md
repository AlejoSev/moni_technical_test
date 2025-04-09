# moni_technical_test

## Guia de uso!

```./deploy```

Levanta los contenedores donde se encuentran Django y Postgre. Además levanta el frontend de admin en el puerto 50000 y el frontend de client en el puerto 500001. (Dentro corre npm run dev, por lo que solo es apto para pruebas en development!)

Luego de levantar todo el proyecto, hay que crear el superuser de Django, mediante el cual se tendrá acceso al frontend de admin.

Se puede crear de la siguiente manera:

```docker-compose exec web python manage.py createsuperuserpython manage.py createsuperuse```

Eso sería, todo, a partir de ahora se puede ingresar al frontend de clientes (```http://127.0.0.1:500001```) para enviar nuevas solicitudes de prestamos. Y también ingresar al frontend de administradores (```http://127.0.0.1:500001/admin/login```) para poder gestionar los prestamos creados (ingresando con el usuario creado previamente)!