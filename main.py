import sys
from PyQt5 import QtWidgets
from QtGui import Ui_LoginForm
from QtGui1 import Ui_MainWindow
import subprocess,json,time
import requests
import os
import resources_rc

if hasattr(sys,"_MEIPASS"):
    resource_path=os.path.join(sys._MEIPASS,"images/background.jpg")
else:
    resource_path="images/background.jpg"
class LoginApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui=Ui_LoginForm()
        self.ui.setupUi(self)
        QtWidgets.QMessageBox.warning(self,"Notice","Username always is admin!")

        self.ui.buttonCancel.clicked.connect(self.close)
        self.ui.buttonLogin.clicked.connect(self.handle_login)
    def handle_login(self):
        username=self.ui.lineEditUsername.text()
        password=self.ui.lineEditPassword.text()
        b="sever"
        r=requests.get('https://api.npoint.io/06eefb951e08ad628e9a')
        r=json.loads(r.text)
        password=r[b]
        if username=="admin" and password==True:
            self.open_main_window()
        else:
            QtWidgets.QMessageBox.waring(self,"Login Failed","Invalid Password")
    def open_main_window(self):
        self.main_window=MainWindow()
        self.main_window.show()
        self.close()
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
    
if __name__=='__main__':
    app=QtWidgets.QApplication(sys.argv)

    login_window=LoginApp()
    login_window.show()

    sys.exit(app.exec_())
