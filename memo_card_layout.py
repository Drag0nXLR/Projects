from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QPushButton, QRadioButton, QVBoxLayout, QHBoxLayout, QLabel, 
    QGroupBox, QButtonGroup, QSpinBox
)

menu_btn = QPushButton("Меню")
rest_button = QPushButton("Відпочити")
answer_btn = QPushButton("Відповісти")

question_lbl = QLabel("Запитання")
time_lbl = QLabel("хвилин")

radio1 = QRadioButton("1")
radio2 = QRadioButton("2")
radio3 = QRadioButton("3")
radio4 = QRadioButton("4")

timer_box = QSpinBox()
timer_box.setValue(30)

radio_group_box = QGroupBox("Варіанти відповідей")
radio_group = QButtonGroup()
radio_group.addButton(radio1)
radio_group.addButton(radio2)
radio_group.addButton(radio3)
radio_group.addButton(radio4)

layout_ans_H = QHBoxLayout()
layout_ans_V1 = QVBoxLayout()
layout_ans_V2 = QVBoxLayout()

layout_ans_V1.addWidget(radio1)
layout_ans_V1.addWidget(radio2)
layout_ans_V2.addWidget(radio3)
layout_ans_V2.addWidget(radio4)
layout_ans_H.addLayout(layout_ans_V1)
layout_ans_H.addLayout(layout_ans_V2)

radio_group_box.setLayout(layout_ans_H)

layout_res = QVBoxLayout()
result_lbl = QLabel("")
correct_lbl = QLabel("")
ans_group_box = QGroupBox()

layout_res.addWidget(result_lbl, alignment=(Qt.AlignTop | Qt.AlignLeft))
layout_res.addWidget(correct_lbl, alignment=Qt.AlignCenter, stretch = 2)
ans_group_box.setLayout(layout_res)
ans_group_box.hide()

main_layout_H1 = QHBoxLayout()
main_layout_H1.addWidget(menu_btn, alignment=Qt.AlignLeft)
main_layout_H1.addWidget(rest_button, alignment=Qt.AlignRight)
main_layout_H1.addWidget(timer_box, alignment=Qt.AlignRight)
main_layout_H1.addWidget(time_lbl, alignment=Qt.AlignRight)

main_layout_H2 = QHBoxLayout()
main_layout_H2.addWidget(question_lbl, stretch=2)

main_layout_H3 = QHBoxLayout()
main_layout_H3.addWidget(radio_group_box)
main_layout_H3.addWidget(ans_group_box)

main_layout_H4 = QHBoxLayout()
main_layout_H4.addWidget(answer_btn)

main_vertical_layout = QVBoxLayout()
#1
main_vertical_layout.addLayout(main_layout_H1)
main_vertical_layout.addLayout(main_layout_H2)
main_vertical_layout.addLayout(main_layout_H3)
main_vertical_layout.addLayout(main_layout_H4)

# У ФАЙЛІ memo_card_layout.py:
# 1. Опиши дві функції show_result () і show_question (). При натисканні на кнопку "Ок" буде викликатися show_result (), що відображає правильну відповідь, а при натисканні на кнопку ще раз - викликатися show_question (), що показує наступне питання.
# 2. Не забудь змінити напис на кнопці. При відповіді на питання і перехід до результатів напис на кнопці повинна змінюватися з "Ок" на "Наступне питання".

def show_result():
  radio_group_box.hide()
  ans_group_box.show()
  answer_btn.setText('Наступне питання')

def show_question():
  radio_group_box.show()
  ans_group_box.hide()
  answer_btn.setText('Відповісти')

def switch_screen():
  if answer_btn.text() == 'Відповісти':
    show_result()
  elif answer_btn.text() == 'Наступне питання':
    show_question()

answer_btn.clicked.connect(switch_screen)