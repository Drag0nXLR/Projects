# memo_main_layout.py
''' Головне вікно: зліва список питань, справа - поточне питання, яке можна редагувати ''' 
from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import ( 
        QApplication, QWidget,  
        QTableWidget, QListView, QListWidgetItem, 
        QLineEdit, QFormLayout, 
        QHBoxLayout, QVBoxLayout,  
        QGroupBox, QButtonGroup, QRadioButton,   
        QPushButton, QLabel, QSpinBox) 
from memo_app import app  
from memo_edit_layout import form_layout   
from memo_card_layout import layout_card 
 
questions_list = QListView() 
edit_widget = QWidget() 
edit_widget.setLayout(form_layout) 
add_btn = QPushButton('Нове питання') 
delete_btn = QPushButton('Видалити питання') 
start_btn = QPushButton('Почати тренування') 
 
main_col1 = QVBoxLayout() 
main_col1.addWidget(questions_list) 
main_col1.addWidget(add_btn) 
 
main_col2 = QVBoxLayout() 
main_col2.addWidget(edit_widget) 
main_col2.addWidget(delete_btn) 
 
main_line1 = QHBoxLayout() 
main_line1.addLayout(main_col1) 
main_line1.addLayout(main_col2) 
 
main_line2 = QHBoxLayout() 
main_line2.addStretch(1) 
main_line2.addWidget(start_btn, stretch=2) 
main_line2.addStretch(1) 
 
main_layout = QVBoxLayout() 
main_layout.addLayout(main_line1) 
main_layout.addLayout(main_line2)