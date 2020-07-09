from application.model.entity.autor import Autor
class UsuarioDAO:
    def __init__ (self):
        self._users  = [Autor(1, "igorbrownramos@gmail.com", "123456"),Autor(2, "vinicius@gmail.com", "123456") ]
         
    def cadastrar_usuario (self, email, senha, confirmar_senha):
        for autor in self._users:
            if autor.get_email() == email:
                return "Email Já Cadastrado"
        if senha == confirmar_senha:
            self._users.append(Autor(len(self._users), email, senha))
            return "Cadastro Efetuado"

    def logar_usuario(self, email, senha):
        for autor in self._users:
            if autor.get_email() != email and autor.get_password() != senha:
                return False
        return True