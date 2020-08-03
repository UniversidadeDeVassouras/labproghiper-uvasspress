from flask import Flask
from uuid import uuid4
from application import recuperacaoList


class RecuperacaoSenha:
    def __init__(self, id, dataSolicitacao, autor, email):
        self._id = id
        self._dataSolicitacao = dataSolicitacao
        self._autor = autor
        self._email = email
        self._token = uuid4()
        
    
    def get_id(self):
        return self._id
    
    def get_autor(self):
        return self._autor
    
    def get_email(self):
        return self._email

    def get_token(self):
        return self._token
    


