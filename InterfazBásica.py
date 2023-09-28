
from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from azure.cognitiveservices.vision.customvision.training.models import ImageFileCreateBatch, ImageFileCreateEntry, Region
from msrest.authentication import ApiKeyCredentials
from PyQt5 import QtCore, QtGui, QtWidgets
from conexion import ConexionCustomVision
from ConexionTraslator import ConexionTranlator
import requests, uuid, json
from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
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
        self.lblURL.setGeometry(QtCore.QRect(60, 110, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.lblURL.setFont(font)
        self.lblURL.setTextFormat(QtCore.Qt.PlainText)
        self.lblURL.setWordWrap(False)
        self.lblURL.setIndent(1)
        self.lblURL.setObjectName("lblURL")
        self.lblFile = QtWidgets.QLabel(self.centralwidget)
        self.lblFile.setGeometry(QtCore.QRect(60, 200, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.lblFile.setFont(font)
        self.lblFile.setTextFormat(QtCore.Qt.PlainText)
        self.lblFile.setWordWrap(False)
        self.lblFile.setIndent(1)
        self.lblFile.setObjectName("lblFile")
        self.btnCustomVisionURL = QtWidgets.QPushButton(self.centralwidget)
        self.btnCustomVisionURL.setGeometry(QtCore.QRect(480, 110, 101, 51))
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
        self.lblFile_2.setGeometry(QtCore.QRect(60, 310, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.lblFile_2.setFont(font)
        self.lblFile_2.setTextFormat(QtCore.Qt.PlainText)
        self.lblFile_2.setWordWrap(False)
        self.lblFile_2.setIndent(1)
        self.lblFile_2.setObjectName("lblFile_2")
        self.btnCustomVisionFILE = QtWidgets.QPushButton(self.centralwidget)
        self.btnCustomVisionFILE.setGeometry(QtCore.QRect(480, 200, 101, 51))
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
        self.lineEditURL.setGeometry(QtCore.QRect(110, 110, 351, 51))
        self.lineEditURL.setObjectName("lineEditURL")
        self.lineEditFILE = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditFILE.setGeometry(QtCore.QRect(110, 200, 351, 51))
        self.lineEditFILE.setObjectName("lineEditFILE")
        self.lineEditResult = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditResult.setGeometry(QtCore.QRect(170, 300, 231, 51))
        self.lineEditResult.setObjectName("lineEditResult")
        self.btnCustomVisionCLEAR = QtWidgets.QPushButton(self.centralwidget)
        self.btnCustomVisionCLEAR.setGeometry(QtCore.QRect(590, 20, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btnCustomVisionCLEAR.setFont(font)
        self.btnCustomVisionCLEAR.setMouseTracking(True)
        self.btnCustomVisionCLEAR.setAutoFillBackground(False)
        self.btnCustomVisionCLEAR.setObjectName("btnCustomVisionCLEAR")
        self.comboBoxTRANSLATOR = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxTRANSLATOR.setGeometry(QtCore.QRect(60, 440, 311, 51))
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
        self.lineEditResultTRANSLATOR.setGeometry(QtCore.QRect(390, 440, 331, 51))
        self.lineEditResultTRANSLATOR.setObjectName("lineEditResultTRANSLATOR")
        self.btnTRANLATOR = QtWidgets.QPushButton(self.centralwidget)
        self.btnTRANLATOR.setGeometry(QtCore.QRect(300, 500, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btnTRANLATOR.setFont(font)
        self.btnTRANLATOR.setMouseTracking(True)
        self.btnTRANLATOR.setAutoFillBackground(False)
        self.btnTRANLATOR.setObjectName("btnTRANLATOR")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 763, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.btnCustomVisionCLEAR.clicked.connect(self.clear_INPUT)                        
        self.btnCustomVisionURL.clicked.connect(self.input_URL)  
        self.btnCustomVisionFILE.clicked.connect(self.input_FILE)  
        self.btnTRANLATOR.clicked.connect(self.trasnlator_INPUT)        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def clear_INPUT(self):
        self.lineEditFILE.setText("")
        self.lineEditResult .setText("")
        self.lineEditURL.setText("")             
        self.lineEditResultTRANSLATOR.setText("")        
        self.comboBoxTRANSLATOR.itemText(0)        

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
        #name = "Objeto: " + name + ", Probability: " + str(y)        
        self.lineEditResult.setText(name)             
        
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
                
    def trasnlator_INPUT(self):
        result = self.lineEditResult.text()
        idioma = self.comboBoxTRANSLATOR.currentText()                                
        body = [{
            'text': result
        }]
        
        idiomas = {"FRANCES" : "fr",
                   "INGLES": "en",
                   "PORTUGUES": "pt",}                                    
        conn = ConexionTranlator()                
        request = requests.post(conn.constructed_url, params=conn.params, headers=conn.headers, json=body)    
        response = request.json()
        x = response[0]        
        y = []
        for i in x["translations"]:    
            y.append(i)
            
        for j in y:
            if idiomas[idioma] == j['to']:
                self.lineEditResultTRANSLATOR.setText(j["text"])                
        
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
        self.btnTRANLATOR.setText(_translate("MainWindow", "TRANSLATOR"))


