import sys
from PyQt5 import QtWidgets

class Login(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        
        with open('stylesheet.qss') as f:
            stylesheet = f.read()

        self.setFixedSize(240, 480)
        self.setStyleSheet(stylesheet)


        labelMessage = QtWidgets.QLabel()
        labelMessage.setObjectName('labelMessage')
        labelMessage.move(120, 90)


        usernameInput = QtWidgets.QLineEdit(self)
        usernameInput.setObjectName('usernameInput')
        usernameInput.move(45, 150)

        passwordInput = QtWidgets.QLineEdit(self)
        passwordInput.setObjectName('passwordInput')
        passwordInput.move(45, 230)


        self.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    window = Login()

    sys.exit(app.exec_())
