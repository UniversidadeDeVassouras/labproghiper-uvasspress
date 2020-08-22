class Administrador:
    def __init__(self, nome, nome_usuario, email, senha, todas_postagens_autor):
        self._nome = nome
        self._nome_usuario = nome_usuario
        self._email = email
        self._senha = senha
        self._todas_postagens_autor = []

    def set_id(self, id):
        self._id = id
        
    def set_blog(self, blog):
        self._blog = blog

    def get_id(self):
        return self._id

    def get_nome(self):
        return self._nome

    def get_nome_usuario(self):
        return self._nome_usuario

    def get_email(self):
        return self._email

    def get_password(self):
        return self._senha

    def get_email(self):
        return self._email
    
    def set_todas_postagens_autor(self, postagem):
        self._todas_postagens_autor.append(postagem)

    def get_todas_postagens_autor(self):
        return self._todas_postagens_autor