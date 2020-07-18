from flask import Flask, render_template
import os
from application.model.dao.usuarioDAO import UsuarioDAO


app = Flask(__name__, static_folder=os.path.abspath('application/view/static'), template_folder=os.path.abspath('application/view/template'))

<<<<<<< HEAD
from application.controller import a_controller
from application.controller import login_controller

usuario_dao = UsuarioDAO()
app.config['usuario_dao'] = usuario_dao
=======


from application.controller import a_controller
from application.controller import recuperacaoSenha_controller
from application.controller import alteracaoSenha_controller
>>>>>>> req002
