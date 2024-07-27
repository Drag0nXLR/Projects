from PyQt5.QtCore import Qt, QRect
from PyQt5.QtWidgets import QApplication, QWidget
from random import shuffle

app = QApplication([])
from memo_card_layout import *

window = QWidget()
window.setGeometry(QRect(0, 0, 600, 500))
window.setWindowTitle("Memory Card")

window.setLayout(main_vertical_layout)

start_question = 'Яблуко'
start_variants = [
    'apple', 'application', 'building', 'jiro'
]
answer = 'apple'

q_variants = shuffle(start_variants)

question_lbl.setText(start_question)

radio1.setText(start_variants[0])
radio2.setText(start_variants[1])
radio3.setText(start_variants[2])
radio4.setText(start_variants[3])

def check_result(answer, variants, result):
    print('check result')

window.show()
app.exec_()