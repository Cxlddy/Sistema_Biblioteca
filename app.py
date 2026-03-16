import customtkinter as ctk
from src.usuarios import Usuarios
from src.livros import Livros


biblioteca = Livros() #chama as classes
usuarios = Usuarios() #''

#para manipulação ideal do usuário atual, definimos como None antes para a variável existir
usuario_atual = None

ctk.set_appearance_mode("Dark") #aparência padrão de todas as páginas
ctk.set_default_color_theme("dark-blue") #mesma coisa


# menu do adm

def menu_adm():

    def abrir_add(): #funcao para abrir a página de adicionar livros
        pagina_adicionar_livro()

    def abrir_lista(): #mesma coisa, mas para a de lista
        pagina_listar_livros()
    
    #a partir de agora é apenas as coisas da página, que são itens totalmente genéricos do customTKinter
    janela = ctk.CTk()
    janela.geometry("600x400")
    janela.title("Menu Administração")

    janela.grid_columnconfigure(0, weight=1)

    titulo = ctk.CTkLabel(janela, text="Seja bem vindo, administrador!", font=("Roboto", 28))
    titulo.grid(row=0, column=0, pady=20)

    botao1 = ctk.CTkButton(janela, text="Adicionar Livro", command=abrir_add)
    botao1.grid(row=1, column=0, pady=10)

    botao2 = ctk.CTkButton(janela, text="Listar Livros", command=abrir_lista)
    botao2.grid(row=2, column=0, pady=10)

    botao3 = ctk.CTkButton(janela, text="Remover Livro", command=pagina_remover_livro) #aqui houve uma quebra de padrão, será corrigido depois
    botao3.grid(row=3, column=0, pady=10)

    janela.mainloop()


# menu do usuario

def menu_usuario():

    janela = ctk.CTk()
    janela.geometry("600x400")
    janela.title("Menu Usuário")

    janela.grid_columnconfigure(0, weight=1)

    titulo = ctk.CTkLabel(janela, text="Menu do Usuário", font=("Roboto", 28))
    titulo.grid(row=0, column=0, pady=20)

    botao1 = ctk.CTkButton(janela, text="Listar Livros", command=pagina_listar_livros)
    botao1.grid(row=1, column=0, pady=10)

    botao2 = ctk.CTkButton(janela, text="Pegar Empréstimo", command=pagina_emprestimo)
    botao2.grid(row=2, column=0, pady=10)

    botao3 = ctk.CTkButton(janela, text="Ver Empréstimos", command=pagina_ver_emprestimos)
    botao3.grid(row=3, column=0, pady=10)

    botao4 = ctk.CTkButton(janela, text="Devolver Livro", command=pagina_devolver_livro)
    botao4.grid(row=4, column=0, pady=10)

    janela.mainloop()


#menu de login

def login():

    def enviar_login(): #função de enviar o login
        global usuario_atual #variável usuario atual como global

        email = entrada_email.get() #pega os dados do input
        senha = entrada_senha.get()

        resultado = usuarios.logar_usuario(email, senha) #define variável de resultado do login

        if resultado:
            usuario_atual = resultado
            caixa.delete("0.0", "end")
            caixa.insert("end", "Login realizado com sucesso!")

            janela.after(1500, janela.destroy)

            if resultado["tipo"] == "admin": #se for adm, chamará o menu do adm
                janela.after(100, menu_adm)
            else:
                janela.after(100, menu_usuario) #se for usuario comum, chamara o menu do mesmo

        else:
            caixa.delete("0.0", "end") #se estiver errado, vai tentar denovo
            caixa.insert("end", "Email ou senha incorretos")

    janela = ctk.CTk()
    janela.geometry("350x300")
    janela.title("Login")

    label1 = ctk.CTkLabel(janela, text="Email")
    label1.grid(row=0, column=0, padx=20, pady=20)

    entrada_email = ctk.CTkEntry(janela)
    entrada_email.grid(row=0, column=1)

    label2 = ctk.CTkLabel(janela, text="Senha")
    label2.grid(row=1, column=0)

    entrada_senha = ctk.CTkEntry(janela, show="*")
    entrada_senha.grid(row=1, column=1)

    botao = ctk.CTkButton(janela, text="Entrar", command=enviar_login)
    botao.grid(row=2, column=0, columnspan=2, pady=20)

    caixa = ctk.CTkTextbox(janela, height=60)
    caixa.grid(row=3, column=0, columnspan=2, padx=20)

    janela.mainloop()


