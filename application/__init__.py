from flask import Flask, render_template
import os
from application.model.entity.post import Post
from application.model.entity.administrador import Administrador

todas_postagens = []
todas_postagens.append(Post(1, "Título do Post 1", "Conteúdo do post 1", "Descrição do post 1", "img/diretorioimagemdestaque", "data e hora criacao", "data e hora edicao", "ativo ou inativo", "Pedro Silva", 1))
todas_postagens.append(Post(2, "Título do Post 2", "Conteúdo do post 2", "Descrição do post 2", "img/diretorioimagemdestaque", "data e hora criacao", "data e hora edicao", "ativo ou inativo", "Tadeu Berardinelli", 2))

listaAdministradores = []
listaAdministradores.append(Administrador(1, "Pedro Silva", "PedroSilva", 12345, "pedro.q2000@outlook.com"))
listaAdministradores.append(Administrador(2, "Tadeu Berardinelli", "TadeuBerardinelli", 54321, "antoniotadeubf98@gmail.com"))
from application.model.dao.usuarioDAO import UsuarioDAO
from application.model.dao.post_DAO import PostDAO
from application.model.dao.administradorDAO import AdministradorDAO
from application.model.entity.administrador import Administrador	
from application.model.dao.blog_dao import BlogDAO
from application.model.entity.blog import Blog
from application.model.entity.recuperacaoSenha import RecuperacaoSenha
app = Flask(__name__, static_folder=os.path.abspath("application/view/static"), template_folder=os.path.abspath("application/view/template"))
usuario_dao = UsuarioDAO()
app.config["usuario_dao"] = usuario_dao	app.config["usuario_dao"] = usuario_dao
from application.controller import recuperacaoSenha_controller
from application.controller import login_controller
from application.controller import a_controller	
from application.controller import feed_controller


autor1 = Autor(1, "Pedro Silva", "PedroSilva", 12345, "pedro.q2000@outlook.com")	autor1 = Autor(1, "Pedro Silva", "PedroSilva", 12345, "pedro.q2000@outlook.com")
@@ -46,7 +51,7 @@
listaAutores.append(autor2)	listaAutores.append(autor2)
recuperacaoList.append(recuperacao1)	recuperacaoList.append(recuperacao1)


from application.controller import index_controller
from application.controller import recuperacaoSenha_controller
from application.controller import alteracaoSenha_controller

