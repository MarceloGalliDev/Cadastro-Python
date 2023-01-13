from PySide6.QtCore import QPropertyAnimation, QEasingCurve
from PySide6.QtWidgets import (QApplication, QMainWindow, QMessageBox, QTableWidgetItem)
from PySide6.QtGui import QIcon
from ui_cadastroV2 import Ui_MainWindow
import sys
from ui_functions import consulta_cnpj
from database import Data_base
import pandas as pd
import sqlite3


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
        self.btn_alterar.clicked.connect(self.atualizar_empresas)
        self.btn_excluir.clicked.connect(self.delete_empresas)
        self.pushButton_limpar.clicked.connect(self.limpar_form)
        self.btn_gerar_excel.clicked.connect(self.gerar_excel)
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

        self.buscar_empresas()
                        
        if resp == "OK":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Cadastro")
            msg.setText("Cadastro realizado com sucesso!")
            msg.exec()           
            db.close_connection()
            
            self.lineEdit_cnpj.clear(),
            self.lineEdit_razao_social.clear(),
            self.lineEdit_logradouro.clear(),
            self.lineEdit_numero.clear(),
            self.lineEdit_complemento.clear(),
            self.lineEdit_bairro.clear(),
            self.lineEdit_municipio.clear(),
            self.lineEdit_uf.clear(),
            self.lineEdit_cep.clear(),
            self.lineEdit_telefone.clear(),
            self.lineEdit_email.clear()  
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
    
    ### LIMPAR ###
    def limpar_form(self):
        self.lineEdit_cnpj.clear()        
        self.lineEdit_razao_social.clear(),
        self.lineEdit_logradouro.clear(),
        self.lineEdit_numero.clear(),
        self.lineEdit_complemento.clear(),
        self.lineEdit_bairro.clear(),
        self.lineEdit_municipio.clear(),
        self.lineEdit_uf.clear(),
        self.lineEdit_cep.clear(),
        self.lineEdit_telefone.clear(),
        self.lineEdit_email.clear()  
    ##############
    
    ### BUSCAR ###
    def buscar_empresas(self):
        db = Data_base()
        db.connect()
        result = db.select_all_companies()
              
        self.tb_company.clearContents()
        self.tb_company.setRowCount(len(result))
        
        for row, text in enumerate(result):
            for column, data, in enumerate(text):
                self.tb_company.setItem(row, column, QTableWidgetItem(str(data)))
        
        db.close_connection()
    ##############  
    
    ### UPDATE ###
    def atualizar_empresas(self):
        dados = []
        update_dados = []
        
        for row in range(self.tb_company.rowCount()):
            for column in range(self.tb_company.columnCount()):
                dados.append(self.tb_company.item(row, column).text())
                
            update_dados.append(dados)
            dados = []
            
        db = Data_base()
        db.connect()
        
        for emp in update_dados:
            db.update_company(tuple(emp))
            
        db.close_connection()
               
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Atualização de dados")
        msg.setText("Atualização realizada com sucesso!")
        msg.exec()
        
        self.tb_company.reset()
        self.buscar_empresas()
    ##############  
    
    ### DELETE ###
    def delete_empresas(self):
        db = Data_base()
        db.connect()
        
        msg = QMessageBox()
        msg.setWindowTitle("Excluir")
        msg.setText("Este registro será excluído!")
        msg.setInformativeText("Você tem certeza que deseja excluir esse registro?")
        msg.setStandardButtons(QMessageBox.No | QMessageBox.Yes)
        resp = msg.exec()
        
        if resp == QMessageBox.Yes:
            cnpj = self.tb_company.selectionModel().currentIndex().siblingAtColumn(0).data()
            result = db.delete_companies(cnpj)
            self.buscar_empresas()
            
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Excluir")
            msg.setText(result)
            msg.exec()
            
            
            db.close_connection()
        
        db.close_connection()
    ##############
    
    ### GERAR EXCEL ###
    def gerar_excel(self):
        dados = []
        all_dados = []
        
        for row in range(self.tb_company.rowCount()):
            for column in range(self.tb_company.columnCount()):
                dados.append(self.tb_company.item(row, column).text())
        
            all_dados.append(dados)
            dados = []

        columns = ['CNPJ', 'RAZAO_SOCIAL', 'LOGRADOURO','NUMERO', 'COMPLEMENTO', 'BAIRRO', 'MUNICIPIO', 'UF', 'CEP', 'TELEFONE', 'EMAIL']
        
        empresas = pd.DataFrame(all_dados, columns=columns)
        empresas.to_excel("Empresas.xlsx", sheet_name="empresas", index=False)
        
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Exccel")
        msg.setText("Relatório excel gerado com sucesso!")
        msg.exec()      
        
    def gerar_excel_2(self):
        cnx = sqlite3.connect("system.db")
        
        empresas = pd.read_sql_query("""SELECT * FROM Empresas""", cnx) 
        empresas.to_excel("Empresas.xlsx", sheet_name="empresas", index=False)
        
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Exccel")
        msg.setText("Relatório excel gerado com sucesso!")
        msg.exec()                  
    ###################

if __name__ == "__main__":
    
    db = Data_base()
    db.connect()
    db.create_table_company()
    db.close_connection()
    
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()