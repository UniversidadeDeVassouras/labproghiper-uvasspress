from application import app
from application.model.entity.autor import Autor

class UsuarioDAO:
    def __init__ (self):
        self._users = []
        self._users.append (Autor(1, "Igor Brown Ramos", "igorbrownramos@gmail.com", "123456"))
        self._users.append (Autor(2, "Vinicius Almeida", "vinicius@gmail.com", "123456"))
        

    
    def list_users (self):
        return self._users