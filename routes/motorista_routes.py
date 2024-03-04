from flask import Blueprint, render_template, request, redirect, url_for
from models import db, Motorista

motorista_routes = Blueprint('motoristas_routes', __name__)

@motorista_routes.route('/motorista')
def listar_motorista():
    motoristas = Motorista.query.all()
    return render_template('/motorista/listar_motorista.html', motoristas=motoristas)


# cadatrar motorista
@motorista_routes.route('/motorista/cadastrar', methods=['GET', 'POST'])
def cadastrar_motorista():
    if request.method == 'POST':
        cnh = request.form['cnh']
        if Motorista.query.filter_by(cnh=cnh).first() is not None:
            return 'CNH ja cadastrada'
        else:
            cod_motorista = request.form['cod_motorista']
            nome = request.form['nome']
            telefone = request.form['telefone']
            motorista = Motorista(cod_motorista=cod_motorista, nome=nome, telefone=telefone, cnh=cnh)
            db.session.add(motorista)
            db.session.commit()
            return redirect(url_for('motoristas_routes.listar_motorista'))

    return render_template('/motorista/cadastrar_motorista.html')


# editar motorista
@motorista_routes.route('/motorista/editar/<int:id>', methods=['GET', 'POST'])
def editar_motorista(id):
    motorista = Motorista.query.get(id)
    if request.method == 'POST':
        motorista.cod_motorista = request.form['cod_motorista']
        motorista.nome = request.form['nome']
        motorista.telefone = request.form['telefone']
        motorista.cnh = request.form['cnh']

        db.session.commit()
        return redirect(url_for('motoristas_routes.listar_motorista'))
    return render_template('/motorista/editar_motorista.html', motorista=motorista)


# deletar motorista

@motorista_routes.route('/motorista/deletar/<int:id>')
def deletar_motorista(id):
    motorista = Motorista.query.get_or_404(id)
    db.session.delete(motorista)
    db.session.commit()
    return redirect(url_for('motoristas_routes.listar_motorista'))
