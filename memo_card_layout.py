from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
  QPushButton, QRadioButton, QHBoxLayout, QVBoxLayout, QLabel, QGroupBox, QSpinBox, QButtonGroup
)

menu_btn = QPushButton("Меню")
rest_btn = QPushButton("Відпочити")
ans_btn = QPushButton("Відповісти")

q_label = QLabel('Запитання')

time_label = QLabel('Хвилин')

radio_btn1 = QRadioButton("1")
radio_btn2 = QRadioButton("2")
radio_btn3 = QRadioButton("3")
radio_btn4 = QRadioButton("4")

timer_box = QSpinBox()
timer_box.setValue(30)

radio_g_box = QGroupBox('Варіанти:')
radio_g = QButtonGroup()

radio_g.addButton(radio_btn1)
radio_g.addButton(radio_btn2)
radio_g.addButton(radio_btn3)
radio_g.addButton(radio_btn4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(radio_btn1)
layout_ans2.addWidget(radio_btn2)

layout_ans3.addWidget(radio_btn3)
layout_ans3.addWidget(radio_btn4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

radio_g_box.setLayout(layout_ans1)

result_layout = QVBoxLayout()
result_lbl = QLabel('')
correct_lbl = QLabel('')
ans_group_box = QGroupBox()

result_layout.addWidget(result_lbl, alignment=(Qt.AlignTop | Qt.AlignLeft))
result_layout.addWidget(result_lbl, alignment=Qt.AlignCenter, stretch=2)

ans_group_box.setLayout(result_layout)
ans_group_box.hide()

main_layout_h = QHBoxLayout()
main_layout_h.addWidget(menu_btn, alignment=Qt.AlignLeft)
main_layout_h.addWidget(rest_btn, alignment=Qt.AlignRight)
main_layout_h.addWidget(timer_box, alignment=Qt.AlignRight)
main_layout_h.addWidget(time_label, alignment=Qt.AlignRight)

main_layout2_h = QHBoxLayout()
main_layout2_h.addWidget(q_label, stretch=2)

main_layout3_h = QHBoxLayout()
main_layout3_h.addWidget(radio_g_box)

main_layout4_h = QHBoxLayout()
main_layout4_h.addWidget(ans_btn)

main_layout = QVBoxLayout()
main_layout.addLayout(main_layout_h)
main_layout.addLayout(main_layout2_h)
main_layout.addLayout(main_layout3_h)
main_layout.addLayout(main_layout4_h)