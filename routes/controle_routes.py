from flask import Blueprint, render_template

controle_routes = Blueprint('controle_routes', __name__)

@controle_routes.route('/controle')
def listar_controle():
    return render_template('/controle/tela_principal.html')


# cadatrar controle
@controle_routes.route('/controle/cadastrar')
def cadastrar_controle():
    return render_template('/controle/cadastrar_controle.html')


# editar controle
@controle_routes.route('/controle/editar')
def editar_controle():
    return render_template('/controle/editar_controle.html')