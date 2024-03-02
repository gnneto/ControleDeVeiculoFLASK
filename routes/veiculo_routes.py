# veiculo_routes.py
from flask import Blueprint, render_template, request, redirect, url_for
from models import db, Veiculo


veiculo_routes = Blueprint('veiculo_routes', __name__)

# listar veiculos
@veiculo_routes.route('/veiculo')
def listar_veiculos():
    veiculos = Veiculo.query.all()
    return render_template('/veiculo/listar_veiculo.html', veiculos=veiculos)


# cadastrar veiculos
@veiculo_routes.route('/veiculo/cadastrar', methods=['GET', 'POST'])
def cadastrar_veiculo():
    if request.method == 'POST':
        placa = request.form['placa']
        if Veiculo.query.filter_by(placa=placa).first() is not None:
            return "Placa já cadastrada!"
        else:
            marca = request.form['marca']
            modelo = request.form['modelo']
            km_troca_oleo = request.form['km_troca_oleo']
            veiculo = Veiculo(placa=placa, marca=marca, modelo=modelo, km_troca_oleo=km_troca_oleo)
            db.session.add(veiculo)
            db.session.commit()
            return redirect(url_for('veiculo_routes.listar_veiculo'))
    return render_template('/veiculo/cadastrar_veiculo.html')


# editar veiculo
@veiculo_routes.route('/veiculo/editar/<int:id>')
def editar_veiculo(id):
    return f'Editar veículo com ID {id}'
