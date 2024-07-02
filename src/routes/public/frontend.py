from flask import Blueprint, render_template
from utils.db import db

frontend_public = Blueprint("frontend_private", __name__)

@frontend_public.route('/home')
def home():
    links = [
        'https://hoteldiegodevelazquez.com/wp-content/uploads/2017/05/Andes-Suites-Departamentos-Amoblados-Providencia-Chile.png',
        'https://departamentosenchiclayo.com/wp-content/uploads/2017/10/departamento-amueblado-chiclayo-640x400.jpg',
        'https://i.postimg.cc/hPQb4mc4/cf760250-45df-412c-a7e8-8fb08c83ae7d.jpg'
    ]
    
    return render_template('public/home.html', links=links)
