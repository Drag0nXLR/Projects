from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
	QPushButton, QRadioButton, QVBoxLayout, QHBoxLayout, QLabel, 
	QGroupBox, QButtonGroup, QSpinBox
)
from random import randint

questions = [
	"Яблуко",
	"Машина",
	"Дерево"
]

variants = [
	["apple", "window", "pencil", "door"],
	["apple", "car", "pencil", "door"],
	["car", "window", "apple", "tree"]
]

correct_answers = [
	0,
	1,
	3
]

menu_btn = QPushButton("Меню")
rest_button = QPushButton("Відпочити")
answer_btn = QPushButton("Відповісти")

current_question = randint(0, len(questions) - 1)
question_lbl = QLabel(questions[current_question])
time_lbl = QLabel("хвилин")

radio1 = QRadioButton(variants[current_question][0])
radio2 = QRadioButton(variants[current_question][1])
radio3 = QRadioButton(variants[current_question][2])
radio4 = QRadioButton(variants[current_question][3])

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
	correct_answer = correct_answers[current_question]
	result = "Ви програли"
	if correct_answer == 0 and radio1.isChecked():
		result = "Ви виграли"
	elif correct_answer == 1 and radio2.isChecked():
		result = "Ви виграли"
	elif correct_answer == 2 and radio3.isChecked():
		result = "Ви виграли"
	elif correct_answer == 3 and radio4.isChecked():
		result = "Ви виграли"
			
	result_lbl.setText(result)
	correct_lbl.setText(variants[current_question][correct_answers[current_question]])
	ans_group_box.show()
	radio_group_box.hide()
	answer_btn.setText("Наступне питання")

def show_question():
	global current_question
	radio_group.setExclusive(False)
	radio1.setChecked(False)
	radio2.setChecked(False)
	radio3.setChecked(False)
	radio4.setChecked(False)
	next_current_question = randint(0, len(questions) - 1)
	while next_current_question == current_question:
		next_current_question = randint(1, len(questions))
	current_question = next_current_question
	question_lbl.setText(questions[current_question])
	radio1.setText(variants[current_question][0])
	radio2.setText(variants[current_question][1])
	radio3.setText(variants[current_question][2])
	radio4.setText(variants[current_question][3])
	ans_group_box.hide()
	radio_group_box.show()
	answer_btn.setText("Відповісти")

def switch_screen():
	print(answer_btn.text)
	if answer_btn.text() == "Відповісти":
		show_result()
	elif answer_btn.text() == "Наступне питання":
		show_question()

answer_btn.clicked.connect(switch_screen)