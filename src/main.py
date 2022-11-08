"""
Este módulo se encarga de iniciar el servidor API, cargar la base de datos y agregar los puntos finales
"""
import os
from werkzeug.security import check_password_hash as checkph
from werkzeug.security import generate_password_hash as genph
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, Users
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:manu@localhost/db_app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Manejar/serializar errores como un objeto JSON
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# Generar un mapa del sitio con todos sus puntos finales
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/users', methods=['GET'])
def handle_hello():
    all_users = Users.query.all()
    data = list(map(lambda x: x.serialize(), all_users))
    response_body = {
        "msg": "Hello, this is your GET /people response "
    }
    if len(data) > 0:
        return jsonify(data), 200
    else:
        return jsonify(response_body)

@app.route('/users', methods=['POST'])
def add_user():
    body = request.get_json()
    print(body)

    if body == None:
        return jsonify({'¡Error! Invalid data'}), 400
    elif 'username' not in body:
        return jsonify({'message': 'you must add a username'}), 400
    elif 'name' not in body:
        return jsonify({'message': 'you must add a name'}), 400
    elif 'email' not in body:
        return jsonify({'message': 'you must add a email'}), 400
    elif 'password' not in body:
        return jsonify({'message': 'you must add a password'}), 400
    else:
        hash_pass = genph(body['password'])
        user = Users(username=body['username'], name=body['name'], email=body['email'], password=hash_pass)
        db.session.add(user)
        db.session.commit()
        return jsonify({'success': 'add user'}), 200

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    user = Users.query.filter_by(username=username, password=password).first()
    print(user)
    return jsonify({'user': 'success'}), 200

@app.route('/user/get/<int:id>', methods=['GET'])
def people_for_id(id):
    users = Users.query.all()
    data = list(map(lambda x: x.serialize(), users))
    for person in data:
       if person['id'] == id:
        return jsonify(person)

# Esto solo se ejecuta si se ejecuta `$ python src/main.py como modulo principal`
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3001))
    app.run(host='0.0.0.0', port=PORT, debug=True)
