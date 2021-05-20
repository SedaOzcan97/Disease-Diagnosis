# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LOGİNFORM.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets 
import sys
from PyQt5.QtCore import QSize
from PyQt5 import QtCore, QtGui, QtWidgets as Q
from PyQt5.QtGui import QImage, QPalette, QBrush
from PyQt5.QtWidgets import *

from CREATEACCOUNT import Ui_signup as signup
import sqlite3

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s
try:
    _encoding =QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_Dialog(object):
    def showMessageBox(self,title,message):
        msgBox = QtGui.QMessageBox()
        msgBox.setIcon(QtGui.QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
        msgBox.exec_()
  
    def signUpShow(self):
        self.CREATEACCOUNT = QtGui.Qsignup()
        self. ui = Ui_signup()
        self.ui.setupUi(self.CREATEACCOUNT)
        self.CREATEACCOUNT.show()

    def loginCheck(self):
        username = self.username_lineEdit.text()
        password = self.password_lineEdit.text()

        connection = sqlite3.connect("login.db")
        result = connection.execute("SELECT * FROM USERS WHERE USERNAME = ? AND PASSWORD = ?",(username,password))
        if (len(result.fetchall()) >0 ):
            print("USER FOUND!")
          
        else:
            print("USER NOT FOUND!")

    def Button_clicked(self):
            print("user added succesfully!")
    def openWindow(self):
        self.window= QWidgets.Qsignup
        self.ui= Ui_signup()
        self.ui.setupUi(self.window)
        self.window.show()


    def signupCheck(self):
        print("signup !")
        self.signUpShow()
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(644, 405)
        Dialog.setStyleSheet("QWidget#Form {background-image: url(5c8cf89945d2a05010d25979.jpg);}")
        self.username_label = QtWidgets.QLabel(Dialog)
        self.username_label.setGeometry(QtCore.QRect(230, 250, 91, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.username_label.setFont(font)
        self.username_label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(85, 170, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"")
        self.username_label.setObjectName("username_label")
        self.password_label = QtWidgets.QLabel(Dialog)
        self.password_label.setGeometry(QtCore.QRect(230, 290, 81, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.password_label.setFont(font)
        self.password_label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(85, 170, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.password_label.setObjectName("password_label")
        self.username_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.username_lineEdit.setGeometry(QtCore.QRect(330, 260, 131, 22))
        self.username_lineEdit.setObjectName("username_lineEdit")
        self.password_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.password_lineEdit.setGeometry(QtCore.QRect(330, 290, 131, 22))
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.login_pushButton = QtWidgets.QPushButton(Dialog)
        self.login_pushButton.setGeometry(QtCore.QRect(230, 330, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.login_pushButton.setFont(font)
        self.login_pushButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(85, 170, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.login_pushButton.setObjectName("login_pushButton")
        ####buttton event####
        self.login_pushButton.clicked.connect(self.loginCheck)
        #####################
        self.signup_pushButton = QtWidgets.QPushButton(Dialog)
        self.signup_pushButton.setGeometry(QtCore.QRect(350, 330, 101, 41))
        ####button event####
        #self.signup_pushButton.clicked.connect(self.signupCheck)
        self.signup_pushButton.clicked.connect(self.openWindow)
        ####################
        font = QtGui.QFont()
        font.setPointSize(12)
        self.signup_pushButton.setFont(font)
        self.signup_pushButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(85, 170, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.signup_pushButton.setObjectName("signup_pushButton")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(260, 210, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(44, 0, 67);\n"
"")
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.username_label.setText(_translate("Dialog", "USERNAME:"))
        self.password_label.setText(_translate("Dialog", "PASSWORD:"))
        self.login_pushButton.setText(_translate("Dialog", "LOGIN"))
        self.signup_pushButton.setText(_translate("Dialog", "SIGN UP"))
        self.label.setText(_translate("Dialog", "LOGIN FORM"))





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
