from flask import Flask
from uuid import uuid4

class RecuperacaoSenha:
    def __init__(self, id, dataSolicitacao, autor):
        self._id = id
        self._dataSolicitacao = dataSolicitacao
        self._autor = autor
        self._token = uuid4()
    
    def get_id(self):
        return self._id
    
    def get_autor(self):
        return self._autor
    


