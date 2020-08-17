from application import app
from flask import render_template, request
import os
from application import recuperacaoList
from application import listaAutores
from application.model.entity.recuperacaoSenha import RecuperacaoSenha
from application.model.dao.recuperacaoSenhaDAO import RecuperacaoSenhaDAO
from application.model.entity.autor import Autor
from application.model.dao.autorDAO import AutorDAO


@app.route("/alteracaosenha/<recuperacaoSenha_token>", methods=['GET'])
def alteracaosenha():
   recuperacaoSenha_dao = RecuperacaoSenhaDAO()
   autor_dao = AutorDAO()
   recuperacaoSenha = recuperacaoSenha_dao.buscar_por_token(recuperacaoSenha_token)
   if datetime.now() > RecuperacaoSenha().get_data_solicitacao():
      return render_template("expirado.html")
   else:
      return render_template('alteracaoSenha.html', recuperacaoSenha = recuperacaoSenha)


@app.route("/alteracaosenha/<recuperacaoSenha_token>/alterarsenha", methods=['POST'])
def alterarSenha():
   recuperacaoSenha_dao = RecuperacaoSenhaDAO()
   autor_dao = AutorDAO()
   recuperacaoSenha = recuperacaoSenha_dao.buscar_por_token(recuperacaoSenha_token)
   nova_senha = request.values.get('nova_senha')
   repita_novaSenha = request.values.get('repita_novaSenha')
   autor = recuperacaoSenha.get_autor()
   if nova_senha == repita_novaSenha:
      autor.set_senha(nova_senha)
      return render_template('senhaalterada.html', recuperacaoSenha = recuperacaoSenha, autor = autor), 201
   else:
      return render_template('senhasdiferentes.html', recuperacaoSenha = recuperacaoSenha, autor = autor)
