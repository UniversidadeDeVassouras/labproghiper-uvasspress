from application import app
from flask import render_template, request
from application.model.dao.usuarioDAO import UsuarioDAO
import os

@app.route('/login')
def login_user():
    user_dao = UsuarioDAO
    user_test = user_dao.list_users()
    return render_template('login.html', user_test = user_test)