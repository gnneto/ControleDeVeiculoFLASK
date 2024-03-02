# veiculo_routes.py
from flask import Blueprint, render_template


veiculo_routes = Blueprint('veiculo_routes', __name__)

# Definir as rotas dentro do Blueprint
@veiculo_routes.route('/veiculo')
def listar_veiculo():
    return render_template('/veiculo/listar_veiculo.html')

@veiculo_routes.route('/veiculo/cadastrar')
def cadastrar_veiculo():
    return render_template('/veiculo/cadastrar_veiculo.html')

@veiculo_routes.route('/veiculo/editar/<int:id>')
def editar_veiculo(id):
    return f'Editar veículo com ID {id}'
