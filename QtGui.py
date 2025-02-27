# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoginForm(object):
    def setupUi(self, LoginForm):
        LoginForm.setObjectName("LoginForm")
        LoginForm.resize(400, 296)
        LoginForm.setStyleSheet("background-image: url(:/images/background.jpg) 0 0 0 0 stretch stretch;\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"")
        self.verticalLayout = QtWidgets.QVBoxLayout(LoginForm)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelTitle = QtWidgets.QLabel(LoginForm)
        self.labelTitle.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.labelTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTitle.setObjectName("labelTitle")
        self.verticalLayout.addWidget(self.labelTitle)
        self.lineEditUsername = QtWidgets.QLineEdit(LoginForm)
        self.lineEditUsername.setObjectName("lineEditUsername")
        self.verticalLayout.addWidget(self.lineEditUsername)
        self.lineEditPassword = QtWidgets.QLineEdit(LoginForm)
        self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.verticalLayout.addWidget(self.lineEditPassword)
        self.buttonLogin = QtWidgets.QPushButton(LoginForm)
        self.buttonLogin.setObjectName("buttonLogin")
        self.verticalLayout.addWidget(self.buttonLogin)
        self.buttonCancel = QtWidgets.QPushButton(LoginForm)
        self.buttonCancel.setObjectName("buttonCancel")
        self.verticalLayout.addWidget(self.buttonCancel)
        self.label = QtWidgets.QLabel(LoginForm)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setOpenExternalLinks(False)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        self.retranslateUi(LoginForm)
        QtCore.QMetaObject.connectSlotsByName(LoginForm)

    def retranslateUi(self, LoginForm):
        _translate = QtCore.QCoreApplication.translate
        LoginForm.setWindowTitle(_translate("LoginForm", "Login"))
        self.labelTitle.setText(_translate("LoginForm", "Log in to use all the functions"))
        self.lineEditUsername.setPlaceholderText(_translate("LoginForm", "Username"))
        self.lineEditPassword.setPlaceholderText(_translate("LoginForm", "Password"))
        self.buttonLogin.setText(_translate("LoginForm", "Login"))
        self.buttonCancel.setText(_translate("LoginForm", "Cancel"))
        self.label.setText(_translate("LoginForm", "Tool created by :PhCtrlZ-©️ 2025 "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginForm = QtWidgets.QWidget()
    ui = Ui_LoginForm()
    ui.setupUi(LoginForm)
    LoginForm.show()
    sys.exit(app.exec_())
