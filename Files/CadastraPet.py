from asyncio import events
from audioop import add
from cProfile import label
from cgitb import text
from ctypes.wintypes import SHORT, SIZE
from dataclasses import dataclass
from datetime import date, datetime
from distutils.cmd import Command
from inspect import Attribute
from msilib.schema import ListBox
from re import T
from textwrap import shorten
from tkinter import*
from tkinter import ttk
from tkinter.tix import ComboBox
from turtle import right
from tkinter.messagebox import showinfo

import tkinter as tk
from datetime import timedelta


janela = Tk()
janela.title("ONG")
janela.geometry("1260x1024")
janela.config(
    bg='dark blue'
)

nome= Label (janela)
nome.config(
    text= 'Cadastro Pet',
    font= ('inter', 30, 'bold'),
    bg='dark blue',
    fg='white'
)
nome.pack(pady=20)

frameda=Frame(janela)
frameda.pack(pady=5)
lbl=Label(frameda)
lbl.config(
    fg='white',
    bg='blue',
    text = 'Nome:',
    width= 15,
    height= 1,
    font=('inter', 17, 'bold'),
)
lbl.pack(side=LEFT)

caixa = Entry(frameda)
caixa.config(
    width= 13,
    bg='silver',
    font=('verdana', 15),
)
caixa.pack(side=RIGHT)

frameda=Frame(janela)
frameda.pack(pady=5)
lbl=Label(frameda)
lbl.config(
    fg='white',
    bg='blue',
    text = 'Raça:',
    width= 15,
    height= 1,
    font=('inter', 17, 'bold'),
)
lbl.pack(side=LEFT)

caixa = Entry(frameda)
caixa.config(
    width= 13,
    bg='silver',
    font=('verdana', 15),
)
caixa.pack(side=RIGHT)

frameda=Frame(janela)
frameda.pack(pady=5)
lbl=Label(frameda)
lbl.config(
    fg='white',
    bg='blue',
    text = 'Gênero:',
    width= 15,
    height= 1,
    font=('inter', 17, 'bold'),
)
lbl.pack(side=LEFT)

caixa = Entry(frameda)
caixa.config(
    width= 13,
    bg='silver',
    font=('verdana', 15),
)
caixa.pack(side=RIGHT)

frameda=Frame(janela)
frameda.pack(pady=5)
lbl=Label(frameda)
lbl.config(
    fg='white',
    bg='blue',
    text = 'Idade:',
    width= 15,
    height= 1,
    font=('inter', 17, 'bold'),
)
lbl.pack(side=LEFT)

caixa = Entry(frameda)
caixa.config(
    width= 13,
    bg='silver',
    font=('verdana', 15),
)
#caixa.insert(0,'nome')
caixa.pack(side=RIGHT)

frameda=Frame(janela)
frameda.pack(pady=5)
lbl=Label(frameda)
lbl.config(
    fg='white',
    bg='blue',
    text = 'Status:',
    width= 15,
    height= 1,
    font=('inter', 17, 'bold'),
)
lbl.pack(side=LEFT)

sele = ttk.Combobox(frameda)
sele.config(
    width= 12,
    font=('verdana', 15),
)
sele.set('1')
sele['values'] = ['1','2','3']
sele.pack(side=RIGHT)

frameda=Frame(janela)
frameda.pack(pady=5)
lbl=Label(frameda)
lbl.config(
    fg='white',
    bg='blue',
    text = 'Imagem:',
    width= 15,
    height= 1,
    font=('inter', 17, 'bold'),
)
lbl.pack(side=LEFT)

caixa = Button (frameda)
caixa.config(
    width= 20,
    height= 1,
    text='Upload',
    bg='silver',
)
caixa.pack(side=RIGHT)

botao1= Button(janela)
botao1.configure(
   text= 'Registrar',
   font=("inter", 15, 'bold'), 
   command=quit,
)
botao1.pack(side=BOTTOM)


janela.mainloop()