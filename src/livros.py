from database.database import carregar_dados, salvar_dados

class Livros():

    def __init__(self):
        dados = carregar_dados()
        self.livros = dados["livros"]

    def salvar(self):
        dados = carregar_dados()
        dados["livros"] = self.livros
        salvar_dados(dados)

    def adicionar_livro(self, livro):

        novo = {
            "titulo": livro,
            "disponível": True
        }

        self.livros.append(novo)
        self.salvar()

        print(f"Livro {livro} adicionado com sucesso!")

    def remover_livro(self, livro):

        self.livros.remove(livro)
        self.salvar()

        print(f"Livro {livro['titulo']} removido")