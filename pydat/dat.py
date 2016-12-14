#!/usr/bin/env python3

from PyQt5.uic import loadUiType
from PyQt5 import QtCore, QtWidgets
import sys



from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)
    
import os
uipath = os.path.join(os.path.dirname(os.path.abspath(__file__)),"ui")

Ui_MainWindow, QMainWindow = loadUiType(os.path.join(uipath,'dat.ui'))

from scipy import signal
        
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, ):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)

        self.actionQuit.triggered.connect(self.quit)
        
      
    def ping(self):
        print("pong")
        
    def actionOpen(self):
        print("self.actionOpen")

    def quit(self):
        print("Well, bye.")
        QtWidgets.QApplication.quit()
                
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)  # A new instance of QApplication
    main = MainWindow() 
    main.show()
    sys.exit(app.exec_())
