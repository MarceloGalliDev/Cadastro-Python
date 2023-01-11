# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cadastroV2.ui'
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
    QPushButton, QSizePolicy, QSpacerItem, QTabWidget,
    QTableWidget, QTableWidgetItem, QToolBox, QVBoxLayout,
    QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1156, 864)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_main = QFrame(self.centralwidget)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setMinimumSize(QSize(1050, 650))
        self.frame_main.setMaximumSize(QSize(1050, 600))
        self.frame_main.setStyleSheet(u"background-color: rgb(1, 38, 31);\n"
"border-radius: 15px;")
        self.frame_main.setFrameShape(QFrame.StyledPanel)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_main)
#ifndef Q_OS_MAC
        self.horizontalLayout_2.setSpacing(-1)
#endif
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 12, 0)
        self.frame_main_menu = QFrame(self.frame_main)
        self.frame_main_menu.setObjectName(u"frame_main_menu")
        self.frame_main_menu.setMinimumSize(QSize(0, 0))
        self.frame_main_menu.setMaximumSize(QSize(0, 600))
        self.frame_main_menu.setStyleSheet(u"background-color: rgb(32,89,79);\n"
"border-radius: 10px;")
        self.frame_main_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_main_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_main_menu)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.toolBox = QToolBox(self.frame_main_menu)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setEnabled(True)
        self.toolBox.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setStrikeOut(False)
        font.setKerning(True)
        self.toolBox.setFont(font)
        self.toolBox.setCursor(QCursor(Qt.ArrowCursor))
        self.toolBox.setMouseTracking(False)
        self.toolBox.setTabletTracking(False)
        self.toolBox.setFocusPolicy(Qt.NoFocus)
        self.toolBox.setContextMenuPolicy(Qt.CustomContextMenu)
        self.toolBox.setAcceptDrops(False)
        self.toolBox.setLayoutDirection(Qt.LeftToRight)
        self.toolBox.setAutoFillBackground(False)
        self.toolBox.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(32,89,79);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QToolBox::tab{\n"
"	border-radius: 5px;\n"
"	background-color: rgb(242, 98, 15);\n"
"}\n"
"\n"
"QToolBox::tab:hover{\n"
"	background-color: rgb(242, 84, 2);\n"
"	border-radius: 5px;\n"
"}")
        self.toolBox.setInputMethodHints(Qt.ImhNone)
        self.toolBoxPage1 = QWidget()
        self.toolBoxPage1.setObjectName(u"toolBoxPage1")
        self.toolBoxPage1.setGeometry(QRect(0, 0, 84, 493))
        self.toolBoxPage1.setCursor(QCursor(Qt.PointingHandCursor))
        self.verticalLayout_5 = QVBoxLayout(self.toolBoxPage1)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.btn_home = QPushButton(self.toolBoxPage1)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy)
        self.btn_home.setMinimumSize(QSize(0, 30))
        self.btn_home.setMaximumSize(QSize(16777215, 30))
        self.btn_home.setSizeIncrement(QSize(0, 0))
        self.btn_home.setBaseSize(QSize(0, 0))
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(242, 98, 15);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(242, 84, 27);\n"
"	border-radius: 10px;\n"
"}")

        self.verticalLayout_5.addWidget(self.btn_home)

        self.btn_cadastrar = QPushButton(self.toolBoxPage1)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")
        sizePolicy.setHeightForWidth(self.btn_cadastrar.sizePolicy().hasHeightForWidth())
        self.btn_cadastrar.setSizePolicy(sizePolicy)
        self.btn_cadastrar.setMinimumSize(QSize(0, 30))
        self.btn_cadastrar.setMaximumSize(QSize(16777215, 30))
        self.btn_cadastrar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cadastrar.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(242, 98, 15);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(242, 84, 27);\n"
