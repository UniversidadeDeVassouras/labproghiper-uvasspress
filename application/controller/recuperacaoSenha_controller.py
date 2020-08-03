from application import app
from application import recuperacaoList
from application import listaAutores
from application.model.entity.autor import Autor
from application.model.entity.recuperacaoSenha import RecuperacaoSenha
from application.model.dao.autorDAO import AutorDAO
from application.model.dao.recuperacaoSenhaDAO import RecuperacaoSenhaDAO
from flask import render_template, request
import os
import smtplib
from datetime import date

@app.route("/recuperacaosenha", methods=['GET'])
def recuperacaoSenha():
   return render_template('recuperacaoSenha.html')

@app.route("/recuperacaosenha/enviarlink", methods=['POST'])
def enviarLink():
   autor_dao = AutorDAO()
   recuperacaoSenha_dao = RecuperacaoSenhaDAO()
   data = date.today()
   data_atual = f"{data_atual.day}/{data_atual.month}/{data_atual.year}"
   email = request.values.get('email')
   recuperacaoSenha_dao.apagar_solicitacao(email)
   for user in self._listaAutores:
            if user.get_email() == email:
                if user.get_status() == "ativo":
                   recuperacaoSenha = RecuperacaoSenha(len(recuperacaoList)+1, data_atual, user, email)
                   recuperacaoList.append(recuperacaoSenha)
                   smtpObj = smtplib.SMTP('smtp.gmail.com', 465)
                   smtpObj.ehlo()
                   smtpObj.starttls()
                   msgFrom = "Email do Sistema(Remetente)"
                   toPass = "Senha do Email"
                   smtpObj.login(msgFrom, toPass)
                   msg = '''
                   Foi solicitada a recuperação da senha da conta relacionada à este Email. Acesse o link abaixo para criação de nova senha. \n http://localhost:5000/alteracaosenha/{}
                   ''' format(recuperacaoSenha.get_token())
                   smtpObj.sendmail(msgFrom,email,'Subject: Solicitação de Recuperação de Senha\n{}'.format(msg))
                   smtpObj.quit()
   return None