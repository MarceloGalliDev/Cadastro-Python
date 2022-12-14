from PySide6.QtCore import QPropertyAnimation, QEasingCurve
from PySide6.QtWidgets import (QApplication, QMainWindow, QMessageBox, QTableWidgetItem)
from PySide6.QtGui import QIcon
from ui_cadastroV2 import Ui_MainWindow
import sys
from ui_functions import consulta_cnpj
from database import Data_base


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("ImovPy - Sistema de cadastro de imóveis")
        appIcon = QIcon(u"")
        self.setWindowIcon(appIcon)
         
        ### TOGGLE BUTTON ### 
        self.btn_toggle.clicked.connect(self.leftMenu)
        #####################
        
        ### SYSTEM PAGES ###
        self.btn_home.clicked.connect(lambda: self.tabWidget_content.setCurrentWidget(self.page_home))
        self.btn_cadastrar.clicked.connect(lambda: self.tabWidget_content.setCurrentWidget(self.page_cadastrar))
        self.btn_contatos.clicked.connect(lambda: self.tabWidget_content.setCurrentWidget(self.page_contatos))
        self.btn_sobre.clicked.connect(lambda: self.tabWidget_content.setCurrentWidget(self.page_sobre))
        ##################### 
        
        ### AUTO COMPLETE ###
        self.lineEdit_cnpj.editingFinished.connect(self.consult_api)
        #####################
        
        ### BUTTONS ###
        self.btn_cadastrar_2.clicked.connect(self.cadastrar_empresas)
        ###############  

        ### FUNCTIONS SEARCH ###
        self.buscar_empresas()
        ########################
    
    ### MENU ANIMATION ###    
    def leftMenu(self):
        width = self.frame_main_menu.width()
        
        if width == 0:
            newWidth = 200
        else:
            newWidth = 0
        
        self.animation = QPropertyAnimation(self.frame_main_menu, b"maximumWidth")
        self.animation.setDuration(500)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()
    ######################

    ### API CONSULTS ###
    def consult_api(self):
        campos = consulta_cnpj(self.lineEdit_cnpj.text())
        
        self.lineEdit_razao_social.setText(campos[0])
        self.lineEdit_logradouro.setText(campos[1])
        self.lineEdit_numero.setText(campos[2])
        self.lineEdit_complemento.setText(campos[3])
        self.lineEdit_bairro.setText(campos[4])
        self.lineEdit_municipio.setText(campos[5])
        self.lineEdit_uf.setText(campos[6])
        self.lineEdit_cep.setText(campos[7].replace('.', '').replace('-', ''))
        self.lineEdit_telefone.setText(campos[8].replace('(', '').replace('-', '').replace(')',''))
        self.lineEdit_email.setText(campos[9])    
    ####################
         
    ### CADASTRAR ###
    def cadastrar_empresas(self):
        db = Data_base()
        db.connect()
        
        fullDataSet = (
            self.lineEdit_cnpj.text(),
            self.lineEdit_razao_social.text(),
            self.lineEdit_logradouro.text(),
            self.lineEdit_numero.text(),
            self.lineEdit_complemento.text(),
            self.lineEdit_bairro.text(),
            self.lineEdit_municipio.text(),
            self.lineEdit_uf.text(),
            self.lineEdit_cep.text(),
            self.lineEdit_telefone.text().strip(),
            self.lineEdit_email.text()
        )

        resp = db.register_company(fullDataSet)
        if resp == "OK":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Cadastro Realizado")
            msg.setText("Cadastro realizado com sucesso!")
            msg.exec()
            db.close_connection()
            return
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Erro")
            msg.setText("Erro ao cadastrar, verifique as informações!")
            msg.exec()
            db.close_connection()
            return
    #################
    
    ### BUSCAR ###
    def buscar_empresas(self):
        db = Data_base()
        db.connect()
        result = db.select_all_companies()
        
        print(result)
        
        self.tb_company.clearContents()
        self.tb_company.setRowCount(len(result))
        
        for row, text in enumerate(result):
            for column, data, in enumerate(text):
                self.tb_company.setItem(row, column, QTableWidgetItem(str(data)))
        
        db.close_connection()
        
    ##############    
        
if __name__ == "__main__":
    
    db = Data_base()
    db.connect()
    db.create_table_company()
    db.close_connection()
    
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()