# Flask Boilerplate for Profesional Development

[![Abrir en gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/from-referrer/)
<p align="center">
    <a href="https://youtu.be/ORxQ-K3BzQA"><img height="200px" src="https://github.com/4GeeksAcademy/flask-rest-hello/blob/main/docs/assets/how-to.png?raw=true?raw=true" /></a>
</p>

## Características

- Amplia documentación [aquí](https://start.4geeksacademy.com).
- Integrado con Pipenv para la gestión de paquetes.
- Despliegue rápido a heroku con `$ pipenv run deployment`.
- Uso del archivo `.env`.
- Integración de SQLAlchemy para la abstracción de la base de datos.

## Instalación (automática si está usando gitpod)

> Importante: El boiplerplate está hecho para python 3.7 pero puedes cambiar fácilmente `python_version` en el Pipfile.

Los siguientes pasos se ejecutan automáticamente con gitpod, si está realizando una instalación local, debe hacerlo manualmente:

```sh
pipenv install;
mysql -u root -e "CREATE DATABASE example";
pipenv run init;
pipenv run migrate;
pipenv run upgrade;
```

## ¿Cómo empezar a codificar?

Hay una API de ejemplo que funciona con una base de datos de ejemplo. Todo el código de su aplicación debe estar escrito dentro de la carpeta `./src/`.

- src/main.py (es donde se deben codificar sus puntos finales)
- src/models.py (las tablas de su base de datos y la lógica de serialización)
- src/utils.py (algunas clases y funciones reutilizables)
- src/admin.py (agregue sus modelos al administrador y administre sus datos fácilmente)

Para una explicación más detallada, busque el tutorial dentro de la carpeta `docs`.

## Recuerda migrar cada vez que cambies tus modelos

Debe migrar y actualizar las migraciones para cada actualización que realice en sus modelos:
```
$ pipenv run migrate (para hacer las migraciones)
$ pipenv run upgrade (para actualizar su base de datos con las migraciones)
```


# Instalación manual para Ubuntu y Mac

⚠️ Asegúrese de tener `python 3.6+` y `MySQL` instalados en su computadora y que MySQL se esté ejecutando, luego ejecute los siguientes comandos:
```sh
$ pipenv install (para instalar paquetes pip)
$ pipenv run migrate (para crear la base de datos)
$ pipenv run start (para iniciar el servidor web del matraz)
```


## Implementar en Heroku

Esta plantilla es 100% compatible con Heroku[https://www.heroku.com/], solo asegúrese de comprender y ejecutar los siguientes pasos:

```sh
// Instalar heroku
$ npm i heroku -g
// Inicie sesión en heroku en la línea de comando
$ heroku login -i
// Crea una aplicación (si aún no la tienes)
$ heroku create <nombre_de_tu_aplicación>
// commit and push to heroku (confirmar sus cambios)
$ git push heroku main
```
:advertencia: para obtener una explicación más detallada sobre cómo trabajar con variables .env o la base de datos MySQL [lea la guía completa](https://start.4geeksacademy.com/backend/deploy-heroku-mysql).