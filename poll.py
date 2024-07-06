from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)

win = QtWidgets.QWidget()
win.setWindowTitle("Crazy People Poll")

text = QtWidgets.QLabel("В якому році цей канал отримав Золоту кнопку?")

btn1 = QtWidgets.QRadioButton("2005")
btn2 = QtWidgets.QRadioButton("2010")
btn3 = QtWidgets.QRadioButton("2015")
btn4 = QtWidgets.QRadioButton("2020")

v_layout = QtWidgets.QVBoxLayout()
h_layout = QtWidgets.QHBoxLayout()

h_layout_1 = QtWidgets.QHBoxLayout()
h_layout_2 = QtWidgets.QHBoxLayout()

v_layout.addWidget(text, alignment=Qt.AlignCenter)
v_layout.addWidget(btn1, alignment=Qt.AlignCenter)
v_layout.addWidget(btn2, alignment=Qt.AlignCenter)
v_layout.addWidget(btn3, alignment=Qt.AlignCenter)
v_layout.addWidget(btn4, alignment=Qt.AlignCenter)

win.setLayout(v_layout)
win.show()

def show_msg_win():
    msg = QtWidgets.QMessageBox()
    msg.setWindowTitle('You won!')
    msg.setWindowIcon(QtWidgets.QMessageBox.Information)
    msg.setStandardButtons(QtWidgets.QMessageBox.Ok)

    msg.exec_()

sys.exit(app.exec_())