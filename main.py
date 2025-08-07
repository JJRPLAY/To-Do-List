from PyQt5 import QtWidgets
from PyQt5.QtWidgets import  QApplication, QMainWindow, QTableWidgetItem
from PyQt5.uic import loadUi
import sys
import adicionar
import editar
from funcoes import Funcoes




class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("window.ui", self)
        
        self.db = Funcoes()
        
        self.criar_button.clicked.connect(self.abrir_adicionar_tarefas)
        self.criar_pr_button.clicked.connect(self.abrir_adicionar_projeto)
        self.editar_button.clicked.connect(self.editar_tarefas)
        self.editar_pr_button.clicked.connect(self.editar_projetos)
        #self.excluir_button.clicked.conncet(self.excluir_tarefas)
        #self.excluir_pr_button.clicked.connect(self.excluir_projetos)
        self.sair_button.clicked.connect(self.sair)
        self.sair_pr_button.clicked.connect(self.sair2)
        

    def abrir_adicionar_tarefas(self):
        dialog = adicionar.AddDialog()
        dialog.exec_()
        
    def abrir_adicionar_projeto(self):
        dialog = adicionar.AddDialog_pr()
        dialog.exec_()
    
    def editar_tarefas(self):
        dialog = editar.Edit()
        dialog.exec_()
        
    def editar_projetos(self):
        dialog = editar.Edit_pr()
        dialog.exec_()
        
    '''def excuir_tarefas(self):
        dialog =
        dialog.exec_()
    
    def excluir_projetos(self):
        dialog =
        dialog.exec_()'''
        
    def sair(self):
        self.close()
        sys.exit()
    
    def sair2(self):
        self.close()
        sys.exit()
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())