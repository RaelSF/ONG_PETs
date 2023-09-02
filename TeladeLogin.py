from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import BancoDados
from TelaInicial import *

#criar janela
janela = Tk()
janela.title("ONG")
janela.geometry("1260x1024")
janela.configure(background = "#05264b")
#simplificar comandos
cor='#05264b'
fonte = ("georgia",17)
fontebotao= ("inter", 15, 'bold')


#criar frames principal de login
framelog=Frame(janela, width = 300, height = 600, bg=cor,relief = "raise")
framelog.pack()

#criar frames para o principal
userlbl=Label(framelog,width = 7, height = 2,text='Login:', font=fonte, bg=cor, fg='white' )
userlbl.place(x=1 ,y=200)

userEntry= Entry(framelog, width=25)
userEntry.place(x=100, y= 220)

senhalbl=Label(framelog,width = 7, height = 2,text='Senha:', font=fonte, bg=cor, fg='white' )
senhalbl.place(x=1,y=250)

SenhaEntry= Entry(framelog,width=25,show="•")
SenhaEntry.place(x=100, y= 270)

#criando funcao para cadastrar usuario
def caduser ():
    nomepag=Label(janela,width = 20, height = 2,text='Cadastrar Usuario', font=("inter", 20, 'bold'), bg=cor, fg='white' )
    nomepag.place(y=40, x=490)

    userEntry.delete(0,END)
    SenhaEntry.delete(0,END)
    login.place(x= 8000)
    register.place(x= 80000)

    numerolbl=Label(framelog,width = 7, height = 2,text='Numero:', font=fonte, bg=cor, fg='white' )
    numerolbl.place(x=0,y=300)
    numeroEntry= Entry(framelog,width=25)
    numeroEntry.place(x=100, y= 320)

    nomelbl=Label(framelog,width = 7, height = 2,text='Nome:', font=fonte, bg=cor, fg='white' )
    nomelbl.place(x=0,y=150)
    nomeEntry= Entry(framelog,width=25)
    nomeEntry.place(x=100, y= 170)


    def voltalogin():

        userEntry.delete(0,END)
        SenhaEntry.delete(0,END)
        numeroEntry.delete(0,END)
        nomeEntry.delete(0,END)
        numerolbl.place(x=800000)
        nomelbl.place(x=800000)
        numeroEntry.place(x=800000)
        nomeEntry.place(x=800000)

        login.place(x= 30,y=380)
        register.place(x= 150,y=380)
        volta.place(x=80000)
        registrar.place(x=80000)
        nomepag.destroy()


    volta=Button(framelog,text= 'Volta',font=fontebotao, width=8, command=voltalogin, activebackground= 'LightSlateGray', activeforeground='DarkGrey')
    volta.place(x= 20,y=530)


   
    def cadBancoDados():
        nome=nomeEntry.get()
        user=userEntry.get()
        senha=SenhaEntry.get()
        numero=numeroEntry.get()

        txt = ""
        if nome == "":
            txt =  txt + "Falta criar o Nome!\n"
        if numero == "":
            txt =  txt + "Falta criar o Email!\n"
        if user == "":
            txt =  txt + "Falta criar o Usuario!\n"
        if senha == "":
            txt =  txt + "Falta criar a Senha!\n"

        if txt != "":
            messagebox.showerror(title="Erro Ao Realizar Cadastro", message=txt)
        else:
            BancoDados.cursor.execute("""
                INSERT INTO user(nome,numero,user,senha) VALUES(?,?,?,?) 
            """, (nome, numero, user, senha))

            BancoDados.banco.commit()
            messagebox.showinfo(title="Sucesso!", message="Usuario Cadastrado com Sucesso!")
            voltalogin()

    registrar=Button(framelog,text= 'Registrar',font=fontebotao, width=8, command=cadBancoDados, activebackground= 'LightSlateGray', activeforeground='DarkGrey' )
    registrar.place(x= 160,y=530)


#criando botoes de acesso
register=Button(framelog,text= 'Cadastrar',font=fontebotao,command= caduser, activebackground= 'LightSlateGray', activeforeground='DarkGrey')
register.place(x= 150,y=380)

#funcao fazer login
def logar():
    login = userEntry.get()
    senha = SenhaEntry.get()

    txt = ""
    if login == "":
        txt = txt  + "Você se esqueceu do Usuario\n"
    if senha == "":
        txt = txt + "Você se esqueceu do senha?\n"
    
    if txt != "":
        messagebox.showerror(title="Login Info",message=txt)

    else:
        BancoDados.cursor.execute ('SELECT * FROM user  WHERE (user = ? AND senha = ?)',(login,senha))
        VerifyLogin = BancoDados.cursor.fetchone()
        try: 
            if login in VerifyLogin and senha in VerifyLogin:
                messagebox.showinfo(title="Login Info", message="Seja Bem Vindo!")
                janela.destroy()
                TelaInicial()
        except:
            messagebox.showerror(title="Login Info",message="Este usuário não está cadastrado!")

login= Button(framelog,text= 'Acessar',font=fontebotao, command=logar, activebackground= 'LightSlateGray', activeforeground='DarkGrey')
login.place(x= 30,y=380)


janela.mainloop()