from PyQt5 import QtWidgets
from PyQt5.QtWidgets import  QApplication, QMainWindow, QListWidgetItem, QDialog
from PyQt5.uic import loadUi
import sys
import sqlite3

class AddDialog(QtWidgets.QDialog):
    
    def __init__(self):
        super(AddDialog, self).__init__()
        loadUi("adicionar.ui", self)
        
        self.guardarButton.clicked.connect(self.adicionar_tarefa)
        self.cancelarButton.clicked.connect(self.cancelar)
        
        
        conn = sqlite3.connect('tarefas.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id FROM Projetos')
        projetos = cursor.fetchall()
        for projeto in projetos:
            self.comboBox.addItem(str(projeto[0]))
            conn.close()
            
    def adicionar_tarefa(self):
        nome_tarefa = self.nomelineEdit.text()
        descricao =self.descricaolineEdit.text()
        prazo = None
        
        if not self.prazocheckBox.isChecked():
            prazo = self.calendarWidget.selectedDate().toPyDate().strftime('%Y-%m-%d')
            id_projeto = None
            
            if self.comboBox.currentText():
                id_projeto = self.comboBox.currentText()
                
                try:
                    conn = sqlite3.connect('tarefas.db')
                    cursor = conn.cursor()
                
                    if prazo and id_projeto:
                        cursor.execute('''INSERT INTO Tarefas (nome_tarefa, descricao, prazo, id_projeto) VALUES (?, ?, ?, ?)''', (nome_tarefa, descricao, prazo, id_projeto))
                    
                    elif prazo and not id_projeto:
                        cursor.execute('''INSERT INTO Tarefas (nome_tarefa, descricao, prazo) VALUES (?, ?, ?)''', (nome_tarefa, descricao, prazo))
                        
                    else:
                        if id_projeto:
                            cursor.execute('''INSERT INTO Tarefas (nome_tarefa, descricao, id_projeto) VALUES (?, ?, ?)''', (nome_tarefa, descricao, id_projeto))  
                    conn.commit()
                    conn.close()
                    self.close()
                except sqlite3.Error as e:
                    print(f"Erro ao salvar dados: {e}")
               
    def cancelar(self):
        self.close()
        
class AddDialog_pr(QtWidgets.QDialog):
    
    def __init__(self):
        super(AddDialog_pr, self).__init__()
        loadUi("adicionar_pr.ui", self)
        
        self.guardar_pushButton.clicked.connect(self.adicionar_projeto)
        self.cancelar_pushButton.clicked.connect(self.cancelar)
        
    def adicionar_projeto(self):
        novo_projeto = self.nome_prlineEdit.text()
        descricao = self.descricao_prlineEdit.text()
        prazo = None
        
        if not self.semprazo_checkBox.isChecked():
            prazo = self.prazo_calendarWidget.selectedDate().toPyDate().strftime('%Y-%m-%d')
            try:
                conn = sqlite3.connect("tarefas.db")
                cursor = conn.cursor()
                cursor.execute('''INSERT INTO Projetos (nome_projeto, descricao, prazo) VALUES (?, ?, ?)''', (novo_projeto, descricao, prazo))
                conn.commit()
                conn.close()
                self.close()
                
            except sqlite3.Error as e:
                print(f"Erro ao salvar dados: {e}")
                
                
    def cancelar(self):
        self.close()    
        
        
'''if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = AddDialog()
    mainWin.show()
    sys.exit(app.exec_())'''