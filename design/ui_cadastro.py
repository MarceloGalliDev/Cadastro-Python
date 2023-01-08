# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cadastro.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTabWidget, QTableWidget, QTableWidgetItem, QToolBox,
    QVBoxLayout, QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1164, 783)
        MainWindow.setStyleSheet(u"background-color: rgb(9, 9, 9);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{\n"
"	border:none;\n"
"}\n"
"\n"
"QLabel{\n"
"	color:rgb(255, 255, 255);\n"
"}")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 9, 0, 0)
        self.frame_aside_content = QFrame(self.centralwidget)
        self.frame_aside_content.setObjectName(u"frame_aside_content")
        self.frame_aside_content.setMaximumSize(QSize(200, 16777215))
        self.frame_aside_content.setFrameShape(QFrame.StyledPanel)
        self.frame_aside_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_aside_content)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 0, 5)
        self.frame_logo = QFrame(self.frame_aside_content)
        self.frame_logo.setObjectName(u"frame_logo")
        self.frame_logo.setStyleSheet(u"background-color: rgb(63, 63, 63);")
        self.frame_logo.setFrameShape(QFrame.StyledPanel)
        self.frame_logo.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_logo)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.label_logo = QLabel(self.frame_logo)
        self.label_logo.setObjectName(u"label_logo")
        self.label_logo.setStyleSheet(u"background-color: rgb(163, 163, 163);")
        self.label_logo.setAlignment(Qt.AlignCenter)
        self.label_logo.setMargin(3)

        self.horizontalLayout_4.addWidget(self.label_logo)


        self.verticalLayout_2.addWidget(self.frame_logo)

        self.frame_menu = QFrame(self.frame_aside_content)
        self.frame_menu.setObjectName(u"frame_menu")
        self.frame_menu.setMinimumSize(QSize(200, 0))
        self.frame_menu.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(62, 62, 62);\n"
"}\n"
"\n"
"QToolBox::tab{\n"
"	border-radius: 5px;\n"
"	background-color: rgb(162, 162, 162);\n"
"}")
        self.frame_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_menu.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_menu)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(9, 9, 9, 9)
        self.box_menu = QToolBox(self.frame_menu)
        self.box_menu.setObjectName(u"box_menu")
        self.box_menu.setStyleSheet(u"")
        self.box_menu_menu = QWidget()
        self.box_menu_menu.setObjectName(u"box_menu_menu")
        self.box_menu_menu.setGeometry(QRect(0, 0, 182, 641))
        self.box_menu_menu.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(163, 163, 163);\n"
"	border-radius: 5px;\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.box_menu_menu)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.button_home = QPushButton(self.box_menu_menu)
        self.button_home.setObjectName(u"button_home")
        self.button_home.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setPointSize(18)
        self.button_home.setFont(font)
        self.button_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_home.setStyleSheet(u"QPushButton:hover{\n"
"	border-radius: 5px;\n"
"	background-color: rgb(62, 62, 62);\n"
"}\n"
"\n"
"QPushButton{\n"
"	color: rgb(255, 255, 255)\n"
"}")

        self.verticalLayout_4.addWidget(self.button_home)

        self.button_cadastrar = QPushButton(self.box_menu_menu)
        self.button_cadastrar.setObjectName(u"button_cadastrar")
        self.button_cadastrar.setMinimumSize(QSize(0, 30))
        self.button_cadastrar.setFont(font)
        self.button_cadastrar.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_cadastrar.setStyleSheet(u"QPushButton:hover{\n"
"	border-radius: 5px;\n"
"	background-color: rgb(62, 62, 62);\n"
"}\n"
"\n"
"QPushButton{\n"
"	color: rgb(255, 255, 255)\n"
"}\n"
"")

        self.verticalLayout_4.addWidget(self.button_cadastrar)

        self.button_contatos = QPushButton(self.box_menu_menu)
        self.button_contatos.setObjectName(u"button_contatos")
        self.button_contatos.setMinimumSize(QSize(0, 30))
        self.button_contatos.setFont(font)
        self.button_contatos.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_contatos.setStyleSheet(u"QPushButton:hover{\n"
"	border-radius: 5px;\n"
"	background-color: rgb(62, 62, 62);\n"
"}\n"
"\n"
"QPushButton{\n"
"	color: rgb(255, 255, 255)\n"
"}")

        self.verticalLayout_4.addWidget(self.button_contatos)

        self.button_sobre = QPushButton(self.box_menu_menu)
        self.button_sobre.setObjectName(u"button_sobre")
        self.button_sobre.setMinimumSize(QSize(0, 30))
        self.button_sobre.setFont(font)
        self.button_sobre.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_sobre.setStyleSheet(u"QPushButton:hover{\n"
"	border-radius: 5px;\n"
"	background-color: rgb(62, 62, 62);\n"
"}\n"
"\n"
"QPushButton{\n"
"	color: rgb(255, 255, 255)\n"
"}\n"
"")

        self.verticalLayout_4.addWidget(self.button_sobre)

        self.space_vertical = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.space_vertical)

        self.box_menu.addItem(self.box_menu_menu, u"Menu")
        self.button_home.raise_()
        self.button_cadastrar.raise_()
        self.button_contatos.raise_()
        self.button_sobre.raise_()
        self.box_menu_info = QWidget()
        self.box_menu_info.setObjectName(u"box_menu_info")
        self.box_menu_info.setGeometry(QRect(0, 0, 182, 641))
        self.box_menu_info.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(163, 163, 163);\n"
