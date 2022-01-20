# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signup.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_Dialog1(object):
    def insertData(self):
        username = self.usr_lineEdit.text()
        email=self.mail_lineEdit.text()
        password= pass_lineEdit.text()

        connection=sqlite3.connect("login.db")
        connection.execute("INSERT INTO USERS VALUES(?,?,?)",(username,email,password))
        connection.commit()
        connection.close()

    def setupUi(self, Dialog1):
        Dialog1.setObjectName("Dialog1")
        Dialog1.resize(748, 451)
        Dialog1.setStyleSheet("QDialog{\n"
"background-color: rgb(251, 255, 171);\n"
"}")
        self.signup = QtWidgets.QLabel(Dialog1)
        self.signup.setGeometry(QtCore.QRect(270, 40, 211, 51))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(20)
        self.signup.setFont(font)
        self.signup.setAlignment(QtCore.Qt.AlignCenter)
        self.signup.setObjectName("signup")
        self.usr_label = QtWidgets.QLabel(Dialog1)
        self.usr_label.setGeometry(QtCore.QRect(200, 150, 111, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.usr_label.setFont(font)
        self.usr_label.setAlignment(QtCore.Qt.AlignCenter)
        self.usr_label.setObjectName("usr_label")
        self.mail_label = QtWidgets.QLabel(Dialog1)
        self.mail_label.setGeometry(QtCore.QRect(190, 200, 101, 21))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.mail_label.setFont(font)
        self.mail_label.setAlignment(QtCore.Qt.AlignCenter)
        self.mail_label.setObjectName("mail_label")
        self.pass_label = QtWidgets.QLabel(Dialog1)
        self.pass_label.setGeometry(QtCore.QRect(190, 230, 111, 61))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pass_label.setFont(font)
        self.pass_label.setAlignment(QtCore.Qt.AlignCenter)
        self.pass_label.setObjectName("pass_label")
        self.usr_lineEdit = QtWidgets.QLineEdit(Dialog1)
        self.usr_lineEdit.setGeometry(QtCore.QRect(340, 160, 113, 20))
        self.usr_lineEdit.setObjectName("usr_lineEdit")
        self.mail_lineEdit = QtWidgets.QLineEdit(Dialog1)
        self.mail_lineEdit.setGeometry(QtCore.QRect(340, 210, 113, 20))
        self.mail_lineEdit.setObjectName("mail_lineEdit")
        self.pass_lineEdit = QtWidgets.QLineEdit(Dialog1)
        self.pass_lineEdit.setGeometry(QtCore.QRect(340, 260, 113, 20))
        self.pass_lineEdit.setObjectName("pass_lineEdit")
        self.signup_btn = QtWidgets.QPushButton(Dialog1)
        self.signup_btn.setGeometry(QtCore.QRect(320, 330, 75, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setBold(True)
        font.setWeight(75)
        self.signup_btn.setFont(font)
        self.signup_btn.setObjectName("signup_btn")
        ###############################Insert Data##################
        self.signup_btn.clicked.connect(self.insertData)
        ############################################################
        self.retranslateUi(Dialog1)
        QtCore.QMetaObject.connectSlotsByName(Dialog1)

    def retranslateUi(self, Dialog1):
        _translate = QtCore.QCoreApplication.translate
        Dialog1.setWindowTitle(_translate("Dialog1", "Dialog"))
        self.signup.setText(_translate("Dialog1", "SIGN UP FORM"))
        self.usr_label.setText(_translate("Dialog1", "User Name"))
        self.mail_label.setText(_translate("Dialog1", "Email Id"))
        self.pass_label.setText(_translate("Dialog1", "Password"))
        self.signup_btn.setText(_translate("Dialog1", "SignUp"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog1 = QtWidgets.QDialog()
    ui = Ui_Dialog1()
    ui.setupUi(Dialog1)
    Dialog1.show()
    sys.exit(app.exec_())

