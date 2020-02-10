# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Interface.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_janela_principal(object):
    def setupUi(self, janela_principal):
        janela_principal.setObjectName("janela_principal")
        janela_principal.setWindowModality(QtCore.Qt.ApplicationModal)
        janela_principal.setEnabled(True)
        janela_principal.resize(1069, 716)
        janela_principal.setAcceptDrops(False)
        icon = QtGui.QIcon()
        
        icon.addPixmap(QtGui.QPixmap("imagens\logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        janela_principal.setWindowIcon(icon)
        janela_principal.setLayoutDirection(QtCore.Qt.LeftToRight)
        janela_principal.setAutoFillBackground(False)
        janela_principal.setStyleSheet("background-color: rgb(71, 71, 71);")
        janela_principal.setWindowFilePath("")
        janela_principal.setAnimated(True)
        janela_principal.setTabShape(QtWidgets.QTabWidget.Rounded)
        janela_principal.setDockOptions(QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(janela_principal)
        self.centralwidget.setObjectName("centralwidget")
        self.menu_abas = QtWidgets.QTabWidget(self.centralwidget)
        self.menu_abas.setEnabled(True)
        self.menu_abas.setGeometry(QtCore.QRect(0, 10, 1091, 731))
        self.menu_abas.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.menu_abas.setStyleSheet("background-color: rgb(206, 206, 206);\n"
"color: rgb(0, 0, 0);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.menu_abas.setObjectName("menu_abas")
        self.inicial = QtWidgets.QWidget()
        self.inicial.setObjectName("inicial")
        self.frame_inicial = QtWidgets.QFrame(self.inicial)
        self.frame_inicial.setGeometry(QtCore.QRect(30, 20, 1031, 81))
        self.frame_inicial.setStyleSheet("background-color: rgb(206, 206, 206);\n"
"color: rgb(0, 0, 0);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.frame_inicial.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_inicial.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_inicial.setObjectName("frame_inicial")
        self.table = QtWidgets.QFrame(self.inicial)
        self.table.setGeometry(QtCore.QRect(30, 180, 1031, 481))
        self.table.setStyleSheet("background-color: rgb(206, 206, 206);\n"
"color: rgb(0, 0, 0);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.table.setFrameShape(QtWidgets.QFrame.Box)
        self.table.setFrameShadow(QtWidgets.QFrame.Plain)
        self.table.setObjectName("table")
        self.label_15 = QtWidgets.QLabel(self.table)
        self.label_15.setGeometry(QtCore.QRect(30, 10, 81, 31))
        self.label_15.setStyleSheet("background-color: rgb(206, 206, 206);\n"
"color: rgb(0, 0, 0);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")

        #tabela do inicio 
        self.Tabela_inicio = QtWidgets.QTableWidget(self.table)
        self.Tabela_inicio.setGeometry(QtCore.QRect(30, 260, 771, 181))
        self.Tabela_inicio.setMaximumSize(QtCore.QSize(771, 16777215))
        self.Tabela_inicio.setStyleSheet("background-color: rgb(206, 206, 206);\n"
"color: rgb(0, 0, 0);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.Tabela_inicio.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.Tabela_inicio.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Tabela_inicio.setAutoScroll(True)
        self.Tabela_inicio.setTabKeyNavigation(True)
        self.Tabela_inicio.setProperty("showDropIndicator", True)
        self.Tabela_inicio.setDragDropOverwriteMode(True)
        self.Tabela_inicio.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.Tabela_inicio.setWordWrap(True)
        self.Tabela_inicio.setCornerButtonEnabled(True)
        self.Tabela_inicio.setObjectName("Tabela_inicio")
        self.Tabela_inicio.setColumnCount(3)
        self.Tabela_inicio.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.Tabela_inicio.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabela_inicio.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabela_inicio.setHorizontalHeaderItem(2, item)
        self.Tabela_inicio.horizontalHeader().setVisible(True)
        self.Tabela_inicio.horizontalHeader().setDefaultSectionSize(257)
        self.Tabela_inicio.horizontalHeader().setHighlightSections(True)
        self.Tabela_inicio.verticalHeader().setHighlightSections(True)
        self.verticalLayoutWidget_11 = QtWidgets.QWidget(self.table)
        self.verticalLayoutWidget_11.setGeometry(QtCore.QRect(840, 260, 160, 80))
        self.verticalLayoutWidget_11.setObjectName("verticalLayoutWidget_11")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_11)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        #----------------------
        self.label_16 = QtWidgets.QLabel(self.verticalLayoutWidget_11)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_6.addWidget(self.label_16)

        #Contador 
        self.contador = QtWidgets.QLCDNumber(self.verticalLayoutWidget_11)
        self.contador.setStyleSheet("background-color: rgb(206, 206, 206);\n"
"color: rgb(0, 0, 0);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.contador.setObjectName("contador")
        self.verticalLayout_6.addWidget(self.contador)
        self.verticalLayoutWidget_12 = QtWidgets.QWidget(self.table)
        self.verticalLayoutWidget_12.setGeometry(QtCore.QRect(840, 360, 160, 80))
        self.verticalLayoutWidget_12.setObjectName("verticalLayoutWidget_12")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_12)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_17 = QtWidgets.QLabel(self.verticalLayoutWidget_12)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_7.addWidget(self.label_17)
        self.contador_geral = QtWidgets.QLCDNumber(self.verticalLayoutWidget_12)
        self.contador_geral.setObjectName("contador_geral")
        #-----------------------
        
        self.verticalLayout_7.addWidget(self.contador_geral)
        self.gridLayoutWidget = QtWidgets.QWidget(self.table)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 40, 521, 91))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        #Entry nome evento
        self.entry_nome_evento = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.entry_nome_evento.setObjectName("entry_nome_evento")
        #-----------------------
        self.gridLayout.addWidget(self.entry_nome_evento, 2, 2, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_18.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);\n"
"")
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, 0, 0, 1, 3)
        self.label_20 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_20.setObjectName("label_20")
        self.gridLayout.addWidget(self.label_20, 2, 0, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_19.setObjectName("label_19")

        #Data evento
        self.gridLayout.addWidget(self.label_19, 4, 0, 1, 1)
        self.data_evento = QtWidgets.QDateEdit(self.gridLayoutWidget)
        self.data_evento.setObjectName("data_evento")
        #-----------------------
        self.gridLayout.addWidget(self.data_evento, 4, 2, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.table)
        self.label_21.setGeometry(QtCore.QRect(30, 210, 241, 31))
        self.label_21.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);\n"
"")
        self.label_21.setObjectName("label_21")
        self.infomacao_prcessos = QtWidgets.QLabel(self.table)
        self.infomacao_prcessos.setGeometry(QtCore.QRect(280, 220, 111, 16))
        self.infomacao_prcessos.setObjectName("infomacao_prcessos")

        #aba do certificado 
        self.menu_abas.addTab(self.inicial, "")
        self.aba01 = QtWidgets.QWidget()
        self.aba01.setObjectName("aba01")
        self.frame01 = QtWidgets.QFrame(self.aba01)
        self.frame01.setGeometry(QtCore.QRect(30, 20, 1031, 221))
        self.frame01.setStyleSheet("background-color: rgb(206, 206, 206);\n"
"color: rgb(0, 0, 0);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.frame01.setFrameShape(QtWidgets.QFrame.Box)
        self.frame01.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame01.setObjectName("frame01")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.frame01)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 50, 131, 131))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.label_dados1 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.label_dados1.setContentsMargins(5, 5, 5, 5)
        self.label_dados1.setObjectName("label_dados1")
        self.label_plan = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_plan.setObjectName("label_plan")
        self.label_dados1.addWidget(self.label_plan)
        self.label_power = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_power.setStyleSheet("")
        self.label_power.setObjectName("label_power")
        self.label_dados1.addWidget(self.label_power)
        self.label_salvar = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_salvar.setObjectName("label_salvar")
        self.label_dados1.addWidget(self.label_salvar)
        self.label_14 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_14.setObjectName("label_14")
        self.label_dados1.addWidget(self.label_14)
        self.label = QtWidgets.QLabel(self.frame01)
        self.label.setGeometry(QtCore.QRect(20, 10, 131, 31))
        self.label.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);\n"
