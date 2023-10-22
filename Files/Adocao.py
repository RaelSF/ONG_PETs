from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog
import BancoDados 
from Tabela_Pets import *

cor='#05264b'
fonte = ("georgia",17)
fontebotao= ("inter", 18, 'bold')

class Adocao_pet():
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
      self.finaladocao=Button (self.janela_i, text= 'Finalizar',font=fontebotao,width=10, height=1, command=self.Regi_Adocao)
      self.finaladocao.place(x=520, y=650)
      self.cancelar=Button(self.janela_i, text= 'Cancelar',font=fontebotao,width=10, height=1, command=self.sair)
      self.cancelar.place(x=700, y=650)

    def frames (self):
         nometela=Label(self.janela_i)
         nometela.config(text= 'Adoção',font= ('inter', 33, 'bold'),bg=cor, fg='white')
         nometela.pack(pady=50)

         self.frameadocao=Frame(self.janela_i, width=550, height=450, bg=cor)
         self.frameadocao.place(x= 385,y=150)

         adotantelbl=Label(self.frameadocao,width = 9, height = 2,text='Adotante:', font=fonte, bg=cor, fg='white' )
         adotantelbl.place(x=120,y=50)
         self.adotanteentry= Entry(self.frameadocao,width=16, font=("georgia",11))
         self.adotanteentry.place(x=250, y= 67)
         codlbl=Label(self.frameadocao,width = 13, height = 2,text='CPF:', font=fonte, bg=cor, fg='white' )
         codlbl.place(x=120,y=100)
         self.cpfentry= Entry(self.frameadocao,width=16, font=("georgia",11))
         self.cpfentry.place(x=250, y= 117)

         Sele_Petlbl=Label(self.frameadocao,width = 13, height = 2,text='Selecionar Pet:', font=fonte, bg=cor, fg='white' )
         Sele_Petlbl.place(x=60,y=200)
         self.Sele_Petentry= Button(self.frameadocao,width=16, font=("georgia",11), command=Tabela_Pets)
         self.Sele_Petentry.place(x=250, y= 217)
    
         


         self.CheckVar1=IntVar() 

         statuslbl=Label(self.frameadocao,width = 13, height = 2,text='Status:', font=fonte, bg=cor, fg='white' )
         statuslbl.place(x=100,y=250)

         status_neg=Radiobutton(self.frameadocao, width = 9, height = 1,text='Negado', font=fonte, bg=cor, fg='white',activebackground=cor, cursor='arrow', variable = self.CheckVar1,value=1, selectcolor=cor, bd=4)
         status_neg.place(x=230, y= 260)
         status_apr=Radiobutton(self.frameadocao, width = 9, height = 1,text='Aprovado', font=fonte, bg=cor, fg='white',activebackground=cor, cursor='arrow', variable = self.CheckVar1, value=2 , selectcolor=cor, bd=4)
         status_apr.place(x=240, y= 290)
         status_ana=Radiobutton(self.frameadocao, width = 9, height = 1,text='Analise', font=fonte, bg=cor, fg='white',activebackground=cor, cursor='arrow', variable = self.CheckVar1, value=3, selectcolor=cor, bd=4)
         status_ana.place(x=230, y= 320)

         datalbl=Label(self.frameadocao,width = 13, height = 2,text='Data da Visita:', font=fonte, bg=cor, fg='white' )
         datalbl.place(x=60,y=350)

         self.dia=ttk.Combobox(self.frameadocao, width= 14,font=("georgia",11))
         self.dia['values'] = ['01', '02','03', '04','05', '06','07', '08','09', '10','11', '12','13', '14','15', '16','17', '18','19', '20','21', '22','23', '24','25', '26','27', '28','29', '30','31',] 
         self.dia['state'] = 'readonly'
         self.dia.place(x=250, y=370, width=45)
         self.mes=ttk.Combobox(self.frameadocao, width= 14,font=("georgia",11))
         self.mes['values'] = ['01', '02','03', '04','05', '06','07', '08','09', '10','11', '12'] 
         self.mes['state'] = 'readonly'
         self.mes.place(x=320, y=370, width=45)
         self.ano=ttk.Combobox(self.frameadocao, width= 14,font=("georgia",11))
         self.ano['values'] = ['2022', '2023','2024'] 
         self.ano['state'] = 'readonly'
         self.ano.place(x=390, y=370, width=60)
    
    def situacao (self):
        TxtP = ""
        if (self.CheckVar1.get() == 1):
            TxtP="Negado "
        if (self.CheckVar1.get() == 2):
            TxtP="Aprovado "
        if (self.CheckVar1.get() == 3):
            TxtP="Analise "
        return TxtP
   

    def Regi_Adocao(self):
        nome_ado=self.adotanteentry.get()
        cpf=self.cpfentry.get()
        id_pet=self.Sele_Petentry
        data_visi=self.dia.get() 
        mes_visi = self.mes.get()
        ano_visi = self.ano.get()
        data_completa = data_visi + "/" + mes_visi + "/" + ano_visi
        status_P=self.situacao()
            

        txt = ""
        if nome_ado == "":
           txt =  txt + "Falta informa o nome do Adotante!\n"
        if cpf == "":
           txt =  txt + "Falta informa o CPF do Adotante!\n"
        if id_pet == "":
           txt =  txt + "Falta escolher o Pet!\n"
        if status_P == "":
            txt = txt + "Falta selecionar a Situação do Adotante!\n"
            
        if txt != "":
            messagebox.showerror(title="Erro ao solicitar adoção", message=txt)

        else:
            BancoDados.cursor.execute ('SELECT * FROM cadpessoa  WHERE (nome = ? AND cpf = ?) ',(nome_ado,cpf))
            Verifypessoa = BancoDados.cursor.fetchone()
            print(cpf)
            print(nome_ado)
            try:
                if  nome_ado in Verifypessoa and int(cpf)  in Verifypessoa:
                     BancoDados.cursor.execute("""INSERT INTO adocao(nome_adotante,cpf,id_pet,data,status) VALUES(?,?,?,?,?) """,(nome_ado, cpf, cpf,  data_completa, self.status_P,))
                     BancoDados.banco.commit()
                     messagebox.showinfo(title="Sucesso!", message="Adoção Cadastrada com Sucesso!")
                     self.sair()
            except:
                     messagebox.showinfo(title="Info", message="Adotante não cadastrado!")
           
    def sair(self):
        self.janela_i.destroy()
        
#Adocao_pet()