from PyQt5 import QtCore, QtGui, QtWidgets
from InterfazBásica import Ui_MainWindow 
import sys


#implementación de interfaz y servicios Azure 
if __name__ == "__main__":        
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)        
    MainWindow.show()
    sys.exit(app.exec_())

