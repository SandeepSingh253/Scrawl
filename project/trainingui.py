# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'training.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import mnist_loader
import network
from PyQt5 import QtCore, QtGui, QtWidgets
from threading import *
from PyQt5.QtWidgets import (QWidget, QApplication,QPushButton, 
                             QVBoxLayout)
from PyQt5.QtCore import QThread
import time, threading, sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(720, 405)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.monitor_evaluation_accuracy_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.monitor_evaluation_accuracy_checkBox.setGeometry(QtCore.QRect(40, 200, 181, 21))
        self.monitor_evaluation_accuracy_checkBox.setObjectName("monitor_evaluation_accuracy_checkBox")
        self.train_network_button = QtWidgets.QPushButton(self.centralwidget)
        self.train_network_button.setGeometry(QtCore.QRect(40, 250, 91, 31))
        self.train_network_button.setObjectName("train_network_button")
        self.monitor_training_cost_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.monitor_training_cost_checkBox.setGeometry(QtCore.QRect(40, 160, 141, 21))
        self.monitor_training_cost_checkBox.setObjectName("monitor_training_cost_checkBox")
        self.monitor_training_accuracy_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.monitor_training_accuracy_checkBox.setGeometry(QtCore.QRect(40, 80, 161, 21))
        self.monitor_training_accuracy_checkBox.setObjectName("monitor_training_accuracy_checkBox")
        self.monitor_evaluation_cost_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.monitor_evaluation_cost_checkBox.setGeometry(QtCore.QRect(40, 120, 161, 21))
        self.monitor_evaluation_cost_checkBox.setObjectName("monitor_evaluation_cost_checkBox")
        self.traningProgressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.traningProgressBar.setGeometry(QtCore.QRect(10, 360, 711, 23))
        self.traningProgressBar.setProperty("value", 0)
        self.traningProgressBar.setObjectName("traningProgressBar")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 720, 405))
        self.label.setStyleSheet("background-image: url(:/newPrefix/whiteback.jpg);")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/newPrefix/whiteback.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 340, 101, 16))
        self.label_2.setObjectName("label_2")
        self.label.raise_()
        self.monitor_evaluation_accuracy_checkBox.raise_()
        self.train_network_button.raise_()
        self.monitor_training_cost_checkBox.raise_()
        self.monitor_training_accuracy_checkBox.raise_()
        self.monitor_evaluation_cost_checkBox.raise_()
        self.traningProgressBar.raise_()
        self.label_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.train_network_button.clicked.connect(self.on_click)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def on_click(self):
        global monit_e_a,monit_e_c,monit_t_a,monit_t_c,progBar
        progBar=self.traningProgressBar
        monit_e_a=self.monitor_evaluation_accuracy_checkBox.isChecked()
        monit_e_c=self.monitor_evaluation_cost_checkBox.isChecked()
        monit_t_a=self.monitor_training_accuracy_checkBox.isChecked()
        monit_t_c=self.monitor_training_cost_checkBox.isChecked()
        self.worker = Worker()
        self.worker.run()

    def closeEvent(self,event):
        print('Closing')
        self.worker.terminate()
        event.accept()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Training Network"))
        self.monitor_evaluation_accuracy_checkBox.setText(_translate("MainWindow", "monitor evaluation accuracy"))
        self.train_network_button.setText(_translate("MainWindow", "Train Network"))
        self.monitor_training_cost_checkBox.setText(_translate("MainWindow", "monitor training cost"))
        self.monitor_training_accuracy_checkBox.setText(_translate("MainWindow", "monitor training accuracy"))
        self.monitor_evaluation_cost_checkBox.setText(_translate("MainWindow", "monitor evaluation cost"))
        self.label_2.setText(_translate("MainWindow", "Traning Progress"))

import traningbackimage_rc

class Worker(QThread):

    def _init_(self):
        QThread._init_(self)

    def run(self):
        training_data, validation_data, test_data = \
        mnist_loader.load_data_wrapper()
        self.net = network.Network([784, 30, 10], cost=network.CrossEntropyCost)
        self.net.SGD(training_data, 30, 10, 0.5,progBar,lmbda = 5.0,evaluation_data=validation_data,monitor_evaluation_accuracy=monit_e_a,monitor_evaluation_cost=monit_e_c,monitor_training_accuracy=monit_t_a,monitor_training_cost=monit_t_c)
        
        self.net.save("trained_data")

# app = QtWidgets.QApplication(sys.argv)
# MainWindow = QtWidgets.QMainWindow()
# ui = Ui_MainWindow()
# ui.setupUi(MainWindow)
# MainWindow.show()
# sys.exit(app.exec_())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    # # Create splashscreen
    # splash_pix = QtGui.QPixmap('logo-color.jpg')
    # splash = QtWidgets.QSplashScreen(splash_pix, QtCore.Qt.WindowStaysOnTopHint)
    # # add fade to splashscreen 
    # opaqueness = 0.0
    # step = 0.2
    # splash.setWindowOpacity(opaqueness)
    # splash.show()
    # while opaqueness <= 1:
    #     splash.setWindowOpacity(opaqueness)
    #     time.sleep(step) # Gradually appears
    #     opaqueness+=step
    # time.sleep(1) # hold image on screen for a while
    # splash.close() # close the splash screen

    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())