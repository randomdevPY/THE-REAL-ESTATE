from flask import Blueprint, render_template, request
from utils.db import db

backend_private = Blueprint("backend_private", __name__)

@backend_private.route('/login', methods=['GET', 'POST'])
def login_page():
    if request.method == 'GET':
        url_image = 'https://media.admagazine.com/photos/618a6acacc7069ed5077ca7c/3:2/w_2250,h_1500,c_limit/69052.jpg'
        return render_template('private/login.html', background=url_image)
    elif request.method == 'POST':
        # Acciones a realizar en caso de una petición POST
        return 'POST REQUEST'
''
@backend_private .route('/panel')
def home_page():
    return render_template('private/panel.html')