# menu de cadastro

def cadastro():

    def cadastrar(): #função de cadastrar

        email = entrada_email.get() #pega os dados do login
        senha = entrada_senha.get()

        usuarios.cadastrar_usuario(email, senha) #chama funcao da classe usuarios

        caixa.delete("0.0", "end")
        caixa.insert("end", "Usuário cadastrado com sucesso!") 
        janela.destroy()
        login() #fecha a janela de cadastro e depois abre a de login para o usuario inserir as informacoes cadastradas

    janela = ctk.CTk()
    janela.geometry("350x300")
    janela.title("Cadastro")

    label1 = ctk.CTkLabel(janela, text="Email")
    label1.grid(row=0, column=0, padx=20, pady=20)

    entrada_email = ctk.CTkEntry(janela)
    entrada_email.grid(row=0, column=1)

    label2 = ctk.CTkLabel(janela, text="Senha")
    label2.grid(row=1, column=0)

    entrada_senha = ctk.CTkEntry(janela)
    entrada_senha.grid(row=1, column=1)

    botao = ctk.CTkButton(janela, text="Cadastrar", command=cadastrar)
    botao.grid(row=2, column=0, columnspan=2, pady=20)

    caixa = ctk.CTkTextbox(janela, height=60)
    caixa.grid(row=3, column=0, columnspan=2)

    janela.mainloop()


# menu inicial 

def menu_inicial():

    def abrir_login(): #funcao que apenas chama a pagina de login
        login()

    def abrir_cadastro(): #funcao que apenas chama a pagina de cadastro
        cadastro()

    janela = ctk.CTk()
    janela.geometry("600x300")
    janela.title("Biblioteca")

    janela.grid_columnconfigure(0, weight=1)

    titulo = ctk.CTkLabel(janela, text="Sistema de Biblioteca", font=("Roboto", 32))
    titulo.grid(row=0, column=0, pady=30)

    botao1 = ctk.CTkButton(janela, text="Login", command=abrir_login)
    botao1.grid(row=1, column=0, pady=10)

    botao2 = ctk.CTkButton(janela, text="Cadastrar", command=abrir_cadastro)
    botao2.grid(row=2, column=0, pady=10)

    janela.mainloop()


# paginas que todo usuário poderá ver 

def pagina_listar_livros():

    janela = ctk.CTk()
    janela.geometry("400x400")
    janela.title("Lista dos Livros")
    caixa = ctk.CTkTextbox(janela)
    caixa.pack(fill="both", expand=True)

    for i, livro in enumerate(biblioteca.livros): #mostrará todos os livros no sistema, por padrão existem 4
        status = "Disponível" if livro["disponível"] else "Indisponível"
        caixa.insert("end", f"{i+1} - {livro['titulo']} ({status})\n")

    janela.mainloop()


def pagina_adicionar_livro():

    def adicionar(): #função de adicionar livro que adiciona o livro na lista dos mesmos

        nome = entrada.get()
        biblioteca.adicionar_livro(nome)

        caixa.insert("end", f"Livro '{nome}' adicionado\n")

    janela = ctk.CTk()
    janela.geometry("400x300")
    janela.title("Adicionar Livros")
    entrada = ctk.CTkEntry(janela, placeholder_text="Nome do livro")
    entrada.pack(pady=20)

    botao = ctk.CTkButton(janela, text="Adicionar", command=adicionar)
    botao.pack()

    caixa = ctk.CTkTextbox(janela)
    caixa.pack(pady=20)

    janela.mainloop()


