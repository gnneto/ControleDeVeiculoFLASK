from flask import Blueprint, render_template

motorista_routes = Blueprint('motoristas_routes', __name__)

@motorista_routes.route('/motorista')
def listar_motorista():
    return render_template('/motorista/listar_motorista.html')


# cadatrar motorista
@motorista_routes.route('/motorista/cadastrar')
def cadastrar_motorista():
    return render_template('/motorista/cadastrar_motorista.html')


# editar motorista
@motorista_routes.route('/motorista/editar')
def editar_motorista():
    return render_template('/motorista/editar_motorista.html')