"")
        self.label.setObjectName("label")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.frame01)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(150, 50, 551, 131))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.label_entrys01 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.label_entrys01.setContentsMargins(0, 0, 0, 0)
        self.label_entrys01.setObjectName("label_entrys01")
        
        #entry da planilha 
        self.entry_xlsx = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.entry_xlsx.setObjectName("entry_xlsx")
        #------------------
        
        self.label_entrys01.addWidget(self.entry_xlsx)

        #entry da power point
        self.entry_pptx = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.entry_pptx.setObjectName("entry_pptx")
        #------------------
        
        self.label_entrys01.addWidget(self.entry_pptx)


        #entry da pasta pra salvar
        self.entry_salvar = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.entry_salvar.setObjectName("entry_salvar")
        #------------------
        
        self.label_entrys01.addWidget(self.entry_salvar)

        #cocombox do evento
        self.evento_certi = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.evento_certi.setObjectName("evento_certi")
        #------------------

        
        self.label_entrys01.addWidget(self.evento_certi)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.frame01)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(710, 50, 91, 101))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.label_buttons01 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.label_buttons01.setContentsMargins(0, 0, 0, 0)
        self.label_buttons01.setObjectName("label_buttons01")
        
        #button de buscar planilha
        self.Button_xlsx = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.Button_xlsx.setObjectName("Button_xlsx")
        #-------------------
        
        self.label_buttons01.addWidget(self.Button_xlsx)
        
        #button de buscar powerpoint
        self.Button_pptx = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.Button_pptx.setObjectName("Button_pptx")
        #-------------------
        self.label_buttons01.addWidget(self.Button_pptx)

        #button de buscar pasta de salvar
        self.Button_salvar = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.Button_salvar.setObjectName("Button_salvar")
        #-------------------
        
        self.label_buttons01.addWidget(self.Button_salvar)
        self.label_2 = QtWidgets.QLabel(self.frame01)
        self.label_2.setGeometry(QtCore.QRect(810, 50, 201, 71))
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.frame02 = QtWidgets.QFrame(self.aba01)
        self.frame02.setGeometry(QtCore.QRect(30, 260, 1031, 381))
        self.frame02.setStyleSheet("background-color: rgb(206, 206, 206);\n"
"color: rgb(0, 0, 0);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.frame02.setFrameShape(QtWidgets.QFrame.Box)
        self.frame02.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame02.setObjectName("frame02")
        self.label_3 = QtWidgets.QLabel(self.frame02)
        self.label_3.setGeometry(QtCore.QRect(20, 10, 251, 31))
        self.label_3.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);\n"
