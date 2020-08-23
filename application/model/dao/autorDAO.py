from flask import Flask
from application.model.entity.autor import Autor
from application import listaAutores

class AutorDAO:
    def __init__(self):
        self._listaAutores = listaAutores

    def get_listaAutores(self):
        return self._listaAutores
    
    def buscar_por_id(self, id):
        for autor in range(0, len(self._listaAutores)):
            if self._listaAutores[autor].get_id() == int(id):
                return self._listaAutores[autor]
        return None
    
    def buscar_por_email(self, email):
        for autor in range(0, len(self._listaAutores)):
            if self._listaAutores[autor].get_email() == email:
                return self._listaAutores[autor]
        return None
    
    def inativarAutor(self, autor):
        autor.set_status("inativo")
    
    def ativarAutor(self, autor):
        autor.set_status("ativo")

    
    




    