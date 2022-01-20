# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from welcome import Ui_MainWindow
from signup import Ui_Dialog1
import sqlite3

class Ui_Dialog(object):
    def showMsgBox(self,title,message):
        msgbox = QtGui.QMessageBox()
        msgbox.setIcon(QtGui.QMessageBox.Warning)
        msgbox.setWindowTitle(title)
        msgbox.setText(message)
        msgbox.setStandardButtons(QtGui.QMessageBox.OK)
        msgbox.exec_()

    def signupshow(self):
        self.signupWindow=QtGui.QDialog()
        self.ui=Ui_Dialog1()
        self.ui.setupUi(self.signupWindow)
        self.signupWindow.show()
        
    def welcomeWindowshow(self):
        self.welcomewindow=QtGui.QMainWindow()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self.welcomewindow)
        self.welcomewindow.show()
    def loginCheck(self):
        print("Login button clicked")
        username=username_lineEdit.text()
        password=password_lineEdit.text()

        connection=sqlite3.connect("login.db")
        result=connection.execute("SELECT * FROM USERS WHERE USERNAME=? AND PASSWORD=?",(username,password))
        if(len(result.fetchall())>0):
            print("user found! ")
            self.welcomeWindowshow()
            
        else:
            print("user not found")
    
    def signupCheck(self) :
        print("signup button clicked")
        self.signupshow()
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(751, 456)
        Dialog.setStyleSheet("QDialog{\n"
"background-color: rgb(160, 255, 140);\n"
"}")
        self.username_label = QtWidgets.QLabel(Dialog)
        self.username_label.setGeometry(QtCore.QRect(230, 200, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.username_label.setFont(font)
        self.username_label.setAlignment(QtCore.Qt.AlignCenter)
        self.username_label.setObjectName("username_label")
        self.password_label = QtWidgets.QLabel(Dialog)
        self.password_label.setGeometry(QtCore.QRect(230, 260, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.password_label.setFont(font)
        self.password_label.setAlignment(QtCore.Qt.AlignCenter)
        self.password_label.setWordWrap(False)
        self.password_label.setObjectName("password_label")
        self.login_btn = QtWidgets.QPushButton(Dialog)
        self.login_btn.setGeometry(QtCore.QRect(300, 320, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Typewriter")
        font.setBold(True)
        font.setWeight(75)
        self.login_btn.setFont(font)
        self.login_btn.setObjectName("login_btn")
        ########################### Button Event#####################################
        self.login_btn.clicked.connect(self.loginCheck)
        #############################################################################
        self.signup_btn = QtWidgets.QPushButton(Dialog)
        self.signup_btn.setGeometry(QtCore.QRect(410, 320, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Typewriter")
        font.setBold(True)
        font.setWeight(75)
        self.signup_btn.setFont(font)
        self.signup_btn.setObjectName("signup_btn")
        ############################ Button Event ####################
        self.signup_btn.clicked.connect(self.signupCheck)
        ###############################################################
        self.username_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.username_lineEdit.setGeometry(QtCore.QRect(360, 200, 113, 20))
        self.username_lineEdit.setObjectName("username_lineEdit")
        self.password_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.password_lineEdit.setGeometry(QtCore.QRect(360, 260, 113, 20))
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(280, 30, 211, 71))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "login form"))
        self.username_label.setText(_translate("Dialog", "USERNAME"))
        self.password_label.setText(_translate("Dialog", "PASSWORD"))
        self.login_btn.setText(_translate("Dialog", "LOGIN"))
        self.signup_btn.setText(_translate("Dialog", "SIGNUP"))
        self.label_3.setText(_translate("Dialog", "LOGIN FORM"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

