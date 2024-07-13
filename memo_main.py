from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget

app = QApplication([])

from memo_card_layout import *

window = QWidget()
window.setGeometry(0, 0, 600, 500)
window.setWindowTitle('Memo card')
window.show()

window.setLayout(main_layout)

app.exec_()