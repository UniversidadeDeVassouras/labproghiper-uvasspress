from application.model.entity.autor import Autor
class UsuarioDAO:
    def __init__ (self):
        self._users  = []
         
    def cadastrar_usuario (self, nome, nome_usuario, email, senha, confirmar_senha):
        for autor in self._users:
            if autor.get_nome_usuario() == nome_usuario:
                return "Nome de usuário em uso"

            if autor.get_email() == email:
                return "Email Já Cadastrado"

        if senha == confirmar_senha:
            autor = Autor(nome, nome_usuario, email, senha)
            self._users.append(autor)
            autor.set_id(len(self._users))
            return "Cadastro Efetuado"

    def logar_usuario(self, email, senha):
        for autor in self._users:
            if autor.get_email() == email and autor.get_password() == senha:
                return False
        return True

    def exibir(self):
        return self._users