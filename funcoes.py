import database
from datetime import datetime
import sqlite3


class Funcoes:
    def __init__(self, db_path = 'tarefas.db'):
        self.db_path = db_path
        database.criar_banco_de_dados()
        
    def criar_tarefa(nome_tarefa, descricao, prazo, id_projeto=None):
        conn, cursor = database.conectar_bd()
        cursor.execute('''INSERT INTO Tarefas (nome_tarefa, descricao, prazo, id_projeto) VALUES (?, ?, ?, ?)''', (nome_tarefa, descricao, prazo, id_projeto))
        conn.commit()
        conn.close()
        
    def criar_projeto(nome_projeto, descricao, prazo):
        conn, cursor =database.conectar_bd()
        cursor.execute('''INSERT INTO Projetos (nome_projeto, descricao, prazo) VALUES (?, ?, ?)''', (nome_projeto, descricao, prazo))
        conn.commit()
        conn.close()
    
    def editar_tarefa(id, nome_tarefa, descricao, prazo, id_projeto=None):
        conn, cursor = database.conectar_bd()
        cursor.execute('''
            UPDATE Tarefas
            SET nome_tarefa = ?, descricao = ?, prazo = ?, id_projeto = ?
            WHERE id = ?
        ''', (nome_tarefa, descricao, prazo, id_projeto, id))
        conn.commit()
        conn.close()
    
    def editar_projeto(id, nome_projeto, descricao, prazo):
        conn, cursor = database.conectar_bd()
        cursor.execute('''
            UPDATE Projetos
            SET nome_projeto = ?, descricao = ?, prazo = ?
            WHERE id = ?
        ''', (nome_projeto, descricao, prazo, id))
        conn.commit()
        conn.close()   

    def excluir_tarefa(id):
        conn, cursor = database.conectar_bd()
        cursor.execute('DELETE FROM Tarefas WHERE id = ?', (id,))
        conn.commit()
        conn.close()
    
    def excluir_projeto(id):
        conn, cursor = database.conectar_bd()
        cursor.execute('DELETE FROM Tarefas WHERE id_projeto = ?', (id,))
        cursor.execute('DELETE FROM Projetos WHERE id = ?', (id,))
        conn.commit()
        conn.close()

    def marcar_tarefa_concluida(id):
        conn, cursor = database.conectar_bd()
        concluido = datetime.now().strftime("%Y-%m-%d%H:%M:%S")
        cursor.execute('UPDATE Tarefas SET concluido = ? WHERE id = ?', (concluido, id))
        conn.commit()
        conn.close()
    
    def marcar_projeto_concluido(id):
        conn, cursor = database.conectar_bd()
        concluido = datetime.now().strftime("%Y-%m-%d%H:%M:%S")
        cursor.execute('UPDATE Projetos SET concluido = ? WHERE id = ?', (concluido, id))
        conn.commit()
        conn.close()
    
    def marcar_tarefa_como_importante(id):
        conn, cursor = database.conectar_bd()
        cursor.execute('UPDATE Tarefas SET importante = 1 WHERE id = ?', (id,))
        conn.commit()
        conn.close()
   
    def marcar_projeto_como_importante(id):
        conn, cursor = database.conectar_bd()
        cursor.execute('UPDATE Projeto SET importante = 1 WHERE id = ?', (id,))
        conn.commit()
        conn.close()
   
    def listar_tarefas():
        conn, cursor = database.conectar_bd()
        cursor.execute('SELECT * FROM Tarefas')
        tarefas = cursor.fetchall()
        conn.close()
        return tarefas

    def listar_projetos():
        conn, cursor = database.conectar_bd()
        cursor.execute('SELECT * FROM Projetos')
        projetos = cursor.fetchall()
        conn.close()
        return projetos

    def filtrar_tarefas_concluidas():
        conn, cursor = database.conectar_bd()
        cursor.execute('SELECT * FROM Tarefas WHERE concluido IS NOT NULL')
        tarefas_concluidas = cursor.fetchall()
        conn.close()
        return tarefas_concluidas

    def filtrar_tarefas_pendentes():
        conn, cursor = database.conectar_bd()
        cursor.execute('SELECT * FROM Tarefas WHERE concluido IS NULL')
        tarefas_pendentes = cursor.fetchall()
        conn.close()
        return tarefas_pendentes

    def filtrar_projetos_concluidos():
        conn, cursor = database.conectar_bd()
        cursor.execute('SELECT * FROM Projetos WHERE concluido IS NOT NULL')
        projetos_concluidos = cursor.fetchall()
        conn.close()
        return projetos_concluidos
    
    
    def filtrar_projetos_pendentes():
        conn, cursor = database.conectar_bd()
        cursor.execute('SELECT * FROM Projetos WHERE concluido IS NULL')
        projetos_pendentes = cursor.fetchall()
        conn.close()
        return projetos_pendentes
