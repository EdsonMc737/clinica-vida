from flask import Blueprint, render_template

home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def index():
    return render_template('home/index.html')
    
@home_bp.route('/contato')
def contatos():
    return render_template('home/contato.html')

@home_bp.route('/sobre')
def info():
    return render_template('home/sobre.html')

@home_bp.route('/servico')
def servico():
    return render_template('home/servico.html')