def pagina_emprestimo(): #pagina de emprestimo de livros

    def emprestar():

        numero = int(entrada.get()) - 1 #pede variavel do numero, tira um para manipular corretamente com o índice
        livro = biblioteca.livros[numero]

        sucesso = usuarios.emprestar_livros(usuario_atual, livro)

        if sucesso:
            caixa.insert("end", "Livro emprestado\n")
        else:
            caixa.insert("end", "Livro indisponível\n")

    janela = ctk.CTk()
    janela.geometry("400x400")
    janela.title("Empréstimo de livros")
    caixa = ctk.CTkTextbox(janela)
    caixa.pack()

    for i, livro in enumerate(biblioteca.livros): #para mostrar todos os livros, e se estão disponíveis ou não
        status = "Disponível" if livro["disponível"] else "Indisponível"
        caixa.insert("end", f"{i+1} - {livro['titulo']} ({status})\n")

    entrada = ctk.CTkEntry(janela, placeholder_text="Número do livro")
    entrada.pack(pady=10)

    botao = ctk.CTkButton(janela, text="Emprestar", command=emprestar)
    botao.pack()

    janela.mainloop()


def pagina_ver_emprestimos():

    janela = ctk.CTk()
    janela.geometry("400x300")
    janela.title("Ver Empréstimos")
    caixa = ctk.CTkTextbox(janela)
    caixa.pack(fill="both", expand=True)

    if usuario_atual["Emprestimos"]: #mostra os empréstimos
        for livro in usuario_atual["Emprestimos"]:
            caixa.insert("end", f"{livro['titulo']}\n")
    else:
        caixa.insert("end", "Nenhum empréstimo")

    janela.mainloop()


def pagina_devolver_livro():

    def devolver():

        numero = int(entrada.get()) - 1 #mesma coisa da pagina de pedir empréstimos
        livro = usuario_atual["Emprestimos"][numero]

        livro["disponível"] = True
        usuario_atual["Emprestimos"].remove(livro)

        caixa.insert("end", "Livro devolvido")

    janela = ctk.CTk()
    janela.geometry("400x300")
    janela.title("Devolução do empréstimo")
    caixa = ctk.CTkTextbox(janela)
    caixa.pack()

    for i, livro in enumerate(usuario_atual["Emprestimos"]): #mostrar os livros emprestados pelo usuario
        caixa.insert("end", f"{i+1} - {livro['titulo']}\n")

    entrada = ctk.CTkEntry(janela, placeholder_text="Número do livro")
    entrada.pack(pady=10)

    botao = ctk.CTkButton(janela, text="Devolver", command=devolver)
    botao.pack()

    janela.mainloop()


def pagina_remover_livro():

    def remover():
        try:
            numero = int(entrada.get()) - 1
            livro = biblioteca.livros[numero]

            biblioteca.livros.remove(livro)

            caixa.insert("end", f"Livro '{livro['titulo']}' removido com sucesso!\n")

        except:
            caixa.insert("end", "Número inválido!\n")

    janela = ctk.CTk()
    janela.geometry("400x400")
    janela.title("Remover Livro")

    caixa = ctk.CTkTextbox(janela)
    caixa.pack(pady=10)

    for i, livro in enumerate(biblioteca.livros):
        status = "Disponível" if livro["disponível"] else "Indisponível"
        caixa.insert("end", f"{i+1} - {livro['titulo']} ({status})\n")

    entrada = ctk.CTkEntry(janela, placeholder_text="Número do livro")
    entrada.pack(pady=10)

    botao = ctk.CTkButton(janela, text="Remover", command=remover)
    botao.pack(pady=10)

    janela.mainloop()