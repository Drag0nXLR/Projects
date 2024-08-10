# memo_edit_layout.py
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QListView,
    QPushButton,
    QFormLayout,
    QVBoxLayout,
    QHBoxLayout,
    QLineEdit
)

app = QApplication([])

window = QWidget()
window.setGeometry(QRect(0, 0, 600, 500))
window.setWindowTitle("Список питань")

edit_main_layout = QVBoxLayout()

edit_layout_h1 = QHBoxLayout()
list = QListView()
edit_layout_h1.addWidget(list)

layout_form = QFormLayout()
question_text = QLineEdit('')
correct_answer_text = QLineEdit('')
wrong_answer1_text = QLineEdit('')
wrong_answer2_text = QLineEdit('')
wrong_answer3_text = QLineEdit('')

layout_form.addRow("Запитання:", question_text)
layout_form.addRow("Правильна відповідь:", correct_answer_text)
layout_form.addRow("Неправильна відповідь 1:", wrong_answer1_text)
layout_form.addRow("Неправильна відповідь 2:", wrong_answer2_text)
layout_form.addRow("Неправильна відповідь 3:", wrong_answer3_text)

edit_layout_h1.addLayout(layout_form)

edit_main_layout.addLayout(edit_layout_h1)

edit_layout_h2 = QHBoxLayout()
create_btn = QPushButton("Нове запитання")
edit_btn = QPushButton("Редагувати запитання")
edit_layout_h2.addWidget(create_btn)
edit_layout_h2.addWidget(edit_btn)

edit_main_layout.addLayout(edit_layout_h2)

start_btn = QPushButton("Почати тренування")
edit_main_layout.addWidget(start_btn)

window.setLayout(edit_main_layout)
window.show()

app.exec_()