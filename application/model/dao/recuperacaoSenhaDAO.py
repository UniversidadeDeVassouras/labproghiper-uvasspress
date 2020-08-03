from flask import Flask
from application import app
from application.model.dao.autorDAO import AutorDAO
from application.model.entity.autor import Autor
from application.model.entity.recuperacaoSenha import RecuperacaoSenha
from application import recuperacaoList

class RecuperacaoSenhaDAO:
    def __init__(self):
        self._recuperacaoList = recuperacaoList
        self._listaAutores = self._listaAutores
    
    def buscar_por_token(self, token):
        for recuperacao in range(0, len(recuperacaoList)):
            if self._recuperacaoList[recuperacao].get_token() == token:
                return self._recuperacaoList[recuperacao]
        return None
    
    def apagar_solicitacao(self, email):
        for solicitacao in range(0, len(recuperacaoList)):
            if self._recuperacaoList[solicitacao].get_email() == email:
                self._recuperacaoList.pop(len(recuperacaoList)-1)
        return None
        
