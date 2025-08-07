from PyQt5 import QtWidgets
from PyQt5.QtWidgets import  QApplication, QMainWindow, QListWidgetItem, QDialog
from PyQt5.uic import loadUi
import sys

class Edit(QDialog):
    def __init__(self):
        super(Edit, self).__init__()
        loadUi("editar.ui", self)
        self.cancelar_pushButton.clicked.connect(self.cancelar)
        
    def cancelar(self):
        self.close()

class Edit_pr(QDialog):
    def __init__(self):
        super(Edit_pr, self).__init__()
        loadUi("editar_pr.ui", self)
        self.cancelar_prpushButton.clicked.connect(self.cancelar)
        
    def cancelar(self):
        self.close()
        
        
        