"	border-radius: 5px;\n"
"}")
        self.horizontalLayout_6 = QHBoxLayout(self.box_menu_info)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_info = QLabel(self.box_menu_info)
        self.label_info.setObjectName(u"label_info")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_info.sizePolicy().hasHeightForWidth())
        self.label_info.setSizePolicy(sizePolicy)
        self.label_info.setAlignment(Qt.AlignCenter)
        self.label_info.setWordWrap(True)

        self.horizontalLayout_6.addWidget(self.label_info)

        self.box_menu.addItem(self.box_menu_info, u"Informa\u00e7\u00f5es")

        self.horizontalLayout_5.addWidget(self.box_menu)


        self.verticalLayout_2.addWidget(self.frame_menu)


        self.gridLayout_2.addWidget(self.frame_aside_content, 0, 0, 1, 1)

        self.frame_main_content = QFrame(self.centralwidget)
        self.frame_main_content.setObjectName(u"frame_main_content")
        self.frame_main_content.setFrameShape(QFrame.StyledPanel)
        self.frame_main_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_main_content)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.frame_header = QFrame(self.frame_main_content)
        self.frame_header.setObjectName(u"frame_header")
        self.frame_header.setStyleSheet(u"background-color: rgb(62, 62, 62);")
        self.frame_header.setFrameShape(QFrame.StyledPanel)
        self.frame_header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_header)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.button_toggle = QPushButton(self.frame_header)
        self.button_toggle.setObjectName(u"button_toggle")
        self.button_toggle.setLayoutDirection(Qt.LeftToRight)
        self.button_toggle.setStyleSheet(u"background-color: rgb(62, 62, 62);\n"
"color: rgb(162, 162, 162);")
        icon = QIcon()
        icon.addFile(u":/icons/menu2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_toggle.setIcon(icon)
        self.button_toggle.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.button_toggle, 0, Qt.AlignLeft)

        self.label_header = QLabel(self.frame_header)
        self.label_header.setObjectName(u"label_header")
        self.label_header.setMaximumSize(QSize(559, 16777215))
        self.label_header.setStyleSheet(u"background-color: rgb(162, 162, 162);")
        self.label_header.setAlignment(Qt.AlignCenter)
        self.label_header.setMargin(5)
        self.label_header.setIndent(0)

        self.horizontalLayout_2.addWidget(self.label_header)


        self.verticalLayout.addWidget(self.frame_header)

        self.frame_main_page = QFrame(self.frame_main_content)
        self.frame_main_page.setObjectName(u"frame_main_page")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_main_page.sizePolicy().hasHeightForWidth())
        self.frame_main_page.setSizePolicy(sizePolicy1)
        self.frame_main_page.setStyleSheet(u"background-color: rgb(62, 62, 62);\n"
"")
        self.frame_main_page.setFrameShape(QFrame.StyledPanel)
        self.frame_main_page.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_main_page)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.stackedWidget = QStackedWidget(self.frame_main_page)
        self.stackedWidget.setObjectName(u"stackedWidget")
        palette = QPalette()
        brush = QBrush(QColor(163, 163, 163, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.stackedWidget.setPalette(palette)
        self.stackedWidget.setStyleSheet(u"background-color: rgb(163, 163, 163);\n"
"\n"
"")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.verticalLayout_5 = QVBoxLayout(self.page_home)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_logo_home = QLabel(self.page_home)
        self.label_logo_home.setObjectName(u"label_logo_home")

        self.verticalLayout_5.addWidget(self.label_logo_home)

        self.stackedWidget.addWidget(self.page_home)
        self.page_cadastrar = QWidget()
        self.page_cadastrar.setObjectName(u"page_cadastrar")
        self.verticalLayout_6 = QVBoxLayout(self.page_cadastrar)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.tabWidget = QTabWidget(self.page_cadastrar)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setElideMode(Qt.ElideRight)
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tab_cadastro = QWidget()
        self.tab_cadastro.setObjectName(u"tab_cadastro")
        self.verticalLayout_9 = QVBoxLayout(self.tab_cadastro)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_title_page_cadastrar = QLabel(self.tab_cadastro)
        self.label_title_page_cadastrar.setObjectName(u"label_title_page_cadastrar")

        self.verticalLayout_9.addWidget(self.label_title_page_cadastrar)

        self.frame_content_cadastro = QFrame(self.tab_cadastro)
        self.frame_content_cadastro.setObjectName(u"frame_content_cadastro")
        sizePolicy1.setHeightForWidth(self.frame_content_cadastro.sizePolicy().hasHeightForWidth())
        self.frame_content_cadastro.setSizePolicy(sizePolicy1)
        self.frame_content_cadastro.setMaximumSize(QSize(887, 16777215))
        self.frame_content_cadastro.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(255,255,255);\n"
"	font: 13pt \"Helvetica Neue\";\n"
"}\n"
"\n"
"QFrame{\n"
"	background-color: rgb(63,63,63);\n"
"}")
        self.frame_content_cadastro.setFrameShape(QFrame.StyledPanel)
        self.frame_content_cadastro.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_content_cadastro)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit_9_cep = QLineEdit(self.frame_content_cadastro)
        self.lineEdit_9_cep.setObjectName(u"lineEdit_9_cep")
        self.lineEdit_9_cep.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_9_cep, 3, 2, 1, 1)

        self.lineEdit_11_email = QLineEdit(self.frame_content_cadastro)
        self.lineEdit_11_email.setObjectName(u"lineEdit_11_email")
        self.lineEdit_11_email.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_11_email, 4, 1, 1, 2)

        self.lineEdit_6_bairro = QLineEdit(self.frame_content_cadastro)
        self.lineEdit_6_bairro.setObjectName(u"lineEdit_6_bairro")
        self.lineEdit_6_bairro.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_6_bairro, 2, 2, 1, 1)

        self.lineEdit_5_complemento = QLineEdit(self.frame_content_cadastro)
        self.lineEdit_5_complemento.setObjectName(u"lineEdit_5_complemento")
        self.lineEdit_5_complemento.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_5_complemento, 2, 1, 1, 1)

        self.lineEdit_4_numero = QLineEdit(self.frame_content_cadastro)
        self.lineEdit_4_numero.setObjectName(u"lineEdit_4_numero")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lineEdit_4_numero.sizePolicy().hasHeightForWidth())
        self.lineEdit_4_numero.setSizePolicy(sizePolicy2)
        self.lineEdit_4_numero.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_4_numero, 2, 0, 1, 1)

        self.lineEdit_8_uf = QLineEdit(self.frame_content_cadastro)
        self.lineEdit_8_uf.setObjectName(u"lineEdit_8_uf")
        self.lineEdit_8_uf.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_8_uf, 3, 1, 1, 1)

        self.lineEdit_7_municipio = QLineEdit(self.frame_content_cadastro)
        self.lineEdit_7_municipio.setObjectName(u"lineEdit_7_municipio")
        sizePolicy2.setHeightForWidth(self.lineEdit_7_municipio.sizePolicy().hasHeightForWidth())
        self.lineEdit_7_municipio.setSizePolicy(sizePolicy2)
        self.lineEdit_7_municipio.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_7_municipio, 3, 0, 1, 1)

        self.lineEdit_2_nome_empresarial = QLineEdit(self.frame_content_cadastro)
        self.lineEdit_2_nome_empresarial.setObjectName(u"lineEdit_2_nome_empresarial")
        self.lineEdit_2_nome_empresarial.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_2_nome_empresarial, 0, 1, 1, 2)

        self.lineEdit_3_logradouro = QLineEdit(self.frame_content_cadastro)
        self.lineEdit_3_logradouro.setObjectName(u"lineEdit_3_logradouro")
        self.lineEdit_3_logradouro.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_3_logradouro, 1, 0, 1, 3)

        self.lineEdit_1_cnpj = QLineEdit(self.frame_content_cadastro)
        self.lineEdit_1_cnpj.setObjectName(u"lineEdit_1_cnpj")
        self.lineEdit_1_cnpj.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_1_cnpj, 0, 0, 1, 1)

        self.lineEdit_10_telefone = QLineEdit(self.frame_content_cadastro)
        self.lineEdit_10_telefone.setObjectName(u"lineEdit_10_telefone")
        sizePolicy2.setHeightForWidth(self.lineEdit_10_telefone.sizePolicy().hasHeightForWidth())
        self.lineEdit_10_telefone.setSizePolicy(sizePolicy2)
        self.lineEdit_10_telefone.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_10_telefone, 4, 0, 1, 1)


        self.verticalLayout_9.addWidget(self.frame_content_cadastro)

        self.frame_page_cadastrar = QFrame(self.tab_cadastro)
        self.frame_page_cadastrar.setObjectName(u"frame_page_cadastrar")
        self.frame_page_cadastrar.setStyleSheet(u"QPushButton:hover{\n"
"	border-radius: 5px;\n"
"	background-color: rgb(62, 62, 62);\n"
"}\n"
"\n"
"QPushButton{\n"
"	color: rgb(255, 255, 255)\n"
"}")
        self.frame_page_cadastrar.setFrameShape(QFrame.StyledPanel)
        self.frame_page_cadastrar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_page_cadastrar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.button_confirmar = QPushButton(self.frame_page_cadastrar)
        self.button_confirmar.setObjectName(u"button_confirmar")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.button_confirmar.sizePolicy().hasHeightForWidth())
        self.button_confirmar.setSizePolicy(sizePolicy3)
        self.button_confirmar.setMinimumSize(QSize(0, 30))
        self.button_confirmar.setMaximumSize(QSize(150, 150))
        self.button_confirmar.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.button_confirmar)

        self.button_cancelar = QPushButton(self.frame_page_cadastrar)
        self.button_cancelar.setObjectName(u"button_cancelar")
        sizePolicy3.setHeightForWidth(self.button_cancelar.sizePolicy().hasHeightForWidth())
        self.button_cancelar.setSizePolicy(sizePolicy3)
        self.button_cancelar.setMinimumSize(QSize(0, 30))
        self.button_cancelar.setMaximumSize(QSize(150, 150))
        self.button_cancelar.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.button_cancelar)


        self.verticalLayout_9.addWidget(self.frame_page_cadastrar)

        self.tabWidget.addTab(self.tab_cadastro, "")
        self.tab_empresas = QWidget()
        self.tab_empresas.setObjectName(u"tab_empresas")
        self.verticalLayout_8 = QVBoxLayout(self.tab_empresas)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_title_page_empresas = QLabel(self.tab_empresas)
        self.label_title_page_empresas.setObjectName(u"label_title_page_empresas")

        self.verticalLayout_8.addWidget(self.label_title_page_empresas)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.tableWidget = QTableWidget(self.tab_empresas)
        if (self.tableWidget.columnCount() < 9):
            self.tableWidget.setColumnCount(9)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setMinimumSize(QSize(700, 500))
        self.tableWidget.setMaximumSize(QSize(16777215, 16777215))
        self.tableWidget.setBaseSize(QSize(0, 0))
        self.tableWidget.setStyleSheet(u"QHeaderView::section{\n"
"	background-color: rgb(63,63,63);\n"
"	color: rgb(255,255,255)\n"
"}\n"
"\n"
"QTableWidget{\n"
"	\n"
"}")

        self.horizontalLayout_7.addWidget(self.tableWidget)

        self.frame = QFrame(self.tab_empresas)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(150, 500))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.button_excel = QPushButton(self.frame)
        self.button_excel.setObjectName(u"button_excel")
        self.button_excel.setMinimumSize(QSize(0, 30))
        self.button_excel.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_excel.setStyleSheet(u"QPushButton:hover{\n"
"	border-radius: 5px;\n"
"	background-color: rgb(62, 62, 62);\n"
"}\n"
"\n"
"QPushButton{\n"
"	color: rgb(255, 255, 255)\n"
"}\n"
"")

        self.verticalLayout_7.addWidget(self.button_excel)

        self.button_alterar = QPushButton(self.frame)
        self.button_alterar.setObjectName(u"button_alterar")
        self.button_alterar.setMinimumSize(QSize(0, 30))
        self.button_alterar.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_alterar.setStyleSheet(u"QPushButton:hover{\n"
"	border-radius: 5px;\n"
"	background-color: rgb(62, 62, 62);\n"
"}\n"
"\n"
"QPushButton{\n"
"	color: rgb(255, 255, 255)\n"
"}\n"
"")

        self.verticalLayout_7.addWidget(self.button_alterar)

        self.button_excluir = QPushButton(self.frame)
        self.button_excluir.setObjectName(u"button_excluir")
        self.button_excluir.setMinimumSize(QSize(0, 30))
        self.button_excluir.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_excluir.setStyleSheet(u"QPushButton:hover{\n"
"	border-radius: 5px;\n"
"	background-color: rgb(62, 62, 62);\n"
"}\n"
"\n"
"QPushButton{\n"
"	color: rgb(255, 255, 255)\n"
"}\n"
"")

        self.verticalLayout_7.addWidget(self.button_excluir)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer)


        self.horizontalLayout_7.addWidget(self.frame)


        self.verticalLayout_8.addLayout(self.horizontalLayout_7)

        self.tabWidget.addTab(self.tab_empresas, "")

        self.verticalLayout_6.addWidget(self.tabWidget)

        self.stackedWidget.addWidget(self.page_cadastrar)
        self.page_contatos = QWidget()
        self.page_contatos.setObjectName(u"page_contatos")
        self.verticalLayout_11 = QVBoxLayout(self.page_contatos)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_2 = QFrame(self.page_contatos)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_2)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")

        self.verticalLayout_10.addWidget(self.label, 0, Qt.AlignHCenter)

        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_2)


        self.verticalLayout_11.addWidget(self.frame_2)

        self.stackedWidget.addWidget(self.page_contatos)
        self.page_sobre = QWidget()
        self.page_sobre.setObjectName(u"page_sobre")
        self.verticalLayout_12 = QVBoxLayout(self.page_sobre)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_3 = QLabel(self.page_sobre)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_12.addWidget(self.label_3)

        self.label_4 = QLabel(self.page_sobre)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_4.setWordWrap(True)
        self.label_4.setMargin(5)
        self.label_4.setIndent(0)

        self.verticalLayout_12.addWidget(self.label_4)

        self.stackedWidget.addWidget(self.page_sobre)

        self.verticalLayout_3.addWidget(self.stackedWidget)


        self.verticalLayout.addWidget(self.frame_main_page)

        self.frame_footer = QFrame(self.frame_main_content)
        self.frame_footer.setObjectName(u"frame_footer")
        self.frame_footer.setStyleSheet(u"background-color: rgb(62, 62, 62);")
        self.frame_footer.setFrameShape(QFrame.StyledPanel)
        self.frame_footer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_footer)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.label_footer = QLabel(self.frame_footer)
        self.label_footer.setObjectName(u"label_footer")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_footer.sizePolicy().hasHeightForWidth())
        self.label_footer.setSizePolicy(sizePolicy4)
        self.label_footer.setStyleSheet(u"background-color: rgb(163, 163, 163);")
        self.label_footer.setAlignment(Qt.AlignCenter)
        self.label_footer.setMargin(3)
        self.label_footer.setIndent(-1)

        self.horizontalLayout_3.addWidget(self.label_footer)


        self.verticalLayout.addWidget(self.frame_footer)


        self.gridLayout_2.addWidget(self.frame_main_content, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.box_menu.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(2)
        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_logo.setText(QCoreApplication.translate("MainWindow", u"GalliBrothers.Inc", None))
        self.button_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.button_cadastrar.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.button_contatos.setText(QCoreApplication.translate("MainWindow", u"Contatos", None))
        self.button_sobre.setText(QCoreApplication.translate("MainWindow", u"Sobre", None))
        self.box_menu.setItemText(self.box_menu.indexOf(self.box_menu_menu), QCoreApplication.translate("MainWindow", u"Menu", None))
        self.label_info.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Criado por <span style=\" font-weight:600;\">Galli, Marcelo L.</span></p><p align=\"center\"><a href=\"https://github.com/MarceloGalliDev\"><span style=\" text-decoration: underline; color:#0000ff;\">GitHub</span></a></p></body></html>", None))
        self.box_menu.setItemText(self.box_menu.indexOf(self.box_menu_info), QCoreApplication.translate("MainWindow", u"Informa\u00e7\u00f5es", None))
        self.button_toggle.setText("")
        self.label_header.setText(QCoreApplication.translate("MainWindow", u"Sistema de cadastro", None))
