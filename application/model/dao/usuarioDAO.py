from application import app
from application.model.entity.autor import Autor

class UsuarioDAO:
    def __init__ (self):
        self._users = []
        self._users.append(Autor(1, "igorbrownramos@gmail.com", "123456"))
        self._users.append(Autor(2, "vinicius@gmail.com", "123456"))
        
    def cadastrar_usuario (self, email, senha):
        for autor in self._users:
            if autor.get_email() == email:
                return "Email Já Cadastrado"
        if senha == senha:
            self._users.append(Autor(len(self._users), email, senha))
            return "Cadastro Efetuado"
        