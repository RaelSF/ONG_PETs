from PIL import Image as IMG
from PIL import ImageTk
from tkinter import messagebox, ttk, filedialog
from tkinter import *
from tkinter.filedialog import askopenfile, askopenfilename, askopenfilenames
import BancoDados
from Gerenciador import *
from Adocao import *
from Tabela_Pets import *

cor='#05264b'
fonte = ("georgia",17)
fontebotao= ("inter", 18, 'bold')

#classe da tela inicial
class TelaInicial():
   def __init__(self):

      self.janela_i = Tk()
      self.Tela()
      self.frames()
      self.janela_i.mainloop()
#funcao para volta 
   def  backinicia(self):
      self.janela_i.destroy()
      self.__init__()
#configuracoes da tela
   def Tela (self):
      self.janela_i.title("ONG")
      self.janela_i.geometry("1260x1024")
      self.janela_i.configure(bg=cor)
#frames da tela
   def frames (self):
      self.nometela= Label (self.janela_i)
      self.nometela.config(text= 'LOVE PET',font= ('inter', 33, 'bold'),bg=cor, fg='white')
      self.nometela.pack(pady=50)

      self.frameprin= Frame(self.janela_i, bg=cor)
      self.frameprin.place(x= 420,y=180)
      self.cadastro=Button(self.frameprin, text= 'Cadastrar',font=fontebotao,width=14, height=1, command=self.Cadastro, activebackground= 'LightSlateGray', activeforeground='DarkGrey')
      self.cadastro.grid(column=0,row=0, pady= 25, padx=30)
      self.cadastropet=Button(self.frameprin, text= 'Cadastrar Pet',font=fontebotao,width=14, height=1, command=self.cadpet, activebackground= 'LightSlateGray', activeforeground='DarkGrey')
      self.cadastropet.grid(column=1,row=0, pady= 25, padx=30)
      self.adocao=Button(self.frameprin, text= 'Adoção',font=fontebotao,width=14, height=1, command=Adocao_pet, activebackground= 'LightSlateGray', activeforeground='DarkGrey')
      self.adocao.grid(column=0,row=1, pady= 25, padx=30)
      self.tabelapet=Button(self.frameprin, text= 'Tabela de Pets',font=fontebotao,width=14, height=1, command=self.tabepet, activebackground= 'LightSlateGray', activeforeground='DarkGrey')
      self.tabelapet.grid(column=1,row=1, pady= 25, padx=30)
      self.gerenciador=Button(self.frameprin, text= 'Gerenciador',font=fontebotao,width=14, height=1, command=self.gerenciamento, activebackground= 'LightSlateGray', activeforeground='DarkGrey')
      self.gerenciador.grid(column=0,row=2, pady= 25, padx=30)
      self.cadastroclinica=Button(self.frameprin, text= 'Cadastrar Clinica',font=fontebotao,width=14, height=1, activebackground= 'LightSlateGray', activeforeground='DarkGrey')
      self.cadastroclinica.grid(column=1,row=2, pady= 25, padx=30)

      #self.imagem_diretorio = "C:/Users/rafael/Desktop/Topicos Linguagem de Programação/imagens/Cadu.png"
      #imagem = IMG.open(self.imagem_diretorio)
      #self.foto = ImageTk.PhotoImage(imagem)

      #self.imagemlbl=Label(self.janela_i, bg='black')
      #self.imagemlbl.config(image=self.foto)
      #self.imagemlbl.pack(side=LEFT)

      #funcao de cadastrar pessoa
   def Cadastro (self):
      self.frameprin.destroy()
      self.nometela.config(text= 'Cadastro',font= ('inter', 33, 'bold'),bg=cor, fg='white')
      self.selecadastro=Button(self.janela_i, text= 'Registrar',font=fontebotao,width=10, height=1, command=self.regipessoa, activebackground= 'LightSlateGray', activeforeground='DarkGrey')
      self.selecadastro.place(x=500, y=650)
      self.cancelar=Button(self.janela_i, text= 'Cancelar',font=fontebotao,width=10, height=1, command=self.backinicia, activebackground= 'LightSlateGray', activeforeground='DarkGrey')
      self.cancelar.place(x=700, y=650)

      infor= Label(self.janela_i,text= 'Informações',font= ('inter', 25, 'bold'),bg=cor, fg='white' )
      infor.place(x=420, y=150)
      ender= Label(self.janela_i,text= 'Endereço',font= ('inter', 25, 'bold'),bg=cor, fg='white' )
      ender.place(x=840, y=150)

      self.framecad=Frame(self.janela_i, width=950, height=350, bg=cor)
      self.framecad.place(x= 330,y=250)

      nomelbl=Label(self.framecad,width = 9, height = 2,text='Nome:', font=fonte, bg=cor, fg='white' )
      nomelbl.place(x=21,y=0)
      self.nomeentry= Entry(self.framecad,width=16, font=("georgia",11))
      self.nomeentry.place(x=130, y= 17)

      cpflbl=Label(self.framecad,width = 9, height = 2,text='CPF:', font=fonte, bg=cor, fg='white' )
      cpflbl.place(x=30,y=50)
      self.cpfentry= Entry(self.framecad,width=16, font=("georgia",11))
      self.cpfentry.place(x=130, y= 67)

      emaillbl=Label(self.framecad,width = 9, height = 2,text='E-Mail:', font=fonte, bg=cor, fg='white' )
      emaillbl.place(x=15,y=100)
      self.emailentry= Entry(self.framecad,width=16, font=("georgia",11))
      self.emailentry.place(x=130, y= 117)
      
      telefonelbl=Label(self.framecad,width = 9, height = 2,text='Telefone:', font=fonte, bg=cor, fg='white' )
      telefonelbl.place(x=9,y=150)
      self.telefoneentry= Entry(self.framecad,width=16, font=("georgia",11))
      self.telefoneentry.place(x=130, y= 167)



      rualbl=Label(self.framecad,width = 9, height = 2,text='Rua:', font=fonte, bg=cor, fg='white' )
      rualbl.place(x=420,y=0)
      self.ruaentry= Entry(self.framecad,width=16, font=("georgia",11))
      self.ruaentry.place(x=520, y= 17)


      numerocslbl=Label(self.framecad,width = 9, height = 2,text='Numero:', font=fonte, bg=cor, fg='white' )
      numerocslbl.place(x=400,y=50)
      self.numerocsentry= Entry(self.framecad,width=16, font=("georgia",11))
      self.numerocsentry.place(x=520, y= 67)

      bairrolbl=Label(self.framecad,width = 9, height = 2,text='Bairro:', font=fonte, bg=cor, fg='white' )
      bairrolbl.place(x=410,y=100)
      self.bairroentry= Entry(self.framecad,width=16, font=("georgia",11))
      self.bairroentry.place(x=520, y= 117)

      cidadelbl=Label(self.framecad,width = 9, height = 2,text='Cidade:', font=fonte, bg=cor, fg='white' )
      cidadelbl.place(x=405,y=150)
      self.cidadeentry= Entry(self.framecad,width=16, font=("georgia",11))
      self.cidadeentry.place(x=520, y= 167)

      telefonelbl=Label(self.framecad,width = 12, height = 2,text='Tipo de Pessoa:', font=fonte, bg=cor, fg='white' )
      telefonelbl.place(x=150,y=220)
      self.CheckVar1=IntVar()
      self.CheckVar2=IntVar()
   
      tipopessoaad=Checkbutton(self.framecad, width = 9, height = 1,text='Adotante', font=fonte, bg=cor, fg='white',activebackground=cor, cursor='arrow', variable = self.CheckVar1, onvalue=1, offvalue=0,selectcolor=cor, bd=4)
      tipopessoaad.place(x=330, y= 230)
      tipopessoavo=Checkbutton(self.framecad, width = 9, height = 1,text='Voluntario', font=fonte, bg=cor, fg='white',activebackground=cor, cursor='arrow', variable = self.CheckVar2, onvalue=1, offvalue=0, selectcolor=cor, bd=4)
      tipopessoavo.place(x=338, y= 270)

   def Tipo_Pessoa (self):
      TxtP=""
      if (self.CheckVar1.get() == 1):
         TxtP=TxtP + "adotante\n"
      if (self.CheckVar2.get() == 1):
         TxtP=TxtP + "voluntario\n "
      return TxtP
 
      #funcao para registrar pessoa
   def regipessoa(self):
      nome=self.nomeentry.get()
      cpf=self.cpfentry.get()
      email=self.emailentry.get()
      telefone=self.telefoneentry.get()
      rua=self.ruaentry.get()
      numero=self.numerocsentry.get()
      bairro=self.bairroentry.get()
      cidade=self.cidadeentry.get()
      endereco=rua +","+ numero +"," + bairro + ","+ cidade
      tipopessoa=self.Tipo_Pessoa()

      txt = ""
      if nome == "":
         txt =  txt + "Falta criar o Nome!\n"
      if cpf == "":
         txt =  txt + "Falta criar o cpf!\n"
      if email == "":
         txt =  txt + "Falta criar o E-Mail!\n"
      if telefone == "":
         txt =  txt + "Falta criar a Telefone!\n"
      if endereco == "":
         txt =  txt + "Falta Informa Endereço!\n"
      

      if txt != "":
         messagebox.showerror(title="Erro Ao Realizar Cadastro", message=txt)
      else:
         BancoDados.cursor.execute("""INSERT INTO cadpessoa(nome,cpf,email,telefone,endereco,tipopessoa) VALUES(?,?,?,?,?,?) """,(nome, cpf, email, telefone, endereco, tipopessoa ))
         BancoDados.banco.commit()
         messagebox.showinfo(title="Sucesso!", message="Usuario Cadastrado com Sucesso!")
         self.backinicia()
            
            

   def cadpet (self):
      self.frameprin.destroy()
      self.nometela.config(text= 'Cadastro de Pet',font= ('inter', 33, 'bold'),bg=cor, fg='white')

      self.framecad=Frame(self.janela_i, width=750, height=750, bg=cor)
      self.framecad.place(x= 385,y=150)

      nomelbl=Label(self.framecad,width = 9, height = 2,text='Nome:', font=fonte, bg=cor, fg='white' )
      nomelbl.place(x=148,y=0)
      self.nomeentry= Entry(self.framecad,width=16, font=("georgia",11))
      self.nomeentry.place(x=260, y= 17)

      racalbl=Label(self.framecad,width = 9, height = 2,text='Raça:', font=fonte, bg=cor, fg='white' )
      racalbl.place(x=155,y=50)
      self.racaentry= Entry(self.framecad,width=16, font=("georgia",11))
      self.racaentry.place(x=260, y= 67)

      generolbl=Label(self.framecad,width = 9, height = 2,text='Gênero:', font=fonte, bg=cor, fg='white' )
      generolbl.place(x=145,y=100)
      self.generoentry= Entry(self.framecad,width=16, font=("georgia",11))
      self.generoentry.place(x=260, y= 117)
      
      idadelbl=Label(self.framecad,width = 9, height = 2,text='idade:', font=fonte, bg=cor, fg='white' )
      idadelbl.place(x=153,y=150)
      self.idadeentry= Entry(self.framecad,width=16, font=("georgia",11))
      self.idadeentry.place(x=260, y= 167)

      opcaolbl=Label(self.framecad,width = 9, height = 2,text='Status:', font=fonte, bg=cor, fg='white' )
      opcaolbl.place(x=150,y=200)

      self.status=ttk.Combobox(self.framecad, width= 14,font=("georgia",11))
      self.status.set('Selecionar')
      self.status['values'] = ['Disponivel', 'Não Disponivel'] 
      self.status['state'] = 'readonly'
      self.status.place(x=260, y=217)

      opcaolbl=Label(self.framecad,width = 9, height = 2,text='Imagem:', font=fonte, bg=cor, fg='white' )
      opcaolbl.place(x=140,y=250)

      #self.imagemlbl=Label(self.framecad,width = 9, height = 2,text='Imagem:', font=fonte, bg='white', fg='white' )
      #self.imagemlbl.place(x=230,y=230)
      #self.imagem_diretorio ='C:\\Users\\rafael\\Desktop\\"Topicos Linguagem de Programação"\\imagens\\Cadu.png'

      #imagem = Image.open(self.framecad)
      #self.foto=ImageTk.PhotoImage(imagem)
      
      #self.imglbl.place(x=0, y=0)

      self.imgButton=Button(self.framecad, width = 19, height = 1, text='Selecionar Imagem', command=self.seleimg, activebackground= 'LightSlateGray', activeforeground='DarkGrey')
      self.imgButton.place(x=260,y=270)

      selecadastro=Button(self.janela_i, text= 'Registrar',font=fontebotao,width=10, height=1, command=self.Regi_Pet, activebackground= 'LightSlateGray', activeforeground='DarkGrey')
      selecadastro.place(x=520, y=650)
      cancelar=Button(self.janela_i, text= 'Cancelar',font=fontebotao,width=10, height=1, command=self.backinicia, activebackground= 'LightSlateGray', activeforeground='DarkGrey')
      cancelar.place(x=700, y=650)

   def seleimg(self):

      self.imagem_diretorio=filedialog.askopenfilename()
      self.imglbl=Label(self.framecad,image=self.foto,width=200, height=200)
      imagem = IMG.open(self.imagem_diretorio)
      self.foto = ImageTk.PhotoImage(imagem)
      self.imglbl.config(image=self.foto,)
      self.imglbl.place(x=260, y=260)
      
   def Regi_Pet(self):
      nome=self.nomeentry.get()
      raca=self.racaentry.get()
      genero=self.generoentry.get()
      idade=self.idadeentry.get()
      status_P=self.status.get()
      

      txt = ""
      if nome == "":
         txt =  txt + "Falta criar o Nome!\n"
      if raca == "":
         txt =  txt + "Falta criar o Raça!\n"
      if genero == "":
         txt =  txt + "Falta criar o Gênero!\n"
      if idade == "":
         txt =  txt + "Falta criar a Idade!\n"
      if status_P == "Selecionar":
         txt = txt + "Falta selecionar o Status!\n"

      if txt != "":
         messagebox.showerror(title="Erro Ao Realizar Cadastro", message=txt)
      else:
         BancoDados.cursor.execute("""INSERT INTO cadpet(nome,raca,genero,idade, status, imagem) VALUES(?,?,?,?,?,?) """,(nome, raca, genero, idade, status_P, self.imagem_diretorio))
         BancoDados.banco.commit()
         messagebox.showinfo(title="Sucesso!", message="Pet Cadastrado com Sucesso!")
         self.backinicia()

   def tabepet (self):
      Tabela_Pets()
   def gerenciamento(self):
      #self.janela_i.destroy()
      Tabela_Gerenciar()

#TelaInicial()