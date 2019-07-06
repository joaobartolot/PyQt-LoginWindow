import sys
from data import LoadData
from PyQt5 import QtWidgets

class Login(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        
        with open('stylesheet.qss') as f:
            stylesheet = f.read()

        self.setFixedSize(240, 480)
        self.setWindowTitle('Login')
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
        self.loginBtn.clicked.connect(self.verify_account)
        self.loginBtn.setObjectName('loginBtn')
        self.loginBtn.move(35, 320)
        

        self.show()


    def verify_account(self):
        self.usernameError.setText('')
        self.passwordError.setText('')

        data = LoadData()

        if self.usernameInput.text() != '' and self.passwordInput != '':
            if self.usernameInput.text() == '':
                self.usernameError.setText('Please enter a username')
                self.usernameError.adjustSize()

            if self.passwordInput.text() == '':
                self.passwordError.setText('Please enter a password')
                self.passwordError.adjustSize()


            if self.usernameInput.text() not in data.username_list:
                self.usernameError.setText('Please check your username')
                self.usernameError.adjustSize()

            else:
                if self.passwordInput.text() not in data.password_list:
                    self.passwordError.setText('You got the wrong password')
                    self.passwordError.adjustSize()


        else:
            self.usernameError.setText('Please enter a username')
            self.usernameError.adjustSize()

            self.passwordError.setText('Please enter a password')
            self.passwordError.adjustSize()



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    window = Login()

    sys.exit(app.exec_())
