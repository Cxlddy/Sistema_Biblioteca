#classe dos livros
class Livros():
    #inicializa a classe
    def __init__(self):
        self.livros = [
            {
                "titulo" : "1984", 
                "disponível" : True
            },
            
            {
               "titulo" : "Dom Quixote",
               "disponível" : True 
            },

            {
                "titulo" : "A Megera Domada",
                "disponível" : True
            },

            {
                "titulo" : "A revolução dos bichos",
                "disponível" : True
            }


        ]

    #adiciona livros
    def adicionar_livro(self, livro):
        self.livros.append({
            "titulo" : livro,
            "disponível" : True
        })
        print(f"Livro {livro} adicionado com sucesso!")
    
    def listar_livros(self):
        #mostra os livros
        if not self.livros:
            print("Nenhum livro cadastrado")
        elif self.livros:
            print("~~~ Livros Cadastrados: ~~~")
            for i, livro in enumerate(self.livros):
                #mostra se o livro esta emprestado ou não
                if livro["disponível"]:
                    status = "Disponível"
                else:
                    status = "Indisponível"
                print(i + 1, "-", "Título", livro["titulo"], f'({status})')

    #remove os livros
    def remover_livro(self, livro):
        if livro in self.livros:
            self.livros.remove(livro)
            print(f'Livro {livro} removido')
        elif livro not in self.livros:
            print(f'{livro} não foi encontrado no sistema')
        

