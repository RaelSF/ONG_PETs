from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter
from cProfile import label
from msilib.schema import ListBox
from tkinter import*
import sqlite3

cor='#05264b'
fonte = ("georgia",17)
fontebotao= ("inter", 18, 'bold')

class Tabela_Gerenciar():
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
        self.janela_i.title("Verificação Adotantes")
        self.janela_i.geometry("1260x1024")
        
        self.barra_menu=Menu(self.janela_i)
        self.janela_i.configure(bg=cor,menu=self.barra_menu)

        
        self.barra_menu.add_cascade(label = "Verifição das Adoções", command=self.VA)
        self.barra_menu.add_cascade (label = "Pessoas Cadastradas", command=self.VP)

        
            
    def VA(self):
        #self.pesquisarbutton.destroy()
        
        self.situacaolbl=Label(self.frameprin,width = 9, height = 2,text='Situação:', font=fonte, bg=cor, fg='white' )
        self.situacaolbl.place(x=10,y=100)
        self.status=ttk.Combobox(self.frameprin, width= 14,font=("georgia",11))
        self.status.set('Selecionar')
        self.status['values'] = ['Aprovado', 'Negado' , 'Analise'] 
        self.status['state'] = 'readonly'
        self.status.place(x=130, y=120)

        self.aprovarbutton=Button(self.janela_i, text="Aprovar", font=fonte, command=self.Aprovar, width=7)
        self.aprovarbutton.place(x=540,y=630)
        self.negarbutton=Button(self.janela_i, text="Negado", font=fonte, command=self.Negar, width=7)
        self.negarbutton.place(x=740,y=630)
        self.pesquisarbutton=Button(self.frameprin, text="Pesquisar", font=("georgia",11), command=self.pesquisarADO)
        self.pesquisarbutton.place(x=130,y=170)
        self.Criar_tabelaAdo()
        self.InserAtualiADO()
    
    def pesquisarADO (self):
        self.tabela.delete(*self.tabela.get_children())
        if self.status.get() == "Selecionar":
            listaBanco="SELECT * FROM adocao where cpf LIKE '%"+self.cpfentry.get()+"%' AND nome_adotante LIKE'%"+self.nomeentry.get()+"%'order by id"
            self.lista = self.filtre(listaBanco)
            for item in self.lista:
                self.tabela.insert('','end', values=(item[0],item[1],item[2],item[3],item[5], item[4]))

        #self.InserAtualiADO()
        elif self.status.get() != "Selecionar":
            listaBanco="SELECT * FROM adocao where cpf LIKE '%"+self.cpfentry.get()+"%' AND nome_adotante LIKE'%"+self.nomeentry.get()+"%' AND status LIKE'%"+self.status.get()+"%' order by id"
            self.lista = self.filtre(listaBanco)
            for item in self.lista:
                self.tabela.insert('','end', values=(item[0],item[1],item[2],item[3],item[5], item[4]))


        

        
    
    def VP (self):
        #self.pesquisarbutton.destroy()
        self.situacaolbl.destroy()

        self.modificarbutton=Button(self.janela_i, text="Modificar", font=fonte, command=self.Aprovar, width=7)
        self.modificarbutton.place(x=540,y=630)
        self.deletarbutton=Button(self.janela_i, text="Deletar", font=fonte, command=self.Negar, width=7)
        self.deletarbutton.place(x=740,y=630)

        self.situacaolbl=Label(self.frameprin,width = 9, height = 2,text='Tipo:', font=fonte, bg=cor, fg='white' )
        self.situacaolbl.place(x=30,y=100)
        self.status=ttk.Combobox(self.frameprin, width= 14,font=("georgia",11))
        self.status.set('Selecionar')
        self.status['values'] = ['Todos','Adotante', 'Voluntario'] 
        self.status['state'] = 'readonly'
        self.status.place(x=130, y=120)

        self.pesquisarbutton=Button(self.frameprin, text="Pesquisar", font=("georgia",11), command=self.pesquisarPS)
        self.pesquisarbutton.place(x=130,y=170)
        self.Criar_tabelaPS()
        self.InserAtualiPS()

    def pesquisarPS (self):
        self.tabela.delete(*self.tabela.get_children())
        if self.status.get() == "Selecionar":
            self.tabela.delete(*self.tabela.get_children())
            listaBanco="SELECT * FROM cadpessoa where cpf LIKE '%"+self.cpfentry.get()+"%' AND nome LIKE'%"+self.nomeentry.get()+"%'order by id"
            self.lista = self.filtre(listaBanco)
            for item in self.lista:
                self.tabela.insert('','end', values=(item[0],item[1],item[2],item[3],item[4], item[6]))

        elif self.status.get() != "Selecionar":
            self.tabela.delete(*self.tabela.get_children())
            listaBanco="SELECT * FROM cadpessoa where cpf LIKE '%"+self.cpfentry.get()+"%' AND nome LIKE'%"+self.nomeentry.get()+"%' AND tipopessoa LIKE'%"+self.status.get()+"%' order by id"
            self.lista = self.filtre(listaBanco)
            for item in self.lista:
                self.tabela.insert('','end', values=(item[0],item[1],item[2],item[3],item[4], item[6]))

    def filtre(self, listaBanco):
        banco = sqlite3.connect('C:\\Users\\rafael\\Desktop\\Projetos\\TopicosLinguagemdeProgramação\\DataBase.db')
        cursor=banco.cursor()
        cursor.execute(listaBanco)
        res=cursor.fetchall()
        return res

    def frames(self):
        self.nometela= Label (self.janela_i)
        self.nometela.config(text= 'Gerenciador',font= ('inter', 33, 'bold'),bg=cor, fg='white')
        self.nometela.pack(pady=50)

        self.frameprin=Frame(self.janela_i, width=550, height=300, bg=cor)
        self.frameprin.place(x=380, y=150)

        nomelbl=Label(self.frameprin,width = 9, height = 2,text='Nome:', font=fonte, bg=cor, fg='white' )
        nomelbl.place(x=21,y=0)
        self.nomeentry= Entry(self.frameprin,width=40, font=("georgia",11))
        self.nomeentry.place(x=130, y= 17)
        self.cpflbl=Label(self.frameprin,width = 9, height = 2,text='CPF:', font=fonte, bg=cor, fg='white' )
        self.cpflbl.place(x=30,y=50)
        self.cpfentry= Entry(self.frameprin,width=40, font=("georgia",11))
        self.cpfentry.place(x=130, y= 67)


        self.situacaolbl=Label(self.frameprin,width = 9, height = 2,text='Situação:', font=fonte, bg=cor, fg='white' )
        self.situacaolbl.place(x=10,y=100)
        self.status=ttk.Combobox(self.frameprin, width= 14,font=("georgia",11))
        self.status.set('Selecionar')
        self.status['values'] = ['Todos','Aprovado', 'Negado' , 'Analise'] 
        self.status['state'] = 'readonly'
        self.status.place(x=130, y=120)

        #self.pesquisarbutton=Button(self.frameprin, text="Pesquisar", font=("georgia",11), command=self.pesquisarPS)
        #self.pesquisarbutton.place(x=130,y=170)

    
    
    def Criar_tabelaAdo(self):
        def teste_fun(event):
            print("muito bom")
        #item=ttk.Treeview.bind
        #self.tabela.bind
        self.tabela=ttk.Treeview(self.janela_i, show='headings',height=10, selectmode='browse', takefocus=True)
        self.tabela.place(x=370, y=370, width=700)
        self.tabela.bind("<Double-1>", teste_fun)

        self.tabela['columns']=('Nome', 'CPF', 'Id Pet', 'Data', 'Id Adoção', 'Situação',)
        self.tabela.column('#0', width=0, stretch=NO)
        self.tabela.column('Nome', anchor=CENTER, width=90)
        self.tabela.column('CPF',anchor=CENTER, width=90)
        self.tabela.column('Id Pet', anchor=CENTER, width=90)
        self.tabela.column('Data', anchor=CENTER, width=90)
        self.tabela.column('Situação', anchor=CENTER, width=90)
        self.tabela.column('Id Adoção', anchor=CENTER, width=90)

        self.tabela.heading('#0', text='', anchor=CENTER)
        self.tabela.heading('Nome', text='Nome', anchor=CENTER)
        self.tabela.heading('CPF', text='CPF', anchor=CENTER)
        self.tabela.heading('Id Pet', text='Id Pet', anchor=CENTER)
        self.tabela.heading('Data', text='Data', anchor=CENTER)
        self.tabela.heading('Situação', text='Situação', anchor=CENTER)
        self.tabela.heading('Id Adoção', text='Id Adoção', anchor=CENTER)

    def Criar_tabelaPS(self):
        self.tabela=ttk.Treeview(self.janela_i, show='headings',height=10, selectmode='browse', takefocus=True)
        self.tabela.place(x=370, y=370, width=700)
        self.tabela['columns']=('Nome', 'CPF', 'E-Mail', 'Telefone', 'Endereço', 'Tipo Pessoa',)
        self.tabela.column('#0', width=0, stretch=NO)
        self.tabela.column('Nome', anchor=CENTER, width=120)
        self.tabela.column('CPF',anchor=CENTER, width=100)
        self.tabela.column('E-Mail', anchor=CENTER, width=120)
        self.tabela.column('Telefone', anchor=CENTER, width=90)
        self.tabela.column('Endereço', anchor=CENTER, width=150)
        self.tabela.column('Tipo Pessoa', anchor=CENTER, width=120)

        self.tabela.heading('#0', text='', anchor=CENTER)
        self.tabela.heading('Nome', text='Nome', anchor=CENTER)
        self.tabela.heading('CPF', text='CPF', anchor=CENTER)
        self.tabela.heading('E-Mail', text='E-Mail', anchor=CENTER)
        self.tabela.heading('Telefone', text='Telefone', anchor=CENTER)
        self.tabela.heading('Endereço', text='Endereço', anchor=CENTER)
        self.tabela.heading('Tipo Pessoa', text='Tipo Pessoa', anchor=CENTER)

     
    import sqlite3

    def conectar(self):
        conn = self.sqlite3.connect('C:\\Users\\rafael\\Desktop\\Projetos\\TopicosLinguagemdeProgramação\\DataBase.db')
        cursor = conn.cursor()
        return conn,cursor

    def InserAtualiADO(self):
        self.tabela.destroy()
        self.Criar_tabelaAdo()
        #self.tabela.delete(*self.tabela.get_children())
        conn,cursor = self.conectar()
        cursor.execute(""" 
                SELECT * FROM adocao  
            """)
        lista = cursor.fetchall()
        conn.close()
        for item in lista:
            self.tabela.insert('','end', values=(item[0],item[1],item[2],item[3],item[5], item[4]))

    def InserAtualiPS(self):
        self.tabela.destroy()
        self.Criar_tabelaPS()
        conn,cursor = self.conectar()
        cursor.execute(""" 
                SELECT * FROM cadpessoa  
            """)
        lista = cursor.fetchall()
        conn.close()
        for item in lista:
            self.tabela.insert('','end', values=(item[0],item[1],item[2],item[3],item[4], item[6]))
           
    def Aprovar (self):
       
        self.txt=self.tabela.focus()
        self.valores=self.tabela.item(self.txt, "values",)
        self.valores=self.valores[4]


        self.conn,self.cursor = self.conectar()
        self.cursor.execute(""" 
                UPDATE adocao SET status='Aprovado' where id = ?
            """, (self.valores,))
        self.conn.commit()
        self.conn.close()
        self.VA()

    def Negar (self):
       
        self.txt=self.tabela.focus()
        self.valores=self.tabela.item(self.txt, "values",)
        self.valores=self.valores[4]

        self.conn,self.cursor = self.conectar()
        self.cursor.execute(""" 
                UPDATE adocao SET status='Negado' where id = ?
            """, (self.valores,))
        self.conn.commit()
        self.conn.close()
        self.VA()

#Tabela_Gerenciar()