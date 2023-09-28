from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from azure.cognitiveservices.vision.customvision.training.models import ImageFileCreateBatch, ImageFileCreateEntry, Region
from msrest.authentication import ApiKeyCredentials
from PyQt5 import QtCore, QtGui, QtWidgets
from conexion import ConexionCustomVinsion
from InterfazBásica import Ui_MainWindow 
import sys

if __name__ == "__main__":        
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)        
    MainWindow.show()
    sys.exit(app.exec_())

