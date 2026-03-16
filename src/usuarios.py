from database.database import carregar_dados, salvar_dados

class Usuarios():

    def __init__(self):
        dados = carregar_dados()
        self.usuarios = dados["usuarios"]

    def salvar(self):
        dados = carregar_dados()
        dados["usuarios"] = self.usuarios
        salvar_dados(dados)

    def cadastrar_usuario(self, email, senha):

        novo_usuario = {
            "email": email,
            "senha": senha,
            "tipo": "usuario",
            "Emprestimos": []
        }

        self.usuarios.append(novo_usuario)
        self.salvar()

        print("Usuário cadastrado com sucesso!")

    def logar_usuario(self, email, senha):

        for usuario in self.usuarios:

            if usuario["email"] == email and usuario["senha"] == senha:
                print("Login realizado com sucesso")
                return usuario

        print("Usuário ou senha incorretos")
        return None


    def emprestar_livros(self, usuario, livro):

        if not livro["disponível"]:
            print("Livro já emprestado")
            return False

        livro["disponível"] = False
        usuario["Emprestimos"].append(livro)

        self.salvar()

        return True