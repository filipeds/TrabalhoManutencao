#BasedeDados = Responsavel por conectar com o banco de dados
#sqlite3 = essa importação implementa um banco de dados SQL embutido.

import sqlite3
#Faz a conexão com o banco
conn = sqlite3.connect('UsuariosDados.db')

cursor = conn.cursor()

#Cria a tabela dentro do banco de dados
cursor.execute("""
CREATE TABLE IF NOT EXISTS Usuarios (
    Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL,
    Email TEXT NOT NULL,
    Usuario TEXT NOT NULL,
    Senha TEXT NOT NULL
);
""")
#Notifica se estamos conectados ao banco de dados.
print('Conectado com banco de dados')