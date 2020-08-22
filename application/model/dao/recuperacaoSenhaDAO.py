from flask import Flask
from application import app
from datetime import date, datetime, timedelta
import smtplib
from application.model.dao.autorDAO import AutorDAO
from application.model.entity.autor import Autor
from application.model.entity.recuperacaoSenha import RecuperacaoSenha
from application import recuperacaoList
from application import listaAutores

class RecuperacaoSenhaDAO:
    def __init__(self):
        self._recuperacaoList = recuperacaoList
        self._listaAutores = listaAutores
    
    def buscar_por_token(self, token):
        for recuperacao in range(0, len(recuperacaoList)):
            if self._recuperacaoList[recuperacao].get_token() == token:
                return self._recuperacaoList[recuperacao]
        return None
    
    def buscar_por_email(self, email):
        for recuperacao in range(0, len(recuperacaoList)):
            if self._recuperacaoList[recuperacao].get_email() == email:
                return self._recuperacaoList[recuperacao]
        return None

    def apagar_solicitacao(self, email):
        for solicitacao in range(0, len(recuperacaoList)):
            if self._recuperacaoList[solicitacao].get_email() == email:
                self._recuperacaoList.pop(len(recuperacaoList)-1)
        return None
    
    def enviarEmail(self, email):
        for user in range(0, len(listaAutores)):
            if self._listaAutores[user].get_email() == email:
                if self._listaAutores[user].get_status() == "ativo":
                    data = date.today()
                    data_atual = f"{data.day}/{data.month}/{data.year}"
                    recuperacaoSenha = RecuperacaoSenha(len(recuperacaoList)+1, data_atual, user, email)
                    recuperacaoList.append(recuperacaoSenha)
                    msgFrom = email
                    smtpObj = smtplib.SMTP('smtp.outlook.com', 587)
                    smtpObj.ehlo()
                    smtpObj.starttls()
                    msgTo = 'sistemahipermidia@outlook.com'
                    toPass = 'hipermidia2019.1'
                    smtpObj.login(msgTo, toPass)
                    msg = '''
		            Foi solicitada a recuperação da senha da conta relacionada à este Email. Acesse o link abaixo para criação de nova senha. \n http://localhost:5000/alteracaosenha/{}'.format(recuperacaoSenha.get_token())
		            '''
                    smtpObj.sendmail(msgTo,msgFrom,'Subject: Solicitação de Recuperação de Senha\n{}'.format(msg))
                    smtpObj.quit()
        return None 
        
        
