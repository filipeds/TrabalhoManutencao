#Autores: Filipe Zanin e Gabriel Macedo.  
#Index é o responśvel por fazer todas as interações com o cliente.
#tkinter = biblioteca responsável por criar as interfaces gráficas do projeto.
#BasedeDados = guarda os dados dos usúarios cadastrados em um banco de dados SQLite3.
#pandas = é uma biblioteca que nos dá a liberdade de puxar determinado lugar na web.

from tkinter import *
from tkinter import messagebox, Frame
from tkinter import ttk
import BasedeDados
import pandas as pd

#Pega os dados de outro lugar para podermos utilizar dentro do código
uri = "https://raw.githubusercontent.com/alura-cursos/introducao-a-data-science/master/aula6.2/movies.csv"

#Altera o nome das colunas para português
filmes = pd.read_csv(uri)
filmes.columns = ['Filmes Id', 'Título', 'Generos']
uri = "https://raw.githubusercontent.com/alura-cursos/introducao-a-data-science/master/aula6.2/ratings.csv"
notas = pd.read_csv(uri)
notas.columns = ['Usuarios Id', 'Filmes Id', 'Nota', 'Momento']


#Criação janela e seus atributos.
janela = Tk()
janela.title('TS-Flix')
janela.geometry('600x300')
janela.configure(background="white")
janela.resizable(width=False, height=False)

#Puxando a imagem
logo = PhotoImage(file="fundo.png")

#Criando a divisão com Frames
#Frame Esquerdo
LEFTFrame = Frame(janela, width=200, height=300, bg="#48514e", relief="raise")
LEFTFrame.pack(side=LEFT)
#Frame Direito
RIGHTFrame = Frame(janela, width=395, height=300, bg="#48514e", relief="raise")
RIGHTFrame.pack(side=RIGHT)

#Colocano a imagem como fundo do Frame Esquerdo
LogoLabel = Label(LEFTFrame, image=logo, bg="black")
LogoLabel.place(x=0, y=0)

#Criando label da Versão
VersaoLabel = Label(LEFTFrame, text="Versão - 2020.2", font=("Arial", 15), bg="#48514e", fg="white")
VersaoLabel.place(x=50, y=270)

#Label Titulo
TituloLabel = Label(RIGHTFrame, text='TS-Flix', font=("Consolas", 25), bg="#48514e", fg="white")
TituloLabel.place(x=197, y=5)

#Criando as Labels (nome, senha)
#Label Nome
UserLabel = Label(RIGHTFrame, text="Username:", font=("Consolas", 20), bg="#48514e", fg="white")
UserLabel.place(x=5, y=100)
#Entry(local onde a pessoa digita)
UserEntry = ttk.Entry(RIGHTFrame, width=25)
UserEntry.place(x=175, y=110)
#Label Senha
PassLabel = Label(RIGHTFrame, text="Senha:", font=("Consolas", 20), bg="#48514e", fg="white")
PassLabel.place(x=5, y=150)
#Entry(local onde a pessoa digita)
PassEntry = ttk.Entry(RIGHTFrame, width=25, show="•")
PassEntry.place(x=175, y=160)



def cadastrar():
    """
    Cria os botões e labels que os usuarios utilizam para realizarem o cadastro.
    :return:
    """
    #Removendo os botões de login
    TituloLabel.place(x=9999999)
    LoginButton.place(x=9999999)
    RegisterButton.place(x=9999999)
    #Inserindo Widgets de cadastro
    NomeLabel = Label(RIGHTFrame, text="Nome:", font=("Consolas", 20), bg="#48514e", fg="white")
    NomeLabel.place(x=5, y=5)
    NomeEntry = ttk.Entry(RIGHTFrame, width=25)
    NomeEntry.place(x=175, y=12)
    EmailLabel = Label(RIGHTFrame, text="Email:", font=("Consolas", 20), bg="#48514e", fg="white")
    EmailLabel.place(x=5, y=55)
    EmailEntry = ttk.Entry(RIGHTFrame, width=25)
    EmailEntry.place(x=175, y=62)

    def CadastrarDados():
        """
        Examina os dados que os usuarios preencheram, se estiver preenchido corretamente os dados são enviados para o banco de dados
        :returns: messagebox.showinfo(title=Cadastro Info, message=Cadastrado com Sucesso)
        """
        Nome = NomeEntry.get()
        Email = EmailEntry.get()
        Username = UserEntry.get()
        Senha = PassEntry.get()
        
        #notifica que deve preencher todas os campos caso algum esteja faltando
        if (Nome == "" and Email == "" and Username == "" and Senha == ""):
            messagebox.showerror(title="Erro no Cadastro", message="Preencha os Campos.")

        else:
            BasedeDados.cursor.execute("""
            INSERT INTO Usuarios(Nome, Email, Usuario, Senha) VALUES(?, ?, ?, ?)
            """, (Nome, Email, Username, Senha))
            BasedeDados.conn.commit()
            messagebox.showinfo(title="Cadastro Info", message="Cadastrado Com Sucesso")

    Register = ttk.Button(RIGHTFrame, text="Cadastrar", width=20, command=CadastrarDados)
    Register.place(x=30, y=225)

    def VoltarLogin():
        """
        Após o usuario ter clicado no botão Voltar na Tela de Cadastro, ele é movido para a Tela de Login
        :return:
        """
        #Removendo Widgtes da Cadastro
        NomeLabel.place(x=9999999)
        NomeEntry.place(x=9999999)
        EmailLabel.place(x=9999999)
        EmailEntry.place(x=9999999)
        Register.place(x=9999999)
        Voltar.place(x=9999999)
        #Voltando os Widgets do Login
        TituloLabel.place(x=197, y=5)
        LoginButton.place(x=209, y=225)
        RegisterButton.place(x=30, y=225)
    Voltar = ttk.Button(RIGHTFrame, text="Voltar", width=20, command=VoltarLogin)
    Voltar.place(x=209, y=225)

