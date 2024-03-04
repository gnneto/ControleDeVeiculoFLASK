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
            return redirect(url_for('veiculo_routes.listar_veiculos'))
    return render_template('/veiculo/cadastrar_veiculo.html')


# editar veiculo
@veiculo_routes.route('/veiculo/editar/<int:id>', methods=['GET', 'POST'])
def editar_veiculo(id):
    veiculo = Veiculo.query.get(id)
    if request.method == 'POST':
        veiculo.placa = request.form['placa']
        veiculo.marca = request.form['marca']
        veiculo.modelo = request.form['modelo']
        veiculo.km_troca_oleo = request.form['km_troca_oleo']
        # veiculo = Veiculo(placa=placa, marca=marca, modelo=modelo, km_troca_oleo=km_troca_oleo)
        db.session.commit()
        return redirect(url_for('veiculo_routes.listar_veiculos'))
    return render_template('/veiculo/editar_veiculo.html', veiculo=veiculo)



# deletar veiculo

@veiculo_routes.route('/veiculo/deletar/<int:id>')
def deletar_veiculo(id):
    veiculo = Veiculo.query.get_or_404(id)
    db.session.delete(veiculo)
    db.session.commit()
    return redirect(url_for('veiculo_routes.listar_veiculos'))