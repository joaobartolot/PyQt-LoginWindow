import sys
from PyQt5 import QtWidgets

class Login(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        
        with open('stylesheet.qss') as f:
            stylesheet = f.read()

        self.setFixedSize(240, 480)
        self.setStyleSheet(stylesheet)


        self.usernameInput = QtWidgets.QLineEdit(self)
        self.usernameInput.setObjectName('usernameInput')
        self.usernameInput.move(45, 150)

        self.usernameError = QtWidgets.QLabel('', self)
        self.usernameError.setObjectName('labelError')
        self.usernameError.move(45, 190)


        self.passwordInput = QtWidgets.QLineEdit(self)
        self.passwordInput.setObjectName('passwordInput')
        self.passwordInput.move(45, 230)

        self.passwordError = QtWidgets.QLabel('', self)
        self.passwordError.setObjectName('labelError')
        self.passwordError.move(45, 270)


        self.loginBtn = QtWidgets.QPushButton('Login', self)
        self.loginBtn.clicked.connect(self.verify_password)
        self.loginBtn.setObjectName('loginBtn')
        self.loginBtn.move(35, 320)
        

        self.show()


    def verify_password(self):
        pass


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    window = Login()

    sys.exit(app.exec_())
