from flask import Blueprint, render_template, redirect, url_for, request, session
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User


auth_bp = Blueprint('auth', __name__)


# login
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            session['username'] = user.username
            return redirect(url_for('controle_routes.listar_controle'))
        else:
            return 'Credenciais inválidas. <a href="/login">Tente novamente</a>.'
    return render_template('usuario/login.html')

# registro
@auth_bp.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        hashed_password = generate_password_hash(password)
        new_user = User(username=username, email=email, password=hashed_password, first_name=first_name, last_name=last_name)

        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('auth.login'))
    return render_template('usuario/registro.html')


@auth_bp.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('controle_routes.listar_controle'))