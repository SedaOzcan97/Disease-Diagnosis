# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CREATEACCOUNT.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
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



class Ui_signup(object):

    def insertData(self):
        username = self.uname_lineEdit.text()
        email = self.mail_lineEdit_3.text()
        password = self.pass_lineEdit_2.text()

        connection = sqlite3.connect("login.db")
        connection.execute("INSERT INTO USERS VALUES(?,?,?)", (username, email, password))

        connection.commit()

        connection.close()


    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(665, 403)
        Dialog.setAutoFillBackground(False)
        Dialog.setStyleSheet("QWidget#Form {background-image: url(5c8cf89945d2a05010d25979.jpg);}")
        self.createacc_label = QtWidgets.QLabel(Dialog)
        self.createacc_label.setGeometry(QtCore.QRect(220, 220, 291, 51))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.createacc_label.setFont(font)
        self.createacc_label.setAutoFillBackground(False)
        self.createacc_label.setStyleSheet("color: rgb(56, 0, 85);")
        self.createacc_label.setObjectName("createacc_label")
        self.uname_label_2 = QtWidgets.QLabel(Dialog)
        self.uname_label_2.setGeometry(QtCore.QRect(340, 260, 81, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.uname_label_2.setFont(font)
        self.uname_label_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(85, 170, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.uname_label_2.setObjectName("uname_label_2")
        self.pass_label_3 = QtWidgets.QLabel(Dialog)
        self.pass_label_3.setGeometry(QtCore.QRect(340, 290, 81, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.pass_label_3.setFont(font)
        self.pass_label_3.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(85, 170, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.pass_label_3.setObjectName("pass_label_3")
        self.mail_label_4 = QtWidgets.QLabel(Dialog)
        self.mail_label_4.setGeometry(QtCore.QRect(340, 320, 81, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.mail_label_4.setFont(font)
        self.mail_label_4.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(85, 170, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.mail_label_4.setObjectName("mail_label_4")
        self.uname_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.uname_lineEdit.setGeometry(QtCore.QRect(450, 260, 161, 22))
        self.uname_lineEdit.setObjectName("uname_lineEdit")
        self.pass_lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.pass_lineEdit_2.setGeometry(QtCore.QRect(450, 290, 161, 22))
        self.pass_lineEdit_2.setObjectName("pass_lineEdit_2")
        self.mail_lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.mail_lineEdit_3.setGeometry(QtCore.QRect(450, 320, 161, 22))
        self.mail_lineEdit_3.setObjectName("mail_lineEdit_3")
        self.createaccount_pushButton = QtWidgets.QPushButton(Dialog)
        self.createaccount_pushButton.setGeometry(QtCore.QRect(470, 350, 131, 41))

        
        font = QtGui.QFont()
        font.setPointSize(12)
        self.createaccount_pushButton.setFont(font)
        self.createaccount_pushButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(85, 170, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.createaccount_pushButton.setObjectName("createaccount_pushButton")
        
        ############Event############
        self.createaccount_pushButton.clicked.connect(self.insertData)
        ###############################
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)



    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.createacc_label.setText(_translate("Dialog", "CREATE ACCOUNT"))
        self.uname_label_2.setText(_translate("Dialog", "USERNAME:"))
        self.pass_label_3.setText(_translate("Dialog", "PASSWORD:"))
        self.mail_label_4.setText(_translate("Dialog", "E-MAİL:"))
        self.createaccount_pushButton.setText(_translate("Dialog", "SIGN UP"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_signup()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
