from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from azure.cognitiveservices.vision.customvision.training.models import ImageFileCreateBatch, ImageFileCreateEntry, Region
from msrest.authentication import ApiKeyCredentials
import os, time, uuid
from conexion import ConexionCustomVinsion
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(763, 641)
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
        self.lblURL.setGeometry(QtCore.QRect(70, 150, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.lblURL.setFont(font)
        self.lblURL.setTextFormat(QtCore.Qt.PlainText)
        self.lblURL.setWordWrap(False)
        self.lblURL.setIndent(1)
        self.lblURL.setObjectName("lblURL")
        self.lblFile = QtWidgets.QLabel(self.centralwidget)
        self.lblFile.setGeometry(QtCore.QRect(70, 240, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.lblFile.setFont(font)
        self.lblFile.setTextFormat(QtCore.Qt.PlainText)
        self.lblFile.setWordWrap(False)
        self.lblFile.setIndent(1)
        self.lblFile.setObjectName("lblFile")
        self.btnCustomVisionURL = QtWidgets.QPushButton(self.centralwidget)
        self.btnCustomVisionURL.setGeometry(QtCore.QRect(490, 150, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btnCustomVisionURL.setFont(font)
        self.btnCustomVisionURL.setMouseTracking(True)
        self.btnCustomVisionURL.setAutoFillBackground(False)
        self.btnCustomVisionURL.setObjectName("btnCustomVisionURL")
        self.lblFile_2 = QtWidgets.QLabel(self.centralwidget)
        self.lblFile_2.setGeometry(QtCore.QRect(70, 350, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.lblFile_2.setFont(font)
        self.lblFile_2.setTextFormat(QtCore.Qt.PlainText)
        self.lblFile_2.setWordWrap(False)
        self.lblFile_2.setIndent(1)
        self.lblFile_2.setObjectName("lblFile_2")
        self.btnCustomVisionFILE = QtWidgets.QPushButton(self.centralwidget)
        self.btnCustomVisionFILE.setGeometry(QtCore.QRect(490, 240, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btnCustomVisionFILE.setFont(font)
        self.btnCustomVisionFILE.setMouseTracking(True)
        self.btnCustomVisionFILE.setAutoFillBackground(False)
        self.btnCustomVisionFILE.setObjectName("btnCustomVisionFILE")
        self.lineEditURL = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditURL.setGeometry(QtCore.QRect(120, 150, 351, 61))
        self.lineEditURL.setObjectName("lineEditURL")
        self.lineEditFILE = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditFILE.setGeometry(QtCore.QRect(120, 240, 351, 61))
        self.lineEditFILE.setObjectName("lineEditFILE")
        self.lineEditResult = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditResult.setGeometry(QtCore.QRect(180, 340, 231, 51))
        self.lineEditResult.setObjectName("lineEditResult")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 763, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.btnCustomVisionURL.clicked.connect(self.input_URL)                        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)           
    
    def input_URL(self, predit):
        prediccion = ConexionCustomVinsion()
        predit = prediccion.conn()  
        img = self.lineEditURL.text()
        results = predit.classify_image_url(prediccion.project_id, prediccion.model, img)
        data = {}
        y = 0
        name = ""                
        for prediction in results.predictions:            
            if prediction.probability > y :
                name = prediction.tag_name 
                y = prediction.probability
        name = "Objeto: " + name + ", Probability: " + str(y)        
        self.lineEditResult.setText(name)                        
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lblURL.setText(_translate("MainWindow", "URL"))
        self.lblFile.setText(_translate("MainWindow", "FILE"))
        self.btnCustomVisionURL.setText(_translate("MainWindow", "Upload"))
        self.lblFile_2.setText(_translate("MainWindow", "RESULT"))
        self.btnCustomVisionFILE.setText(_translate("MainWindow", "Upload"))



