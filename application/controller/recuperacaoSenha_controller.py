from flask import Flask, render_template, request
from application import app
import os
from application import recuperacaoList
from application import listaAutores
from application.model.entity.autor import Autor
from application.model.entity.recuperacaoSenha import RecuperacaoSenha
from application.model.dao.autorDAO import AutorDAO
from application.model.dao.recuperacaoSenhaDAO import RecuperacaoSenhaDAO
from datetime import datetime, timedelta

@app.route("/recuperacaosenha", methods=['GET'])
def recuperacaoSenha():
   autor_dao = AutorDAO()
   recuperacaoSenha_dao = RecuperacaoSenhaDAO()
   return render_template('recuperacaoSenha.html')

@app.route("/recuperacaosenha/linkenviado", methods=['POST'])
def enviarlink():
   autor_dao = AutorDAO()
   recuperacaoSenha_dao = RecuperacaoSenhaDAO()
   email = request.values.get('email')
   recuperacao_senha = recuperacaoSenha_dao.buscar_por_email(email)
   recuperacao_senha.enviarEmail(email)
   tempo_solicitacao = datetime.now() + timedelta(hours=24)
   recuperacao_senha.set_solicitacao(tempo_solicitacao) 
   return render_template('linkenviado.html', recuperacao_senha = recuperacao_senha), 201

