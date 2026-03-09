#classe dos usuarios
class Usuarios():
    # inicializa a classe
    def __init__(self):
        # lista com os dicionarios, usuarios padrao (o adm)
        self.usuarios = [
            {
                "email": "admin",
                "senha": "administracao123",
                "tipo": "admin",
                "Emprestimos": []
            }
        ]

    # funcao do cadastro do caba
    def cadastrar_usuario(self, email, senha):

        # cria um novo usuario com estrutura padrao
        novo_usuario = {
            "email": email,
            "senha": senha,
            "tipo": "usuario",
            "Emprestimos": []
        }

        # adiciona o usuario na lista de usuarios
        self.usuarios.append(novo_usuario)

        print("\nUsuário cadastrado com sucesso!")

        return True

    # funcao do login do caba
    def logar_usuario(self, email, senha):

        # percorre todos os usuarios da lista
        for usuario in self.usuarios:

            # compara o email e a senha
            if usuario["email"] == email and usuario["senha"] == senha:
                print(f"Logado com sucesso, seja bem vindo!")
                return usuario

        print("\nUsuário ou senha incorretos!")
        return None
    
    #funcao de emprestar o livro
    def emprestar_livros(self, usuario, livro):
        if livro["disponível"] == False:
            print("\nEste livro já está emprestado!")
            return False

        livro["disponível"] = False
        usuario["Emprestimos"].append(livro)

        print("Livro emprestado com sucesso!")
        return True

    def devolver_livros(self, usuario):
        if usuario["Emprestimos"]:
            for i, livro in enumerate(usuario["Emprestimos"]):
                print(f"{i + 1} - {livro["titulo"]}")

            print("\nEscolha o número do livro que deseja devolver: ")
            numero = int(input())

            livro = usuario["Emprestimos"][numero - 1]

            livro["disponível"] = True
            usuario["Emprestimos"].remove(livro)
        else:
            print("\nNenhum livro emprestado")

    def ver_emprestimos(self, usuario):
        if usuario["Emprestimos"]:
            for i, livro in enumerate(usuario["Emprestimos"]):
                print(f"{i + 1} - {livro["titulo"]}")
        else:
            print("\nVocê não possui nenhum empréstimo pendente")