"	border-radius: 10px;\n"
"}")

        self.verticalLayout_5.addWidget(self.btn_cadastrar)

        self.btn_contatos = QPushButton(self.toolBoxPage1)
        self.btn_contatos.setObjectName(u"btn_contatos")
        sizePolicy.setHeightForWidth(self.btn_contatos.sizePolicy().hasHeightForWidth())
        self.btn_contatos.setSizePolicy(sizePolicy)
        self.btn_contatos.setMinimumSize(QSize(0, 30))
        self.btn_contatos.setMaximumSize(QSize(16777215, 30))
        self.btn_contatos.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_contatos.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(242, 98, 15);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(242, 84, 27);\n"
"	border-radius: 10px;\n"
"}")

        self.verticalLayout_5.addWidget(self.btn_contatos)

        self.btn_sobre = QPushButton(self.toolBoxPage1)
        self.btn_sobre.setObjectName(u"btn_sobre")
        sizePolicy.setHeightForWidth(self.btn_sobre.sizePolicy().hasHeightForWidth())
        self.btn_sobre.setSizePolicy(sizePolicy)
        self.btn_sobre.setMinimumSize(QSize(0, 30))
        self.btn_sobre.setMaximumSize(QSize(16777215, 30))
        self.btn_sobre.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_sobre.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(242, 98, 15);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(242, 84, 27);\n"
