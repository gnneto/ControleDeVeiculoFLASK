# app.py
from flask import Flask
from models import db
from routes.veiculo_routes import veiculo_routes
from routes.motorista_routes import motorista_routes
from routes.controle_routes import controle_routes

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ctrlVeic.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)


from models import Veiculo, Motorista, Controle

# rotas
app.register_blueprint(veiculo_routes)
app.register_blueprint(motorista_routes)
app.register_blueprint(controle_routes)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
