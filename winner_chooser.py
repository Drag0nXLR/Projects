from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

from random import randint

import sys
print(sys.version)

class App(QMainWindow):
    def __init__(self):
        super(App, self).__init__()

        self.setWindowTitle('Winner Chooser')
        self.setGeometry(300, 250, 350, 200)

        self.text = QtWidgets.QLabel(self)
        self.text.setText('Winner')
        self.text.move(160, 70)
        self.text.adjustSize()

        self.winner_num = QtWidgets.QLabel(self)
        self.winner_num.setText('?')
        self.winner_num.move(173, 100)
        self.winner_num.adjustSize()

        self.btn = QtWidgets.QPushButton(self)
        self.btn.move(75, 150)
        self.btn.setText('Generate')
        self.btn.setFixedWidth(200)
        self.btn.clicked.connect(self.choose_winner)

    def choose_winner(self):
        winner = randint(1, 100)
        self.winner_num.setText(str(winner))
        self.winner_num.adjustSize()

def application():
    app = QApplication(sys.argv)
    window = App()

    window.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    application()
