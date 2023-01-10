from PySide6.QtCore import Qt, QCoreApplication, QPropertyAnimation, QEasingCurve
from PySide6.QtWidgets import (QApplication, QMainWindow)
from PySide6.QtGui import QIcon
from ui_cadastroV2 import Ui_MainWindow
import sys


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
         super(MainWindow, self).__init__()
         self.setupUi(self)
         self.setWindowTitle("ImovPy - Sistema de cadastro de imóveis")
         appIcon = QIcon(u"")
         self.setWindowIcon(appIcon)
         
         self.btn_toggle.clicked.connect(self.leftMenu)
        
        

### TOGGLE BUTTON ### 
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
#####################

### SYSTEM PAGES ###
        self.btn_home.clicked.connect(lambda: self.tabWidget_content.setCurrentWidget(self.page_home))
        self.btn_cadastrar.clicked.connect(lambda: self.tabWidget_content.setCurrentWidget(self.page_cadastrar))
        self.btn_contatos.clicked.connect(lambda: self.tabWidget_content.setCurrentWidget(self.page_contatos))
        self.btn_sobre.clicked.connect(lambda: self.tabWidget_content.setCurrentWidget(self.page_sobre))
#####################         
         
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()