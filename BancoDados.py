import sqlite3

banco = sqlite3.connect('DataBase.db')

cursor=banco.cursor()

#cursor.execute("CREATE TABLE IF NOT EXISTS cadpessoa (nome text,cpf text,email text,telefone text,rua text,numero text,bairro text,cidade text)")

