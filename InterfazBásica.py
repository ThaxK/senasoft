#importacion de clases y librerias para interfaz
from PyQt5 import QtCore, QtGui, QtWidgets
from conexion import ConexionCustomVision
from conexionTranslator import ConexionTranslator
import requests, uuid, json
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    #creacion de la interfaz grafica, código autogenerado desde pyqt5
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(763, 800)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(56, 56, 56))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(56, 56, 56))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        MainWindow.setPalette(palette)
        icon = QtGui.QIcon.fromTheme("hole")
        MainWindow.setWindowIcon(icon)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lblURL = QtWidgets.QLabel(self.centralwidget)
        self.lblURL.setGeometry(QtCore.QRect(80, 170, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.lblURL.setFont(font)
        self.lblURL.setTextFormat(QtCore.Qt.PlainText)
        self.lblURL.setWordWrap(False)
        self.lblURL.setIndent(1)
        self.lblURL.setObjectName("lblURL")
        self.lblFile = QtWidgets.QLabel(self.centralwidget)
        self.lblFile.setGeometry(QtCore.QRect(80, 260, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.lblFile.setFont(font)
        self.lblFile.setTextFormat(QtCore.Qt.PlainText)
        self.lblFile.setWordWrap(False)
        self.lblFile.setIndent(1)
        self.lblFile.setObjectName("lblFile")
        self.btnCustomVisionURL = QtWidgets.QPushButton(self.centralwidget)
        self.btnCustomVisionURL.setGeometry(QtCore.QRect(500, 170, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btnCustomVisionURL.setFont(font)
        self.btnCustomVisionURL.setMouseTracking(True)
        self.btnCustomVisionURL.setAutoFillBackground(False)
        self.btnCustomVisionURL.setObjectName("btnCustomVisionURL")    
        self.lblFile_2 = QtWidgets.QLabel(self.centralwidget)
        self.lblFile_2.setGeometry(QtCore.QRect(80, 370, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.lblFile_2.setFont(font)
        self.lblFile_2.setTextFormat(QtCore.Qt.PlainText)
        self.lblFile_2.setWordWrap(False)
        self.lblFile_2.setIndent(1)
        self.lblFile_2.setObjectName("lblFile_2")
        self.btnCustomVisionFILE = QtWidgets.QPushButton(self.centralwidget)
        self.btnCustomVisionFILE.setGeometry(QtCore.QRect(500, 260, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btnCustomVisionFILE.setFont(font)
        self.btnCustomVisionFILE.setMouseTracking(True)
        self.btnCustomVisionFILE.setAutoFillBackground(False)
        self.btnCustomVisionFILE.setObjectName("btnCustomVisionFILE")
        self.lineEditURL = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditURL.setGeometry(QtCore.QRect(130, 170, 351, 51))
        self.lineEditURL.setObjectName("lineEditURL")
        self.lineEditFILE = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditFILE.setGeometry(QtCore.QRect(130, 260, 351, 51))
        self.lineEditFILE.setObjectName("lineEditFILE")
        self.lineEditResult = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditResult.setGeometry(QtCore.QRect(190, 360, 231, 51))
        self.lineEditResult.setObjectName("lineEditResult")
        self.btnCustomVisionCLEAR = QtWidgets.QPushButton(self.centralwidget)
        self.btnCustomVisionCLEAR.setGeometry(QtCore.QRect(470, 370, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btnCustomVisionCLEAR.setFont(font)
        self.btnCustomVisionCLEAR.setMouseTracking(True)
        self.btnCustomVisionCLEAR.setAutoFillBackground(False)
        self.btnCustomVisionCLEAR.setObjectName("btnCustomVisionCLEAR")
        self.comboBoxTRANSLATOR = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxTRANSLATOR.setGeometry(QtCore.QRect(80, 500, 311, 51))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.comboBoxTRANSLATOR.setFont(font)
        self.comboBoxTRANSLATOR.setObjectName("comboBoxTRANSLATOR")
        self.comboBoxTRANSLATOR.addItem("")
        self.comboBoxTRANSLATOR.addItem("")
        self.comboBoxTRANSLATOR.addItem("")
        self.comboBoxTRANSLATOR.addItem("")
        self.lineEditResultTRANSLATOR = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditResultTRANSLATOR.setGeometry(QtCore.QRect(410, 500, 331, 51))
        self.lineEditResultTRANSLATOR.setObjectName("lineEditResultTRANSLATOR")
        self.btnTRANLATOR = QtWidgets.QPushButton(self.centralwidget)
        self.btnTRANLATOR.setGeometry(QtCore.QRect(320, 560, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btnTRANLATOR.setFont(font)
        self.btnTRANLATOR.setMouseTracking(True)
        self.btnTRANLATOR.setAutoFillBackground(False)
        self.btnTRANLATOR.setObjectName("btnTRANLATOR")
        self.lblURL_2 = QtWidgets.QLabel(self.centralwidget)
        self.lblURL_2.setGeometry(QtCore.QRect(0, 0, 800, 71))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(28)
        self.lblURL_2.setFont(font)
        self.lblURL_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lblURL_2.setStyleSheet("background-color: #0078d7; color: white \n""")
        self.lblURL_2.setTextFormat(QtCore.Qt.PlainText)
        self.lblURL_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lblURL_2.setWordWrap(False)
        self.lblURL_2.setIndent(1)
        self.lblURL_2.setObjectName("lblURL_2")
        self.lblURL_3 = QtWidgets.QLabel(self.centralwidget)
        self.lblURL_3.setGeometry(QtCore.QRect(130, 140, 331, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.lblURL_3.setFont(font)
        self.lblURL_3.setTextFormat(QtCore.Qt.PlainText)
        self.lblURL_3.setWordWrap(False)
        self.lblURL_3.setIndent(1)
        self.lblURL_3.setObjectName("lblURL_3")
        self.lblURL_4 = QtWidgets.QLabel(self.centralwidget)
        self.lblURL_4.setGeometry(QtCore.QRect(130, 230, 371, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.lblURL_4.setFont(font)
        self.lblURL_4.setTextFormat(QtCore.Qt.PlainText)
        self.lblURL_4.setWordWrap(False)
        self.lblURL_4.setIndent(1)
        self.lblURL_4.setObjectName("lblURL_4")
        self.lblURL_5 = QtWidgets.QLabel(self.centralwidget)
        self.lblURL_5.setGeometry(QtCore.QRect(200, 330, 371, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.lblURL_5.setFont(font)
        self.lblURL_5.setTextFormat(QtCore.Qt.PlainText)
        self.lblURL_5.setWordWrap(False)
        self.lblURL_5.setIndent(1)
        self.lblURL_5.setObjectName("lblURL_5")
        self.lblURL_6 = QtWidgets.QLabel(self.centralwidget)
        self.lblURL_6.setGeometry(QtCore.QRect(140, 460, 501, 41))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.lblURL_6.setFont(font)
        self.lblURL_6.setTextFormat(QtCore.Qt.PlainText)
        self.lblURL_6.setWordWrap(False)
        self.lblURL_6.setIndent(1)
        self.lblURL_6.setObjectName("lblURL_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 763, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        #Cambio colores botones
        self.btnCustomVisionURL.setStyleSheet("background-color: #0078d7; color: white")
        self.btnCustomVisionFILE.setStyleSheet("background-color: #0078d7; color: white")
        self.btnCustomVisionCLEAR.setStyleSheet("background-color: #0078d7; color: white")
        self.btnTRANLATOR.setStyleSheet("background-color: #0078d7; color: white")
        
        #Configuración de Botones
        self.btnCustomVisionCLEAR.clicked.connect(self.clear_INPUT)                        
        self.btnCustomVisionURL.clicked.connect(self.input_URL)  
        self.btnCustomVisionFILE.clicked.connect(self.input_FILE)  
        self.btnTRANLATOR.clicked.connect(self.trasnlator_INPUT) 

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
     
    #Creacion del metodo limpiar inputs   
    def clear_INPUT(self):
        self.lineEditFILE.setText("")
        self.lineEditResult .setText("")
        self.lineEditURL.setText("")             
        self.lineEditResultTRANSLATOR.setText("")        
        self.comboBoxTRANSLATOR.itemText(0)        
    
    #Creacion del metodo clasificaión por URL
    def input_URL(self, predit):
        prediccion = ConexionCustomVision()
        predit = prediccion.conn()  
        img = self.lineEditURL.text()
        results = predit.classify_image_url(prediccion.project_id, prediccion.model, img)
        
        y = 0
        name = ""                
        for prediction in results.predictions:            
            if prediction.probability > y :
                name = prediction.tag_name 
                y = prediction.probability 
    
        self.lineEditResult.setText(name)             
    
    #Creacion del metodo clasificaión por arhivo en equipo    
    def input_FILE(self, predit):
        prediccion = ConexionCustomVision()
        predit = prediccion.conn()  
        img = self.lineEditFILE.text()
        
        with open(img, "rb") as image_contents:
            results = predit.classify_image(prediccion.project_id, prediccion.model, image_contents.read())
        y = 0
        name = ""                
        for prediction in results.predictions:            
            if prediction.probability > y :
                name = prediction.tag_name 
                y = prediction.probability 
        #name = "Objeto: " + name + ", Probability: " + str(y)        
        self.lineEditResult.setText(name)    
                
    #Creacion del metodo traducción de respuesta            
    def trasnlator_INPUT(self):
        result = self.lineEditResult.text()
        idioma = self.comboBoxTRANSLATOR.currentText()                                
        body = [{
            'text': result
        }]
        
        idiomas = {"FRANCES" : "fr",
                   "INGLES": "en",
                   "PORTUGUES": "pt",}                                    
        conn = ConexionTranslator()               
        request = requests.post(conn.constructed_url, params=conn.params, headers=conn.headers, json=body)    
        response = request.json()
        x = response[0]        
        y = []
        for i in x["translations"]:    
            y.append(i)
            
        for j in y:
            if idiomas[idioma] == j['to']:
                self.lineEditResultTRANSLATOR.setText(j["text"])         
        
    #creacion de nombres y funciones de la interfaz grafica
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lblURL.setText(_translate("MainWindow", "URL"))
        self.lblFile.setText(_translate("MainWindow", "FILE"))
        self.btnCustomVisionURL.setText(_translate("MainWindow", "Upload"))
        self.lblFile_2.setText(_translate("MainWindow", "RESULT"))
        self.btnCustomVisionFILE.setText(_translate("MainWindow", "Upload"))
        self.btnCustomVisionCLEAR.setText(_translate("MainWindow", "CLEAR"))
        self.comboBoxTRANSLATOR.setItemText(0, _translate("MainWindow", "Select the translation language"))
        self.comboBoxTRANSLATOR.setItemText(1, _translate("MainWindow", "INGLES"))
        self.comboBoxTRANSLATOR.setItemText(2, _translate("MainWindow", "FRANCES"))
        self.comboBoxTRANSLATOR.setItemText(3, _translate("MainWindow", "PORTUGUES"))
        self.btnTRANLATOR.setText(_translate("MainWindow", "TRANSLATE"))
        self.lblURL_2.setText(_translate("MainWindow", "TURINGTAGGER"))
        self.lblURL_3.setText(_translate("MainWindow", "Enter the URL of the image you want to classify"))
        self.lblURL_4.setText(_translate("MainWindow", "Enter the location of the file you want to classify"))
        self.lblURL_5.setText(_translate("MainWindow", "Our AI classified your image as:"))
        self.lblURL_6.setText(_translate("MainWindow", "Select the language into which you want to translate the classification result"))



