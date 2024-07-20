from PyQt5.QtCore import Qt, QRect
from PyQt5.QtWidgets import QApplication, QWidget

app = QApplication([])
from memo_card_layout import *

window = QWidget()
window.setGeometry(QRect(0, 0, 600, 500))
window.setWindowTitle("Memory Card")

window.setLayout(main_vertical_layout)

window.show()
app.exec_()