"")
        self.label_3.setObjectName("label_3")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frame02)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 40, 991, 21))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.label_cert = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.label_cert.setContentsMargins(0, 0, 0, 0)
        self.label_cert.setObjectName("label_cert")
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.label_cert.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.label_cert.addWidget(self.label_5)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.frame02)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 60, 991, 26))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.label_entry_certi = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.label_entry_certi.setContentsMargins(0, 0, 0, 0)
        self.label_entry_certi.setObjectName("label_entry_certi")

        #Dados do certificado
        
        #entry de titulo do certificado
        self.entry_titulo_certi = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.entry_titulo_certi.setObjectName("entry_titulo_certi")
        #--------------------
        self.label_entry_certi.addWidget(self.entry_titulo_certi)

        #entry de data do certificado
        self.entry_data_certi = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.entry_data_certi.setObjectName("entry_data_certi")
        #--------------------
        
        self.label_entry_certi.addWidget(self.entry_data_certi)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.frame02)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(20, 100, 991, 271))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)

        #entry do texto do certificado
        self.entry_texto_ceri = QtWidgets.QTextEdit(self.verticalLayoutWidget_4)
        self.entry_texto_ceri.setObjectName("entry_texto_ceri")
        #-------------------
        self.verticalLayout.addWidget(self.entry_texto_ceri)


        #button do ok e do cancelar
        self.button_ok_cancelar = QtWidgets.QDialogButtonBox(self.aba01)
        self.button_ok_cancelar.setGeometry(QtCore.QRect(900, 640, 171, 41))
        self.button_ok_cancelar.setStyleSheet("background-color: rgb(124, 124, 124);\n"
"color: rgb(0, 0, 0);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.button_ok_cancelar.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.button_ok_cancelar.setCenterButtons(True)
        self.button_ok_cancelar.setObjectName("button_ok_cancelar")
        #------------------



#--------aba de envio de certificado ---------------------------------------------------------------------------------------------------------------------------------
        self.menu_abas.addTab(self.aba01, "")
        self.aba02 = QtWidgets.QWidget()
        self.aba02.setObjectName("aba02")
        self.frame_enviar_01 = QtWidgets.QFrame(self.aba02)
        self.frame_enviar_01.setGeometry(QtCore.QRect(30, 20, 1031, 181))
        self.frame_enviar_01.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.frame_enviar_01.setStyleSheet("background-color: rgb(206, 206, 206);\n"
"color: rgb(0, 0, 0);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.frame_enviar_01.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_enviar_01.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_enviar_01.setObjectName("frame_enviar_01")
        self.label_7 = QtWidgets.QLabel(self.frame_enviar_01)
        self.label_7.setGeometry(QtCore.QRect(20, 10, 181, 31))
        self.label_7.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);\n"
"")
        self.label_7.setObjectName("label_7")
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.frame_enviar_01)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(20, 60, 51, 91))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_2.addWidget(self.label_9)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(self.frame_enviar_01)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(70, 60, 371, 91))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.label_entry_enviar = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.label_entry_enviar.setContentsMargins(0, 4, 0, 0)
        self.label_entry_enviar.setSpacing(19)
        self.label_entry_enviar.setObjectName("label_entry_enviar")
        #entry de emial
        self.entry_email = QtWidgets.QLineEdit(self.verticalLayoutWidget_6)
        self.entry_email.setObjectName("entry_email")
        #---------------
        
        self.label_entry_enviar.addWidget(self.entry_email)
        
        #entry de senha
        self.entry_senha = QtWidgets.QLineEdit(self.verticalLayoutWidget_6)
        self.entry_senha.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.entry_senha.setText("")
        self.entry_senha.setObjectName("entry_senha")
        #--------------
        
        self.label_entry_enviar.addWidget(self.entry_senha)
        self.verticalLayoutWidget_7 = QtWidgets.QWidget(self.frame_enviar_01)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(480, 60, 201, 51))
        self.verticalLayoutWidget_7.setObjectName("verticalLayoutWidget_7")
        self.label_de_posta_combobox = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_7)
        self.label_de_posta_combobox.setContentsMargins(0, 0, 0, 0)
        self.label_de_posta_combobox.setObjectName("label_de_posta_combobox")
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget_7)
        self.label_10.setObjectName("label_10")
        self.label_de_posta_combobox.addWidget(self.label_10)
        
        #Combobox de portas
        self.portas = QtWidgets.QComboBox(self.verticalLayoutWidget_7)
        self.portas.setObjectName("portas")
        #--------------
        
        self.label_de_posta_combobox.addWidget(self.portas)
        self.frame_enviar_2 = QtWidgets.QFrame(self.aba02)
        self.frame_enviar_2.setGeometry(QtCore.QRect(30, 230, 1031, 381))
        self.frame_enviar_2.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.frame_enviar_2.setStyleSheet("background-color: rgb(206, 206, 206);\n"
"color: rgb(0, 0, 0);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.frame_enviar_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_enviar_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_enviar_2.setObjectName("frame_enviar_2")
        self.label_11 = QtWidgets.QLabel(self.frame_enviar_2)
        self.label_11.setGeometry(QtCore.QRect(20, 10, 181, 31))
        self.label_11.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);\n"
