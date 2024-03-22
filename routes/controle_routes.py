from flask import Blueprint, render_template, request, redirect, url_for, session
from models import db, Controle, Veiculo, Motorista
from datetime import datetime, time

controle_routes = Blueprint('controle_routes', __name__)

@controle_routes.route('/')
def listar_controle():
    # Verificar se o usuário está logado
    if 'username' not in session:
        # Se o usuário não estiver logado, redirecioná-lo para a página de login
        return redirect(url_for('auth.login'))

    # Se o usuário estiver logado, continuar com a lógica para listar os controles
    controles = Controle.query.all()
    return render_template('/controle/tela_principal.html', controles=controles)


# cadatrar controle
@controle_routes.route('/controle/cadastrar', methods=['GET', 'POST'])
def cadastrar_controle():
    if request.method == 'POST':
        veiculo_id = request.form['veiculo']
        motorista_id = request.form['motorista']
        data_saida = datetime.strptime(request.form['data_saida'], '%Y-%m-%d').date()
        hora_saida = datetime.strptime(request.form['hora_saida'], '%H:%M').time()
        km_saida = request.form['km_saida']
        destino = request.form['destino']
        data_retorno = datetime.strptime(request.form['data_retorno'], '%Y-%m-%d').date()
        hora_retorno = datetime.strptime(request.form['hora_retorno'], '%H:%M').time()
        km_retorno = request.form['km_retorno']
        km_percorrido = request.form['km_percorrido']

        veiculo = Veiculo.query.get(veiculo_id)
        motorista = Motorista.query.get(motorista_id)
        
        controle = Controle(
            veiculo = veiculo,
            motorista = motorista,
            data_saida = data_saida,
            hora_saida = hora_saida,
            km_saida = km_saida,
            destino = destino,
            data_retorno = data_retorno,
            hora_retorno = hora_retorno,
            km_retorno = km_retorno,
            km_percorrido = km_percorrido
        )

        db.session.add(controle)
        db.session.commit()
        return redirect(url_for('controle_routes.listar_controle'))

    veiculos = Veiculo.query.all()
    motoristas = Motorista.query.all()
    return render_template('/controle/cadastrar_controle.html', veiculos=veiculos, motoristas=motoristas)


# editar controle
@controle_routes.route('/controle/editar/<int:id>', methods=['GET', 'POST'])
def editar_controle(id):
    controle = Controle.query.get_or_404(id)
    if request.method == 'POST':
        controle.veiculo_id = request.form['veiculo']
        controle.motorista_id = request.form['motorista']
        controle.data_saida = datetime.strptime(request.form['data_saida'], '%Y-%m-%d').date()
        controle.hora_saida = time.fromisoformat(request.form['hora_saida'])
        controle.km_saida = request.form['km_saida']
        controle.destino = request.form['destino']
        controle.data_retorno = datetime.strptime(request.form['data_retorno'], '%Y-%m-%d').date()
        controle.hora_retorno = time.fromisoformat(request.form['hora_retorno'])
        controle.km_retorno = request.form['km_retorno']
        controle.km_percorrido = request.form['km_percorrido']
        db.session.commit()

        return redirect(url_for('controle_routes.listar_controle'))
    veiculos = Veiculo.query.all()
    motoristas = Motorista.query.all()

    return render_template('/controle/editar_controle.html', controle=controle, veiculos=veiculos, motoristas=motoristas)



# detelar cadastro controle

@controle_routes.route('/controle/deletar/<int:id>')
def deletar_controle(id):
    controle = Controle.query.get_or_404(id)
    db.session.delete(controle)
    db.session.commit()
    return redirect(url_for('controle_routes.listar_controle'))



# visualizar controle

@controle_routes.route('/controle/detalhes/<int:id>')
def visualizar_controle(id):
    controle = Controle.query.get_or_404(id)
    return render_template('controle/visualizar_controle.html', controles=controle)