#if QT_CONFIG(whatsthis)
        self.stackedWidget.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_logo_home.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icons/logo4.png\"/></p></body></html>", None))
        self.label_title_page_cadastrar.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600;\">CADASTRO</span></p></body></html>", None))
        self.lineEdit_9_cep.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CEP", None))
        self.lineEdit_11_email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"E-MAIL", None))
        self.lineEdit_6_bairro.setPlaceholderText(QCoreApplication.translate("MainWindow", u"BAIRRO", None))
        self.lineEdit_5_complemento.setPlaceholderText(QCoreApplication.translate("MainWindow", u"COMPLEMENTO", None))
        self.lineEdit_4_numero.setPlaceholderText(QCoreApplication.translate("MainWindow", u"N\u00daMERO", None))
        self.lineEdit_8_uf.setPlaceholderText(QCoreApplication.translate("MainWindow", u"UF", None))
        self.lineEdit_7_municipio.setPlaceholderText(QCoreApplication.translate("MainWindow", u"MUNIC\u00cdPIO", None))
        self.lineEdit_2_nome_empresarial.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NOME EMPRESARIAL", None))
        self.lineEdit_3_logradouro.setPlaceholderText(QCoreApplication.translate("MainWindow", u"LOGRADOURO", None))
        self.lineEdit_1_cnpj.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CNPJ", None))
        self.lineEdit_10_telefone.setPlaceholderText(QCoreApplication.translate("MainWindow", u"TELEFONE", None))
        self.button_confirmar.setText(QCoreApplication.translate("MainWindow", u"CONFIRMAR", None))
        self.button_cancelar.setText(QCoreApplication.translate("MainWindow", u"CANCELAR", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_cadastro), QCoreApplication.translate("MainWindow", u"Cadastro", None))
        self.label_title_page_empresas.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600;\">EMPRESAS</span></p></body></html>", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"NOME", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"CNPJ", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"LOGRADOURO", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"COMPLEMENTO", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"N\u00daMERO", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"BAIRRO", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"MUNIC\u00edPIO", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"TELEFONE", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"EMAIL", None));
        self.button_excel.setText(QCoreApplication.translate("MainWindow", u"Gerar excel", None))
        self.button_alterar.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.button_excluir.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_empresas), QCoreApplication.translate("MainWindow", u"Empresas", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/icons/icons/whatsApp.png\"/><span style=\" font-size:24pt; vertical-align:super;\">(44)98862-0946</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/icons/icons/email.png\"/><span style=\" font-size:24pt; vertical-align:super;\">marcelolemesgalli@hotmail.com</span></p><p><br/></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:600;\">SOBRE</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">EMPRESA CRIADA PARA DESENVOLVIMENTO DE SOFTWARE, MACHINE LEARNING, BUSINESS INTELIGENCE</span></p></body></html>", None))
        self.label_footer.setText(QCoreApplication.translate("MainWindow", u"GalliBrothers.Inc", None))
    # retranslateUi