"")
        self.label_11.setObjectName("label_11")
        self.verticalLayoutWidget_8 = QtWidgets.QWidget(self.frame_enviar_2)
        self.verticalLayoutWidget_8.setGeometry(QtCore.QRect(20, 50, 391, 51))
        self.verticalLayoutWidget_8.setObjectName("verticalLayoutWidget_8")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_8)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_seleciona = QtWidgets.QLabel(self.verticalLayoutWidget_8)
        self.label_seleciona.setObjectName("label_seleciona")
        self.verticalLayout_3.addWidget(self.label_seleciona)
        
        #combobox de selecionar evento
        self.selecionar_evento = QtWidgets.QComboBox(self.verticalLayoutWidget_8)
        self.selecionar_evento.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.selecionar_evento.setObjectName("selecionar_evento")
        #-----------------------
        
        self.verticalLayout_3.addWidget(self.selecionar_evento)
        self.verticalLayoutWidget_9 = QtWidgets.QWidget(self.frame_enviar_2)
        self.verticalLayoutWidget_9.setGeometry(QtCore.QRect(480, 50, 391, 51))
        self.verticalLayoutWidget_9.setObjectName("verticalLayoutWidget_9")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_9)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_12 = QtWidgets.QLabel(self.verticalLayoutWidget_9)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_4.addWidget(self.label_12)
        
        #titulo de enviar
        self.entry_ti_enviar = QtWidgets.QLineEdit(self.verticalLayoutWidget_9)
        self.entry_ti_enviar.setObjectName("entry_ti_enviar")
        #-----------------------
        self.verticalLayout_4.addWidget(self.entry_ti_enviar)
        self.verticalLayoutWidget_10 = QtWidgets.QWidget(self.frame_enviar_2)
        self.verticalLayoutWidget_10.setGeometry(QtCore.QRect(20, 140, 851, 211))
        self.verticalLayoutWidget_10.setObjectName("verticalLayoutWidget_10")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_10)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_13 = QtWidgets.QLabel(self.verticalLayoutWidget_10)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_5.addWidget(self.label_13)
        
        #mensagem de texto
        self.menssage_envio = QtWidgets.QTextEdit(self.verticalLayoutWidget_10)
        self.menssage_envio.setObjectName("menssage_envio")
        #--------------------
        self.verticalLayout_5.addWidget(self.menssage_envio)

        #button de ok e cancela enviar
        self.button_ok_enviar = QtWidgets.QDialogButtonBox(self.aba02)
        self.button_ok_enviar.setGeometry(QtCore.QRect(890, 640, 171, 41))
        self.button_ok_enviar.setStyleSheet("background-color: rgb(124, 124, 124);\n"
"color: rgb(0, 0, 0);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.button_ok_enviar.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.button_ok_enviar.setCenterButtons(False)
        self.button_ok_enviar.setObjectName("button_ok_enviar")
        #-------------------
        
        self.menu_abas.addTab(self.aba02, "")
        self.aba03 = QtWidgets.QWidget()
        self.aba03.setObjectName("aba03")
        self.menu_abas.addTab(self.aba03, "")
        janela_principal.setCentralWidget(self.centralwidget)

        self.retranslateUi(janela_principal)
        self.menu_abas.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(janela_principal)
        
        janela_principal.setTabOrder(self.entry_xlsx, self.entry_pptx)
        janela_principal.setTabOrder(self.entry_pptx, self.entry_salvar)
        janela_principal.setTabOrder(self.entry_salvar, self.Button_xlsx)
        janela_principal.setTabOrder(self.Button_xlsx, self.menu_abas)
        janela_principal.setTabOrder(self.menu_abas, self.Button_pptx)
        janela_principal.setTabOrder(self.Button_pptx, self.Button_salvar)
        janela_principal.setTabOrder(self.Button_salvar, self.entry_titulo_certi)
        janela_principal.setTabOrder(self.entry_titulo_certi, self.entry_data_certi)
        janela_principal.setTabOrder(self.entry_data_certi, self.entry_texto_ceri)
        janela_principal.setTabOrder(self.entry_texto_ceri, self.entry_email)
        janela_principal.setTabOrder(self.entry_email, self.entry_senha)
        janela_principal.setTabOrder(self.entry_senha, self.portas)
        janela_principal.setTabOrder(self.portas, self.selecionar_evento)
        janela_principal.setTabOrder(self.selecionar_evento, self.entry_ti_enviar)
        janela_principal.setTabOrder(self.entry_ti_enviar, self.menssage_envio)

    def retranslateUi(self, janela_principal):
        _translate = QtCore.QCoreApplication.translate
        janela_principal.setWindowTitle(_translate("janela_principal", "Certified"))
        item = self.Tabela_inicio.horizontalHeaderItem(0)
        item.setText(_translate("janela_principal", "Nome "))
        item = self.Tabela_inicio.horizontalHeaderItem(1)
        item.setText(_translate("janela_principal", "Email"))
        item = self.Tabela_inicio.horizontalHeaderItem(2)
        item.setText(_translate("janela_principal", "Evento"))
        self.label_16.setText(_translate("janela_principal", "Concluidas"))
        self.label_17.setText(_translate("janela_principal", "Total "))
        self.label_18.setText(_translate("janela_principal", "Cadastro de Evento "))
        self.label_20.setText(_translate("janela_principal", "Nome    "))
        self.label_19.setText(_translate("janela_principal", "Data "))
        self.label_21.setText(_translate("janela_principal", "Monitoramento de processo"))
        
        # texto de execução
        self.infomacao_prcessos.setText(_translate("janela_principal", "[Sem processos]"))
        #-----------------------
        
        self.menu_abas.setTabText(self.menu_abas.indexOf(self.inicial), _translate("janela_principal", "Início"))
        self.label_plan.setText(_translate("janela_principal", "Planilha (.xlsx)"))
        self.label_power.setText(_translate("janela_principal", "Power P (.pptx)"))
        self.label_salvar.setText(_translate("janela_principal", "Salvar"))
        self.label_14.setText(_translate("janela_principal", "Evento"))
        self.label.setText(_translate("janela_principal", "Gerir Arquivos"))
        self.Button_xlsx.setText(_translate("janela_principal", "Buscar"))
        self.Button_pptx.setText(_translate("janela_principal", "Buscar"))
        self.Button_salvar.setText(_translate("janela_principal", "Buscar"))
        self.label_2.setText(_translate("janela_principal", "         Ordem das colunas na Planilha\n"
"     1º coluna: Nome   | 2° coluna: Email"))
        self.label_3.setText(_translate("janela_principal", "Inserir Dados da Certificação"))
        self.label_4.setText(_translate("janela_principal", "Título do Certificado"))
        self.label_5.setText(_translate("janela_principal", "Data do Certificado"))
        self.label_6.setText(_translate("janela_principal", "Texto do Certificado"))
        self.menu_abas.setTabText(self.menu_abas.indexOf(self.aba01), _translate("janela_principal", "Criar Certificado"))
        self.label_7.setText(_translate("janela_principal", "Envio de Certificados"))
        self.label_9.setText(_translate("janela_principal", "Email"))
        self.label_8.setText(_translate("janela_principal", "Senha"))
        self.label_10.setText(_translate("janela_principal", "Opções de Email"))
        self.label_11.setText(_translate("janela_principal", "Selecionar Evento"))
        self.label_seleciona.setText(_translate("janela_principal", "Selecionar Evento"))
        self.label_12.setText(_translate("janela_principal", "Título da Email"))
        self.label_13.setText(_translate("janela_principal", "Mensagem do Email"))
        self.menu_abas.setTabText(self.menu_abas.indexOf(self.aba02), _translate("janela_principal", "Enviar Certificado"))
        self.menu_abas.setTabText(self.menu_abas.indexOf(self.aba03), _translate("janela_principal", "Disparar Mensagem"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    janela_principal = QtWidgets.QMainWindow()
    ui = Ui_janela_principal()
    ui.setupUi(janela_principal)
    janela_principal.show()
    sys.exit(app.exec_())
