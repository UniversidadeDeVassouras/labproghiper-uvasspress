from flask import Flask
from application.model.entity.autor import Autor

class AutorDAO:
    def __init__(self):
        self._listaAutores = [Autor(1, "Pedro Silva", "PedroSilva", 12345, "pedro.q2000@outlook.com"),Autor(2, "Tadeu Berardinelli", "TadeuBerardinelli", 54321, "antoniotadeubf98@gmail.com")]

    def get_listaAutores(self):
        return self._listaAutores

    