"	border-radius: 10px;\n"
"}")

        self.verticalLayout_5.addWidget(self.btn_sobre)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.toolBox.addItem(self.toolBoxPage1, u"Menu")
        self.toolBoxPage2 = QWidget()
        self.toolBoxPage2.setObjectName(u"toolBoxPage2")
        self.toolBoxPage2.setGeometry(QRect(0, 0, 92, 493))
        self.toolBoxPage2.setCursor(QCursor(Qt.PointingHandCursor))
        self.horizontalLayout_3 = QHBoxLayout(self.toolBoxPage2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.toolBoxPage2)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet(u"color: #fff")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setIndent(0)

        self.horizontalLayout_3.addWidget(self.label)

        self.toolBox.addItem(self.toolBoxPage2, u"Info")

        self.verticalLayout.addWidget(self.toolBox)


        self.horizontalLayout_2.addWidget(self.frame_main_menu)

        self.frame_main_content = QFrame(self.frame_main)
        self.frame_main_content.setObjectName(u"frame_main_content")
        self.frame_main_content.setMinimumSize(QSize(0, 0))
        self.frame_main_content.setMaximumSize(QSize(1050, 600))
        self.frame_main_content.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(32,89,79);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"")
        self.frame_main_content.setFrameShape(QFrame.StyledPanel)
        self.frame_main_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_main_content)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_header = QFrame(self.frame_main_content)
        self.frame_header.setObjectName(u"frame_header")
        self.frame_header.setMaximumSize(QSize(16777215, 50))
        self.frame_header.setStyleSheet(u"background-color: rgb(242, 98, 15);\n"
"border-radius: 10px;")
        self.frame_header.setFrameShape(QFrame.StyledPanel)
        self.frame_header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_header)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btn_toggle = QPushButton(self.frame_header)
        self.btn_toggle.setObjectName(u"btn_toggle")
        sizePolicy.setHeightForWidth(self.btn_toggle.sizePolicy().hasHeightForWidth())
        self.btn_toggle.setSizePolicy(sizePolicy)
        self.btn_toggle.setMaximumSize(QSize(50, 16777215))
        self.btn_toggle.setStyleSheet(u"QPushButton:pressed{\n"
"	background-color: rgb(254, 158,49);\n"
"	border-radius: 0px;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/icons/menu2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_toggle.setIcon(icon)
        self.btn_toggle.setIconSize(QSize(30, 30))

        self.horizontalLayout_4.addWidget(self.btn_toggle)

        self.label_header_title = QLabel(self.frame_header)
        self.label_header_title.setObjectName(u"label_header_title")

        self.horizontalLayout_4.addWidget(self.label_header_title)


        self.verticalLayout_3.addWidget(self.frame_header)

        self.frame_content = QFrame(self.frame_main_content)
        self.frame_content.setObjectName(u"frame_content")
        sizePolicy.setHeightForWidth(self.frame_content.sizePolicy().hasHeightForWidth())
        self.frame_content.setSizePolicy(sizePolicy)
        self.frame_content.setStyleSheet(u"background-color: rgb(242, 98, 15);\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.frame_content.setFrameShape(QFrame.StyledPanel)
        self.frame_content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_content)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(5, 5, 5, 5)
        self.tabWidget_content = QTabWidget(self.frame_content)
        self.tabWidget_content.setObjectName(u"tabWidget_content")
        self.tabWidget_content.setMinimumSize(QSize(0, 0))
        self.tabWidget_content.setTabletTracking(False)
        self.tabWidget_content.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.tabWidget_content.setStyleSheet(u"QTabBar::tab{\n"
"	background-color: rgb(242, 98, 15);\n"
"}\n"
"\n"
"QTabBar::tab:selected{\n"
"	background-color: rgb(254, 158,49);\n"
"}\n"
"\n"
"QWidget{\n"
"	background-color: rgb(254, 158,49);\n"
"}\n"
"\n"
"")
        self.tabWidget_content.setElideMode(Qt.ElideRight)
        self.tabWidget_content.setDocumentMode(False)
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(100)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.page_home.sizePolicy().hasHeightForWidth())
        self.page_home.setSizePolicy(sizePolicy1)
        self.page_home.setMinimumSize(QSize(0, 0))
        self.page_home.setStyleSheet(u"")
        self.horizontalLayout_9 = QHBoxLayout(self.page_home)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.frame_1_content = QFrame(self.page_home)
        self.frame_1_content.setObjectName(u"frame_1_content")
        self.frame_1_content.setStyleSheet(u"background-color: rgb(32,89,79);\n"
"border-radius: 10px;")
        self.frame_1_content.setFrameShape(QFrame.StyledPanel)
        self.frame_1_content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_1_content)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_1_content = QLabel(self.frame_1_content)
        self.label_1_content.setObjectName(u"label_1_content")

        self.horizontalLayout_10.addWidget(self.label_1_content)


        self.horizontalLayout_9.addWidget(self.frame_1_content)

        self.tabWidget_content.addTab(self.page_home, "")
        self.page_cadastrar = QWidget()
        self.page_cadastrar.setObjectName(u"page_cadastrar")
        self.page_cadastrar.setStyleSheet(u"QWidget::tab{\n"
"	background-color: rgb(254, 158, 49);\n"
"	color: rgb(0,0,0,);\n"
"}\n"
"\n"
"QWidget{\n"
"	background-color: rgb(254, 158, 49);\n"
"	color: rgb(0,0,0,);\n"
"}")
        self.horizontalLayout_16 = QHBoxLayout(self.page_cadastrar)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.tabWidget = QTabWidget(self.page_cadastrar)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QSize(0, 0))
        self.tabWidget.setLayoutDirection(Qt.LeftToRight)
        self.tabWidget.setStyleSheet(u"QTabBar::tab{\n"
"	background-color: rgb(254, 158,49);\n"
"}\n"
"\n"
"QTabBar::tab:selected{\n"
"	background-color: rgb(32,89,79);\n"
"}\n"
"\n"
"QWidget{\n"
"	background-color: rgb(32,89,79);\n"
"}\n"
"\n"
"\n"
"")
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setElideMode(Qt.ElideLeft)
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tab_1 = QWidget()
        self.tab_1.setObjectName(u"tab_1")
        self.verticalLayout_8 = QVBoxLayout(self.tab_1)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_2 = QLabel(self.tab_1)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 50))
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")
        self.label_2.setLineWidth(5)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setMargin(5)
        self.label_2.setIndent(0)

        self.verticalLayout_8.addWidget(self.label_2)

        self.frame_2_content = QFrame(self.tab_1)
        self.frame_2_content.setObjectName(u"frame_2_content")
        sizePolicy.setHeightForWidth(self.frame_2_content.sizePolicy().hasHeightForWidth())
        self.frame_2_content.setSizePolicy(sizePolicy)
        self.frame_2_content.setStyleSheet(u"background-color: rgb(32,89,79);")
        self.frame_2_content.setFrameShape(QFrame.StyledPanel)
        self.frame_2_content.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_2_content)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(5, 5, 5, 5)
        self.frame = QFrame(self.frame_2_content)
        self.frame.setObjectName(u"frame")
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setSizeIncrement(QSize(0, 0))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_cep = QLineEdit(self.frame)
        self.lineEdit_cep.setObjectName(u"lineEdit_cep")
        self.lineEdit_cep.setMinimumSize(QSize(0, 40))
        font1 = QFont()
        font1.setPointSize(18)
        self.lineEdit_cep.setFont(font1)
        self.lineEdit_cep.setStyleSheet(u"background-color: rgb(136,191,181);")
        self.lineEdit_cep.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_cep, 3, 2, 1, 1)

        self.lineEdit_cnpj = QLineEdit(self.frame)
        self.lineEdit_cnpj.setObjectName(u"lineEdit_cnpj")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lineEdit_cnpj.sizePolicy().hasHeightForWidth())
        self.lineEdit_cnpj.setSizePolicy(sizePolicy2)
        self.lineEdit_cnpj.setMinimumSize(QSize(0, 40))
        self.lineEdit_cnpj.setFont(font1)
        self.lineEdit_cnpj.setStyleSheet(u"background-color: rgb(136,191,181);")
        self.lineEdit_cnpj.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_cnpj, 0, 0, 1, 1)

        self.lineEdit_razao_social = QLineEdit(self.frame)
        self.lineEdit_razao_social.setObjectName(u"lineEdit_razao_social")
        self.lineEdit_razao_social.setMinimumSize(QSize(0, 40))
        self.lineEdit_razao_social.setFont(font1)
        self.lineEdit_razao_social.setStyleSheet(u"background-color: rgb(136,191,181);")
        self.lineEdit_razao_social.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_razao_social, 0, 1, 1, 2)

        self.lineEdit_uf = QLineEdit(self.frame)
        self.lineEdit_uf.setObjectName(u"lineEdit_uf")
        self.lineEdit_uf.setMinimumSize(QSize(0, 40))
        self.lineEdit_uf.setFont(font1)
        self.lineEdit_uf.setStyleSheet(u"background-color: rgb(136,191,181);")
        self.lineEdit_uf.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_uf, 3, 1, 1, 1)

        self.lineEdit_email = QLineEdit(self.frame)
        self.lineEdit_email.setObjectName(u"lineEdit_email")
        self.lineEdit_email.setMinimumSize(QSize(0, 40))
        self.lineEdit_email.setFont(font1)
        self.lineEdit_email.setStyleSheet(u"background-color: rgb(136,191,181);")
        self.lineEdit_email.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_email, 4, 1, 1, 2)

        self.lineEdit_telefone = QLineEdit(self.frame)
        self.lineEdit_telefone.setObjectName(u"lineEdit_telefone")
        self.lineEdit_telefone.setMinimumSize(QSize(0, 40))
        self.lineEdit_telefone.setFont(font1)
        self.lineEdit_telefone.setStyleSheet(u"background-color: rgb(136,191,181);")
        self.lineEdit_telefone.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_telefone, 4, 0, 1, 1)

        self.lineEdit_municipio = QLineEdit(self.frame)
        self.lineEdit_municipio.setObjectName(u"lineEdit_municipio")
        self.lineEdit_municipio.setMinimumSize(QSize(0, 40))
        self.lineEdit_municipio.setFont(font1)
        self.lineEdit_municipio.setStyleSheet(u"background-color: rgb(136,191,181);")
        self.lineEdit_municipio.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_municipio, 3, 0, 1, 1)

        self.lineEdit_logradouro = QLineEdit(self.frame)
        self.lineEdit_logradouro.setObjectName(u"lineEdit_logradouro")
        sizePolicy2.setHeightForWidth(self.lineEdit_logradouro.sizePolicy().hasHeightForWidth())
        self.lineEdit_logradouro.setSizePolicy(sizePolicy2)
        self.lineEdit_logradouro.setMinimumSize(QSize(0, 40))
        self.lineEdit_logradouro.setFont(font1)
        self.lineEdit_logradouro.setStyleSheet(u"background-color: rgb(136,191,181);")
        self.lineEdit_logradouro.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_logradouro, 1, 0, 1, 2)

        self.lineEdit_numero = QLineEdit(self.frame)
        self.lineEdit_numero.setObjectName(u"lineEdit_numero")
        self.lineEdit_numero.setMinimumSize(QSize(0, 40))
        self.lineEdit_numero.setFont(font1)
        self.lineEdit_numero.setStyleSheet(u"background-color: rgb(136,191,181);")
        self.lineEdit_numero.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_numero, 1, 2, 1, 1)

        self.lineEdit_complemento = QLineEdit(self.frame)
        self.lineEdit_complemento.setObjectName(u"lineEdit_complemento")
        self.lineEdit_complemento.setMinimumSize(QSize(0, 40))
        self.lineEdit_complemento.setFont(font1)
        self.lineEdit_complemento.setStyleSheet(u"background-color: rgb(136,191,181);")
        self.lineEdit_complemento.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_complemento, 2, 0, 1, 1)

        self.lineEdit_bairro = QLineEdit(self.frame)
        self.lineEdit_bairro.setObjectName(u"lineEdit_bairro")
        self.lineEdit_bairro.setMinimumSize(QSize(0, 40))
        self.lineEdit_bairro.setFont(font1)
        self.lineEdit_bairro.setStyleSheet(u"background-color: rgb(136,191,181);")
        self.lineEdit_bairro.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_bairro, 2, 1, 1, 2)


        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)


        self.verticalLayout_8.addWidget(self.frame_2_content)

        self.frame_4 = QFrame(self.tab_1)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(242, 98, 15);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(242, 84, 27);\n"
