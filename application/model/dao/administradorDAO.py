from flask import Flask
from application.model.entity.administrador import Administrador
from application import listaAdministradores

class AdministradorDAO:
    def __init__(self):
        pass

    def get_listaAdministradores(self):
        return self._listaAdministradores

    def procurar_id_autor(self):
        for i in range(0, len(self._listaAdministradores)):
            if self._listaAdministradores[i].get_id() == int(id):
                return self._listaAdministradores[i]
        return None

    def identificar_postagens_autor(self):
        for i in range(0,len(self._todas_postagens)):
            if self._todas_postagens[i].get_id_autor() == self.get_listaAdministradores[i].get_id():
                self._todas_postagens_autor.append(self._todas_postagens[i])
                return self._todas_postagens_autor
        return None