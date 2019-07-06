import sys
from PyQt5 import QtWidgets

class SignUp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        with open('stylesheet.qss') as f:
            stylesheet = f.read()

        self.setFixedSize(240, 480)
        self.setWindowTitle('Sign up')
        self.setStyleSheet(stylesheet)

        self.nameInput = QtWidgets.QLineEdit(self)
        self.nameInput.setObjectName('nameInput')
        self.nameInput.move(45, 120)

        self.nameError = QtWidgets.QLabel('', self)
        self.nameError.setObjectName('labelError')
        self.nameError.move(45, 160)

        self.usernameInput = QtWidgets.QLineEdit(self)
        self.usernameInput.setObjectName('usernameInput')
        self.usernameInput.move(45, 200)

        self.usernameError = QtWidgets.QLabel('', self)
        self.usernameError.setObjectName('labelError')
        self.usernameError.move(45, 240)


        self.passwordInput = QtWidgets.QLineEdit(self)
        self.passwordInput.setObjectName('passwordInput')
        self.passwordInput.move(45, 280)

        self.passwordError = QtWidgets.QLabel('', self)
        self.passwordError.setObjectName('labelError')
        self.passwordError.move(45, 320)


        self.loginBtn = QtWidgets.QPushButton('Login', self)
        #self.loginBtn.clicked.connect(self.save_user)
        self.loginBtn.setObjectName('loginBtn')
        self.loginBtn.move(35, 380)
        

        self.show()

    def save_user(self):
        pass


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    window = SignUp()

    sys.exit(app.exec_())