"	border-radius: 10px;\n"
"}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.btn_cadastrar_2 = QPushButton(self.frame_4)
        self.btn_cadastrar_2.setObjectName(u"btn_cadastrar_2")
        self.btn_cadastrar_2.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_5.addWidget(self.btn_cadastrar_2)

        self.pushButton_limpar = QPushButton(self.frame_4)
        self.pushButton_limpar.setObjectName(u"pushButton_limpar")
        self.pushButton_limpar.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_5.addWidget(self.pushButton_limpar)


        self.verticalLayout_8.addWidget(self.frame_4)

        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_9 = QVBoxLayout(self.tab_2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_3 = QLabel(self.tab_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 50))
        self.label_3.setMaximumSize(QSize(16777215, 50))
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")
        self.label_3.setLineWidth(5)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_3.setMargin(5)
        self.label_3.setIndent(0)

        self.verticalLayout_9.addWidget(self.label_3)

        self.frame_2 = QFrame(self.tab_2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_15.setSpacing(5)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.tb_company = QTableWidget(self.frame_2)
        if (self.tb_company.columnCount() < 11):
            self.tb_company.setColumnCount(11)
        __qtablewidgetitem = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        self.tb_company.setObjectName(u"tb_company")
        self.tb_company.setStyleSheet(u"QTableView {\n"
"	background-color: rgb(255,255,255);\n"
"}\n"
"\n"
"")

        self.horizontalLayout_15.addWidget(self.tb_company)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(130, 0))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_3)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.pushButton = QPushButton(self.frame_3)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QSize(0, 30))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(242, 98, 15);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(242, 84, 27);\n"
