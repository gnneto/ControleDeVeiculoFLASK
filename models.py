from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# tabela veiculos
class Veiculo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    placa = db.Column(db.String(20), unique=True, nullable=False)
    marca = db.Column(db.String(100), nullable=False)
    modelo = db.Column(db.String(100), nullable=False)
    km_troca_oleo = db.Column(db.Integer)
    
    def __init__(self, placa, marca, modelo, km_troca_oleo):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.km_troca_oleo = km_troca_oleo


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



# tabela usuario

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=True)
    first_name = db.Column(db.String(100), nullable=True)
    last_name = db.Column(db.String(100), nullable=True)



from app import db
