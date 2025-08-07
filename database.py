import sqlite3

def conectar_bd():
    conn = sqlite3.connect('tarefas.db')
    cursor = conn.cursor()
    return conn, cursor

def criar_tabela_tarefas():
    conn, cursor = conectar_bd()
    cursor.execute(''' CREATE TABLE IF NOT EXISTS Tarefas (
        id INTENGER PRIMARY KEY,
        nome_tarefa TEXT NOT NULL,
        descricao TEXT,
        prazo DATE,
        criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        concluido TIMESTAMP,
        importante INTENGER,
        id_projeto INTENGER,
        FOREIGN KEY (id_projeto) REFERENCES Projetos (id));''' )
    
    conn.commit()
    conn.close()
    
    
def criar_tabela_projetos():
    conn, cursor = conectar_bd()
    cursor.execute(''' CREATE TABLE IF NOT EXISTS Projetos (
        id INTENGER PRIMARY KEY,
        nome_projeto TEXT NOT NULL,
        descricao TEXT,
        prazo DATE,
        criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        concluido TIMESTAMP,
        importante INTENGER);''')
    
    conn.commit()
    conn.close()
    
def criar_banco_de_dados():
    criar_tabela_tarefas()
    criar_tabela_projetos()
    
criar_banco_de_dados()