"	border-radius: 10px;\n"
"}")

        self.verticalLayout_10.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.frame_3)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 30))
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(242, 98, 15);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(242, 84, 27);\n"
"	border-radius: 10px;\n"
"}")

        self.verticalLayout_10.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.frame_3)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(0, 30))
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(242, 98, 15);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(242, 84, 27);\n"
"	border-radius: 10px;\n"
"}")

        self.verticalLayout_10.addWidget(self.pushButton_3)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_2)


        self.horizontalLayout_15.addWidget(self.frame_3)


        self.verticalLayout_9.addWidget(self.frame_2)

        self.tabWidget.addTab(self.tab_2, "")

        self.horizontalLayout_16.addWidget(self.tabWidget)

        self.tabWidget_content.addTab(self.page_cadastrar, "")
        self.page_contatos = QWidget()
        self.page_contatos.setObjectName(u"page_contatos")
        self.horizontalLayout_14 = QHBoxLayout(self.page_contatos)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.frame_3_content = QFrame(self.page_contatos)
        self.frame_3_content.setObjectName(u"frame_3_content")
        self.frame_3_content.setStyleSheet(u"background-color: rgb(32,89,79);\n"
"border-radius: 10px;")
        self.frame_3_content.setFrameShape(QFrame.StyledPanel)
        self.frame_3_content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_3_content)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_4 = QLabel(self.frame_3_content)
        self.label_4.setObjectName(u"label_4")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy3)
        self.label_4.setStyleSheet(u"color: rgb(255,255,255);")
        self.label_4.setTextFormat(Qt.AutoText)
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_4.setIndent(0)

        self.horizontalLayout_13.addWidget(self.label_4)


        self.horizontalLayout_14.addWidget(self.frame_3_content)

        self.tabWidget_content.addTab(self.page_contatos, "")
        self.page_sobre = QWidget()
        self.page_sobre.setObjectName(u"page_sobre")
        self.horizontalLayout_12 = QHBoxLayout(self.page_sobre)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.frame_4_content = QFrame(self.page_sobre)
        self.frame_4_content.setObjectName(u"frame_4_content")
        self.frame_4_content.setStyleSheet(u"background-color: rgb(32,89,79);\n"
"border-radius: 10px;")
        self.frame_4_content.setFrameShape(QFrame.StyledPanel)
        self.frame_4_content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_4_content)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_5 = QLabel(self.frame_4_content)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"color:rgb(255,255,255);")

        self.horizontalLayout_11.addWidget(self.label_5)


        self.horizontalLayout_12.addWidget(self.frame_4_content)

        self.tabWidget_content.addTab(self.page_sobre, "")

        self.horizontalLayout_8.addWidget(self.tabWidget_content)


        self.verticalLayout_3.addWidget(self.frame_content)

        self.frame_footer = QFrame(self.frame_main_content)
        self.frame_footer.setObjectName(u"frame_footer")
        self.frame_footer.setMaximumSize(QSize(16777215, 50))
        self.frame_footer.setStyleSheet(u"background-color: rgb(242, 98, 15);\n"
"border-radius: 10px;")
        self.frame_footer.setFrameShape(QFrame.StyledPanel)
        self.frame_footer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_footer)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_footer = QLabel(self.frame_footer)
        self.label_footer.setObjectName(u"label_footer")
        self.label_footer.setStyleSheet(u"background-color: rgb(242, 98, 15);")

        self.verticalLayout_4.addWidget(self.label_footer)


        self.verticalLayout_3.addWidget(self.frame_footer)


        self.horizontalLayout_2.addWidget(self.frame_main_content)


        self.horizontalLayout.addWidget(self.frame_main)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.btn_home, self.btn_cadastrar)
        QWidget.setTabOrder(self.btn_cadastrar, self.btn_contatos)
        QWidget.setTabOrder(self.btn_contatos, self.btn_sobre)

        self.retranslateUi(MainWindow)

        self.toolBox.setCurrentIndex(0)
        self.tabWidget_content.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_cadastrar.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.btn_contatos.setText(QCoreApplication.translate("MainWindow", u"Contatos", None))
        self.btn_sobre.setText(QCoreApplication.translate("MainWindow", u"Sobre", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.toolBoxPage1), QCoreApplication.translate("MainWindow", u"Menu", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Created 01/01/2023", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.toolBoxPage2), QCoreApplication.translate("MainWindow", u"Info", None))
        self.btn_toggle.setText("")
        self.label_header_title.setText(QCoreApplication.translate("MainWindow", u"ImovPy - Cadastro de im\u00f3veis", None))
        self.label_1_content.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icons/icons/tecnologia.png\"/></p></body></html>", None))
        self.tabWidget_content.setTabText(self.tabWidget_content.indexOf(self.page_home), QCoreApplication.translate("MainWindow", u"Home", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600;\">CADASTRO</span></p></body></html>", None))
        self.lineEdit_cep.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CEP", None))
        self.lineEdit_cnpj.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CNPJ", None))
        self.lineEdit_razao_social.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Raz\u00e3o Social", None))
        self.lineEdit_uf.setPlaceholderText(QCoreApplication.translate("MainWindow", u"UF", None))
        self.lineEdit_email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"E-Mail", None))
        self.lineEdit_telefone.setInputMask("")
        self.lineEdit_telefone.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Telefone", None))
        self.lineEdit_municipio.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Munic\u00edpio", None))
        self.lineEdit_logradouro.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Logradouro", None))
        self.lineEdit_numero.setPlaceholderText(QCoreApplication.translate("MainWindow", u"N\u00famero", None))
        self.lineEdit_complemento.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Complemento", None))
        self.lineEdit_bairro.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Bairro", None))
        self.btn_cadastrar_2.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.pushButton_limpar.setText(QCoreApplication.translate("MainWindow", u"Limpar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600;\">LISTA</span></p></body></html>", None))
        ___qtablewidgetitem = self.tb_company.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"CNPJ", None));
        ___qtablewidgetitem1 = self.tb_company.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"RAZ\u00c3O SOCIAL", None));
        ___qtablewidgetitem2 = self.tb_company.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"LOGRADOURO", None));
        ___qtablewidgetitem3 = self.tb_company.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"N\u00daMERO", None));
        ___qtablewidgetitem4 = self.tb_company.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"COMPLEMENTO", None));
        ___qtablewidgetitem5 = self.tb_company.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"BAIRRO", None));
        ___qtablewidgetitem6 = self.tb_company.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"MUNIC\u00cdPIO", None));
        ___qtablewidgetitem7 = self.tb_company.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"UF", None));
        ___qtablewidgetitem8 = self.tb_company.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"CEP", None));
        ___qtablewidgetitem9 = self.tb_company.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"TELEFONE", None));
        ___qtablewidgetitem10 = self.tb_company.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"EMAIL", None));
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Gerar Excel", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Lista", None))
        self.tabWidget_content.setTabText(self.tabWidget_content.indexOf(self.page_cadastrar), QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icons/icons/whatsApp.png\"/><span style=\" font-size:24pt; vertical-align:super;\">(44)99999-9999</span></p><p align=\"center\"><br/></p><p align=\"center\"><img src=\":/icons/icons/Youtube.png\"/><span style=\" font-size:18pt;\"/><span style=\" font-size:24pt; vertical-align:super;\">/marcelogalli</span></p><p align=\"center\"><br/></p><p align=\"center\"><img src=\":/icons/icons/email.png\"/><span style=\" font-size:24pt; vertical-align:super;\">marcelolemesgalli@hotmail.com</span></p></body></html>", None))
        self.tabWidget_content.setTabText(self.tabWidget_content.indexOf(self.page_contatos), QCoreApplication.translate("MainWindow", u"Contatos", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Empresa criada para solu\u00e7\u00e3o de agilidade em processos de uma empresa!</span></p></body></html>", None))
        self.tabWidget_content.setTabText(self.tabWidget_content.indexOf(self.page_sobre), QCoreApplication.translate("MainWindow", u"Sobre", None))
        self.label_footer.setText(QCoreApplication.translate("MainWindow", u"Created by Galli, Marcelo L. \u24c7", None))
    # retranslateUi

