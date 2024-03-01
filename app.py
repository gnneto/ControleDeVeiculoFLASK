from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ctrlVeic.sqlite3'

db = SQLAlchemy(app)

# tabela veiculos
class Veiculo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    placa = db.Column(db.String(20), unique=True, nullable=False)
    marca = db.Column(db.String(100), nullable=False)
    modelo = db.Column(db.String(100), nullable=False)
    km_troca_oleo = db.Column(db.Integer)

# tabela motorista
class Motorista(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cod_motorista = db.Column(db.String(20), unique=True, nullable=False)
    nome = db.Column(db.String(100), nullable=False)
    telefone = db.Column(db.String(20), nullable=False)
    cnh = db.Column(db.String(20), nullable=False)


# tabela controle
class Controle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    veiculo_id = db.Column(db.Integer, db.ForeignKey('veiculo.id'), nullable=False)
    motorista_id = db.Column(db.Integer, db.ForeignKey('motorista.id'), nullable=False)
    data_saida = db.Column(db.Date, nullable=False)
    hora_saida = db.Column(db.Time, nullable=False)
    km_saida = db.Column(db.Integer, nullable=False)
    destino = db.Column(db.String(100), nullable=False)
    data_retorno = db.Column(db.Date)
    hora_retorno = db.Column(db.Time)
    km_retorno = db.Column(db.Integer)
    km_percorrido = db.Column(db.Integer)

    # relacao
    veiculo = db.relationship('Veiculo', backref=db.backref('controles', lazy=True))
    motorista = db.relationship('Motorista', backref=db.backref('controles', lazy=True))

# pagina principal
@app.route('/')
def index():
    return render_template('index.html')


# ROTAS MOTORISTA


@app.route('/motoristas')
def listar_motoristas():
    return render_template('/motorista/listar_motorista.html')


# cadatrar motorista
@app.route('/motorista/cadastrar')
def cadastrar_motoristas():
    return render_template('/motorista/cadastrar_motorista.html')


# editar motorista
@app.route('/motorista/editar')
def editar_motoristas():
    return render_template('/motorista/editar_motorista.html')
    

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
