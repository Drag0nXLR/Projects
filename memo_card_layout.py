''' Вікно для картки питання ''' 
from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import ( 
        QApplication, QWidget,  
        QTableWidget, QListWidget, QListWidgetItem, 
        QLineEdit, QFormLayout, 
        QHBoxLayout, QVBoxLayout,  
        QGroupBox, QButtonGroup, QRadioButton,   
        QPushButton, QLabel, QSpinBox) 
from memo_app import app  
 
# віджети, які треба буде розмістити: 
menu_btn = QPushButton('Меню') # кнопка повернення в основне вікно  
sleep_btn = QPushButton('Відпочити') # кнопка прибирає вікно і повертає його після закінчення таймера 
minutes_box = QSpinBox() # введення кількості хвилин 
minutes_box.setValue(30) 
ok_btn = QPushButton('Відповісти') # кнопка відповіді 
question_lbl = QLabel('') # текст питання 
 
# ---------------------------------------------------------- 
# Створюємо панель з варіантами відповідей: 
# ---------------------------------------------------------- 
 
# Створюємо віджети і об'єднуємо їх у групи 
radio_group_box = QGroupBox("Варіанти відповідей") # група на екрані для перемикачів з відповідями 
radio_group = QButtonGroup() # а це для групування перемикачів, щоб керувати їх поведінкою 
 
radio1 = QRadioButton('') 
radio2 = QRadioButton('') 
radio3 = QRadioButton('') 
radio4 = QRadioButton('') 
 
radio_group.addButton(radio1) 
radio_group.addButton(radio2) 
radio_group.addButton(radio3) 
radio_group.addButton(radio4) 
 
# Розміщуємо на панелі варіанти відповідей у два стовпці всередині групи: 
layout_ans1 = QHBoxLayout()    
layout_ans2 = QVBoxLayout() # вертикальні будуть всередині горизонтального 
layout_ans3 = QVBoxLayout() 
layout_ans2.addWidget(radio1) # дві відповіді в перший стовпець 
layout_ans2.addWidget(radio2) 
layout_ans3.addWidget(radio3) # дві відповіді в другий стовпець 
layout_ans3.addWidget(radio4) 
 
layout_ans1.addLayout(layout_ans2) 
layout_ans1.addLayout(layout_ans3) # розмістили стовпці в одному рядку 
 
radio_group_box.setLayout(layout_ans1) # готова "панель" з варіантами відповідей  
 
# ---------------------------------------------------------- 
# Створюємо панель з результатом тесту: 
# ---------------------------------------------------------- 
 
# Створюємо віджети і об'єднуємо їх у групи 
answer_group_box = QGroupBox("Результат тесту") 
result_lbl = QLabel('') # тут розміщується напис "правильно" або "неправильно" 
correct_lbl = QLabel('') # тут буде написаний текст правильної відповіді 
 
# Розміщуємо результат тесту: 
layout_res = QVBoxLayout() 
layout_res.addWidget(result_lbl, alignment=(Qt.AlignLeft | Qt.AlignTop)) 
layout_res.addWidget(correct_lbl, alignment=Qt.AlignHCenter, stretch=2) 
answer_group_box.setLayout(layout_res) 
answer_group_box.hide()
layout_line1 = QHBoxLayout() # кнопки для перемикання між режимами 
layout_line2 = QHBoxLayout() # питання 
layout_line3 = QHBoxLayout() # варіанти відповідей або результат тесту 
layout_line4 = QHBoxLayout() # кнопка "Відповісти" 
 
layout_line1.addWidget(menu_btn) 
layout_line1.addStretch(1) # розрив між кнопками робимо по можливості довшим 
layout_line1.addWidget(sleep_btn) 
layout_line1.addWidget(minutes_box) 
layout_line1.addWidget(QLabel('хвилин')) # нам не потрібна змінна для цього напису 
 
layout_line2.addWidget(question_lbl, alignment=(Qt.AlignHCenter | Qt.AlignVCenter)) 
layout_line3.addWidget(radio_group_box) 
layout_line3.addWidget(answer_group_box) 
 
layout_line4.addStretch(1) 
layout_line4.addWidget(ok_btn, stretch=2) # кнопка повинна бути великою 
layout_line4.addStretch(1) 
 
# Тепер створені 4 рядки розмістимо один під одним: 
layout_card = QVBoxLayout() 
layout_card.addLayout(layout_line1, stretch=1) 
layout_card.addLayout(layout_line2, stretch=2) 
layout_card.addLayout(layout_line3, stretch=8) 
layout_card.addStretch(1) 
layout_card.addLayout(layout_line4, stretch=1) 
layout_card.addStretch(1) 
layout_card.setSpacing(5) # проміжки між вмістом 
 
# Результат роботи цього модуля: віджети розміщені всередині layout_card, який можна призначити вікну. 
 
def show_result(): 
    ''' показати панель відповідей ''' 
    radio_group_box.hide() 
    answer_group_box.show() 
    ok_btn.setText('Наступне питання') 
 
def show_question(): 
    ''' показати панель питань ''' 
    radio_group_box.show() 
    answer_group_box.hide() 
    ok_btn.setText('Відповісти') 
    # скинути обрану радіо-кнопку 
    radio_group.setExclusive(False) # зняли обмеження, щоб можна було скинути вибір радіокнопки 
    radio1.setChecked(False) 
    radio2.setChecked(False) 
    radio3.setChecked(False) 
    radio4.setChecked(False) 
    radio_group.setExclusive(True) # повернули обмеження, тепер тільки одна радіокнопка може бути обранаS