def Login():
    """
    Verifica se os dados inseridos no login já foram registrados, se os dados já estiveram sido cadastrados retorna uma mensagem
    :return: messagebox.showinfo(title="Login Info", message="Acesso Permitido. Bem Vindo!")
    """
    Usuario = UserEntry.get()
    Senha = PassEntry.get()
    BasedeDados.cursor.execute("""
        SELECT * FROM Usuarios
        WHERE (Usuario = ? and Senha = ?)
        """, (Usuario, Senha))
    VerificarLogin = BasedeDados.cursor.fetchone()

    def MenuOpcoes():
        """
        Cria todos os botões e labels que serão utilizados no menu e em suas opções
        :return:
        """
        # Escluindo os Widgets De Login
        TituloLabel.place(x=9999999)
        UserLabel.place(x=9999999)
        UserEntry.place(x=9999999)
        PassLabel.place(x=9999999)
        PassEntry.place(x=9999999)
        RegisterButton.place(x=9999999)
        LoginButton.place(x=9999999)
        # Colocando Widgets De Opções
        BuscaLabel = Label(RIGHTFrame, text=' - Busca Por Avaliação', font=("Consolas", 12), bg="#48514e", fg="white")
        BuscaLabel.place(x=5, y=130)
        OpcoesLabel = Label(RIGHTFrame, text='Opções', font=("Consolas", 20), bg="#48514e", fg="white")
        OpcoesLabel.place(x=197, y=5)
        VotacaoLabel = Label(RIGHTFrame, text=' - Ir Para Votação', font=("Consolas", 12), bg="#48514e", fg="white")
        VotacaoLabel.place(x=5, y=90)

        def Votacao():
            """
            Cria as labels que iram ser utilizadas na votação
            :return:
            """
            #Removendo os Widgets
            OpcoesLabel.place(x=9999999)
            BuscaLabel.place(x=9999999)
            VotacaoLabel.place(x=9999999)
            OpcoesButton.place(x=9999999)
            BuscaButton.place(x=9999999)
            #Criando os Widgets
            NomeFilmeLabel = Label(RIGHTFrame, text='Digite o Nome do Filme ->', font=("Consolas", 10), bg="#48514e", fg="white")
            NomeFilmeLabel.place(x=3, y=100)
            NomeFilmeEntry = ttk.Entry(RIGHTFrame, width=20)
            NomeFilmeEntry.place(x=205, y=100)
            VoteLabel = Label(RIGHTFrame, text='Vote Agora Mesmo ->', font=("Consolas", 10), bg="#48514e", fg="white")
            VoteLabel.place(x=3, y=150)
            VoteEntry = ttk.Entry(RIGHTFrame, width=20)
            VoteEntry.place(x=205, y=150)
            TituloVotacaoLabel = Label(RIGHTFrame, text='Votação', font=("Consolas", 20), bg="#48514e", fg="white")
            TituloVotacaoLabel.place(x=150, y=5)
            
            def AnalizarVoto():
                """
                Cria o Botão Votar,
                Examina o voto, se estiver com as labels preenchidas da maneira certa é retornado uma mensagem
                :return:messagebox.showinfo('Voto Info', message='Você acaba de Votar em {}'.format(NomeFilme))
                """
                Voto = VoteEntry.get()
                NomeFilme = NomeFilmeEntry.get()
                if Voto.isnumeric():
                    messagebox.showinfo('Voto Info', message='Você acaba de Votar em {}'.format(NomeFilme))
                else:
                    messagebox.showerror('Voto Info', message='!ERRO! Só seram aceitos números na votação!')
            VoteButton = ttk.Button(RIGHTFrame,text='Votar',width=20, command=AnalizarVoto)
            VoteButton.place(x=209, y=195)
            
            def MenuOpcoes3():
                """
                Permite que o usuário escolha uma entre as opções aprensentadas:
                O "Voltar" volta para o "MenuOpcoes3" e o "Votação" volta para o "votacao".

                :return:
                """
                BuscaLabel.place(x=5, y=130)
                OpcoesLabel.place(x=197, y=5)
                VotacaoLabel.place(x=5, y=90)
                BuscaButton.place(x=30, y=225)
                NomeFilmeLabel.place(x=9999999)
                NomeFilmeEntry.place(x=9999999)
                VoteLabel.place(x=9999999)
                VoteEntry.place(x=9999999)
                TituloVotacaoLabel.place(x=9999999)
                VoltarButton.place(x=9999999)
                VoteButton.place(x=9999999)
                BuscaButton.place(x=30, y=225)
            VoltarButton = ttk.Button(RIGHTFrame, text="Voltar", width=20, command=MenuOpcoes3)
            VoltarButton.place(x=30, y=225)

        VotacaoButton = ttk.Button(RIGHTFrame, text="Votação", width=20, command=Votacao)
        VotacaoButton.place(x=209, y=225)



        def BuscarFilmes():
            """
            Faz a busca do filme desejado, por nota,  id, avaliações ou gêneros.

            :return:
            """
            # Removendo os Widgets
            OpcoesLabel.place(x=9999999)
            BuscaLabel.place(x=9999999)
            VotacaoLabel.place(x=9999999)
            OpcoesButton.place(x=9999999)
            VotacaoButton.place(x=9999999)
            #Criando Widgets
            TituloBuscaLabel = Label(RIGHTFrame, text='Busca dos Filmes pelas Avaliações', font=("Consolas", 10), bg="#48514e", fg="white")
            TituloBuscaLabel.place(x=0, y=5)
            BuscaFilmesAvaliacoesLabel = Label(RIGHTFrame, text=notas.head(), font=("Consolas", 7), bg="#48514e", fg="white")
            BuscaFilmesAvaliacoesLabel.place(x=0, y=32)
            FilmesIdLabel = Label(RIGHTFrame, text='Id´s e Gêneros dos Filmes', font=("Consolas",10), bg="#48514e", fg="white")
            FilmesIdLabel.place(x=0, y=103)
            MostrarFilmesIdLabel = Label(RIGHTFrame, text=filmes.head(), font=("Consolas", 7), bg="#48514e", fg="white")
            MostrarFilmesIdLabel.place(x=0, y=125)
            
            def MenuOpcoes2():
                """
                Permite que o usuário escolha uma entre as opções aprensentadas:
                O "Voltar" volta para o "MenuOpcoes2" e o "Busca" vai para o "BuscarFilmes".

                :return:
                """
                BuscaLabel.place(x=5, y=130)
                OpcoesLabel.place(x=197, y=5)
                VotacaoLabel.place(x=5, y=90)
                VotacaoButton = ttk.Button(RIGHTFrame, text="Votação", width=20, command=Votacao)
                VotacaoButton.place(x=209, y=225)
                BuscaButton.place(x=30, y=225)
                TituloBuscaLabel.place(x=9999999)
                BuscaFilmesAvaliacoesLabel.place(x=9999999)
                FilmesIdLabel.place(x=9999999)
                MostrarFilmesIdLabel.place(x=9999999)
                VoltarButton.place(x=9999999)
            VoltarButton = ttk.Button(RIGHTFrame, text="Voltar", width=20, command=MenuOpcoes2)
            VoltarButton.place(x=209, y=225)

        BuscaButton = ttk.Button(RIGHTFrame, text="Busca", width=20, command=BuscarFilmes)
        BuscaButton.place(x=30, y=225)

        try:
            if (Usuario in VerificarLogin and Senha in VerificarLogin):
                messagebox.showinfo(title="Login Info", message="Acesso Permitido. Bem Vindo!")
                OpcoesButton = ttk.Button(RIGHTFrame, text="Menu Opções", width=20, command=MenuOpcoes)
                OpcoesButton.place(x=30, y=255)
        except:
            messagebox.showinfo(title="Login Info", message="Acesso Negado. Verifique Seus Dados de Login ou Cadastre-se!")

# Botão Login
LoginButton = ttk.Button(RIGHTFrame, text="Login", width=20, command=Login)
LoginButton.place(x=209, y=225)
# Botão Cadastrar
RegisterButton = ttk.Button(RIGHTFrame, text="Cadastrar", width=20, command=cadastrar)
RegisterButton.place(x=30, y=225)

#Função para rodar a janela
janela.mainloop()
