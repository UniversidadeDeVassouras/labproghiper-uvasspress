from flask import Flask
import smtplib
from application.model.dao.autorDAO import AutorDAO
from application.model.entity.recuperacaoSenha import RecuperacaoSenha

class RecuperacaoSenhaDAO:
    def __init__(self):
        self._recuperacaoList = []
        self._listaAutores = self._listaAutores

    def solicitarRecuperacao(self, id, dataSolicitacao, autor, email):
        for user in self._listaAutores:
            if user.get_email() == email:
                for recuperacao in self._recuperacaoList:
                    if recuperacao.get_autor() == autor:
                        self._recuperacaoList.pop(recuperacao.get_id()-1)
                self._recuperacaoList.append(RecuperacaoSenha(len(self._recuperacaoList), dataSolicitacao, autor))
                smtpObj = smtplib.SMTP('smtp.gmail.com', 465)
                smtpObj.ehlo()
		        smtpObj.starttls()
                msgFrom = "Email do Sistema(Remetente)"
                toPass = "Senha do Email"
                smtpObj.login(msgFrom, toPass)
                msg = '''
		        Foi solicitada a recuperação da senha da conta relacionada à este Email. Acesse o link abaixo para criação de nova senha. \n link da página
		        '''
                smtpObj.sendmail(msgFrom,email,'Subject: Solicitação de Recuperação de Senha\n{}'.format(msg))
                smtpObj.quit()
                return "Foi enviado o link de recuperação de senha para o Email informado."

            else:
                return "Nenhuma conta registrada com esse Email."
                    

        
        
