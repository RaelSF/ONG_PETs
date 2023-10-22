from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog
import BancoDados 
import sqlite3

cor='#05264b'
fonte = ("georgia",17)
fontebotao= ("inter", 18, 'bold')

#classe da tela inicial
class Tabela_Pets():
    def __init__(self):

        self.janela_i = Tk()
        self.Tela()
        self.frames()
        self.janela_i.mainloop()
        
#configuracoes da tela
    def Tela (self):
        self.janela_i.title("ONG")
        self.janela_i.geometry("1260x1024")
        self.janela_i.configure(bg=cor)
        self.Criar_tabela()
        self.InserAtuali()
        
#frames da tela
    def frames (self):
        
        self.nometela= Label (self.janela_i)
        self.nometela.config(text= 'Selecionar Pet',font= ('inter', 33, 'bold'),bg=cor, fg='white')
        self.nometela.pack(pady=50)

        self.frameprin= Frame(self.janela_i, bg=cor)
        self.frameprin.place(x= 380,y=150, width=650, height=200)
        

        nomelbl=Label(self.frameprin,width = 9, height = 2,text='Nome:', font=fonte, bg=cor, fg='white' )
        nomelbl.place(x=21,y=0)
        self.nomeentry= Entry(self.frameprin,width=40, font=("georgia",11))
        self.nomeentry.place(x=130, y= 17)
        self.IDlbl=Label(self.frameprin,width = 9, height = 2,text='ID:', font=fonte, bg=cor, fg='white' )
        self.IDlbl.place(x=30,y=50)
        self.IDentry= Entry(self.frameprin,width=40, font=("georgia",11))
        self.IDentry.place(x=130, y= 67)


        situacaolbl=Label(self.frameprin,width = 9, height = 2,text='Situação:', font=fonte, bg=cor, fg='white' )
        situacaolbl.place(x=10,y=100)
        self.status=ttk.Combobox(self.frameprin, width= 14,font=("georgia",11))
        self.status.set('Selecionar')
        self.status['values'] = ['Disponivel', 'Não Disponivel'] 
        self.status['state'] = 'readonly'
        self.status.place(x=130, y=120)

        self.pesquisarbutton=Button(self.frameprin, text="Pesquisar", font=("georgia",11), command=self.pesquisar)
        self.pesquisarbutton.place(x=130,y=170)

    def pesquisar (self):
        self.tabela.delete(*self.tabela.get_children())
        if self.status.get() != "Selecionar":
            self.listaBanco="SELECT * FROM cadpet where nome LIKE '%"+self.nomeentry.get()+"%' and id LIKE '%"+self.IDentry.get()+"%' and status LIKE '"+self.status.get()+"' order by id"
            lista = self.filtre(self.listaBanco)
        else:
            self.listaBanco="SELECT * FROM cadpet where nome LIKE '%"+self.nomeentry.get()+"%' and id LIKE '%"+self.IDentry.get()+"%' order by id"
            lista = self.filtre(self.listaBanco)
        
        for item in lista:
            self.tabela.insert('','end', values=(item[0],item[1],item[2],item[3],item[4], item[5]))

    def filtre(self, listaBanco):
        banco = sqlite3.connect('C:\\Users\\rafael\\Desktop\\Projetos\\TopicosLinguagemdeProgramação\\DataBase.db')
        cursor=banco.cursor()
        cursor.execute(listaBanco)
        res=cursor.fetchall()
        return res

    def Criar_tabela(self):
        self.tabela=ttk.Treeview(self.janela_i, show='headings',height=10,)
        self.tabela.place(x=450, y=370)
        self.tabela['columns']=('ID', 'Nome', 'Raça', 'Genero', 'Idade', 'Situação',)
        self.tabela.column('#0', width=0, stretch=NO)
        self.tabela.column('ID', anchor=CENTER, width=90)
        self.tabela.column('Nome',anchor=CENTER, width=90)
        self.tabela.column('Raça', anchor=CENTER, width=90)
        self.tabela.column('Genero', anchor=CENTER, width=90)
        self.tabela.column('Idade', anchor=CENTER, width=90)
        self.tabela.column('Situação', anchor=CENTER, width=90)
    
        self.tabela.heading('#0', text='', anchor=CENTER)
        self.tabela.heading('ID', text='Id', anchor=CENTER)
        self.tabela.heading('Nome', text='Nome', anchor=CENTER)
        self.tabela.heading('Raça', text='Raça', anchor=CENTER)
        self.tabela.heading('Genero', text='Genero', anchor=CENTER)
        self.tabela.heading('Idade', text='Idade', anchor=CENTER)
        self.tabela.heading('Situação', text='Situação', anchor=CENTER)

    import sqlite3

    def conectar(self):
        conn = self.sqlite3.connect('C:\\Users\\rafael\\Desktop\\Projetos\\TopicosLinguagemdeProgramação\\DataBase.db')
        cursor = conn.cursor()
        return conn,cursor

    def InserAtuali(self):
        self.tabela.destroy()
        self.Criar_tabela()
        #self.tabela.delete(*self.tabela.get_children())
        conn,cursor = self.conectar()
        cursor.execute(""" 
                SELECT * FROM cadpet  
            """)
        lista = cursor.fetchall()
        conn.close()
        for item in lista:
            self.tabela.insert('','end', values=(item[0],item[1],item[2],item[3],item[4], item[5]))

    



#Tabela_Pets()