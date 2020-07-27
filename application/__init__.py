from flask import Flask, render_template
import os
from application.model.dao.usuarioDAO import UsuarioDAO
from application.model.dao.blog_dao import BlogDAO


app = Flask(
    __name__,
    static_folder=os.path.abspath("application/view/static"),
    template_folder=os.path.abspath("application/view/template"),
)

from application.controller import alteracaoSenha_controller
from application.controller import recuperacaoSenha_controller
from application.controller import login_controller
from application.controller import a_controller
from application.controller import blog_controller
from application.controller import feed_controller

usuario_dao = UsuarioDAO()
app.config["usuario_dao"] = usuario_dao
blog_dao = BlogDAO()
app.config["blog_dao"] = blog_dao