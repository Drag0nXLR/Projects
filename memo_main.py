
from PyQt5.QtCore import QTimer 
from PyQt5.QtWidgets import QWidget 
 
from memo_app import app 
from memo_data import * 
from memo_main_layout import * 
from memo_card_layout import * 
from memo_edit_layout import question_text, correct_answer_text, wrong_answer1_text, wrong_answer2_text, wrong_answer3_text 
 
######################################              Константи:              ############################################# 
main_width, main_height = 1000, 450 # початкові розміри головного вікна 
card_width, card_height = 600, 500 # початкові розміри вікна "картка" 
time_unit = 1000    # стільки триває одна одиниця часу з тих, на які потрібно заснути  
                    # (у робочій версії програми збільшити в 60 разів!) 
 
######################################          Глобальні змінні:          ############################################# 
questions_listmodel = QuestionListModel() # список питань 
edit_form = FormEdit(0, question_text, correct_answer_text, wrong_answer1_text, wrong_answer2_text, wrong_answer3_text) # запам'ятовуємо, що у формі редагування питання з чим пов'язане 
radio_list = [radio1, radio2, radio3, radio4] # список віджетів, який потрібно перемішувати (для випадкового розміщення відповідей) 
card_form = 0 # тут буде пов'язано питання з формою тесту 
timer = QTimer() # таймер для можливості "заснути" на час і прокинутись 
card_window = QWidget() # вікно картки 
main_window = QWidget() # вікно редагування питань, основне у програмі 
 
######################################             Тестові дані:            ############################################# 
def testlist(): 
     
    form = Form('Яблуко', 'apple', 'application', 'pineapple', 'apply') 
    questions_listmodel.form_list.append(form) 
    form = Form('Будинок', 'house', 'horse', 'hurry', 'hour') 
    questions_listmodel.form_list.append(form) 
    form = Form('Миша', 'mouse', 'mouth', 'muse', 'museum') 
    questions_listmodel.form_list.append(form) 
    form = Form('Число', 'number', 'digit', 'amount', 'summary') 
    questions_listmodel.form_list.append(form) 
 
######################################     Функції для проведення тесту:    ############################################# 
 
def set_card(): 
    ''' задає, як виглядає вікно картки''' 
    card_window.resize(card_width, card_height) 
    card_window.move(300, 300) 
    card_window.setWindowTitle('Memory Card') 
    card_window.setLayout(layout_card) 
 
def sleep_card(): 
    ''' картка ховається на час, вказаний у таймері''' 
    card_window.hide() 
    timer.setInterval(time_unit * minutes_box.value() ) 
    timer.start() 
 
def show_card(): 
    ''' показує вікно (за таймером), таймер зупиняється''' 
    card_window.show() 
    timer.stop() 
 
def show_random(): 
    ''' показати випадкове питання ''' 
    global card_form # як би властивість вікна - поточна форма з даними картки 
    # отримуємо випадкові дані, і випадково ж розподіляємо варіанти відповідей по радіокнопках: 
    card_form = random_AnswerCheck(questions_listmodel, question_lbl, radio_list, correct_lbl, result_lbl) 
    # ми будемо запускати функцію, коли вікно вже є. Тому показуємо: 
    card_form.show() # завантажити потрібні дані у відповідні віджети  
    show_question() # показати на формі панель питань 
 
def click_OK(): 
    ''' перевіряє питання або завантажує нове питання ''' 
    if ok_btn.text() != 'Наступне питання': 
        card_form.check() 
        show_result() 
    else: 
        # напис на кнопці рівний 'Наступне', от і створюємо наступне випадкове питання: 
        show_random()
 
def back_to_menu(): 
    ''' повернення з тесту у вікно редактора ''' 
    card_window.hide() 
    main_window.showNormal() 
 
######################################     Функції для редагування питань:    ###################################### 
def set_main(): 
    ''' задає, як виглядає головне вікно''' 
    main_window.resize(main_width, main_height) 
    main_window.move(100, 100) 
    main_window.setWindowTitle('Список питань') 
    main_window.setLayout(main_layout) 
 
def edit_question(index): 
    ''' завантажує у форму редагування питання та відповіді, відповідні переданому рядку ''' 
    #  index - це об'єкт класу QModelIndex, див. потрібні методи нижче  
    if index.isValid(): 
        i = index.row() 
        frm = questions_listmodel.form_list[i] 
        edit_form.change(frm) 
        edit_form.show() 
 
def add_form(): 
    ''' додає нове питання і пропонує його змінити ''' 
    questions_listmodel.insertRows() # Нове питання з'явилося у даних і автоматично у списку на екрані 
    last = questions_listmodel.rowCount(0) - 1   # Нове питання - останнє у списку. Знайдемо його позицію.  
                                                # В rowCount передаємо 0, щоб відповідати вимогам функції: 
                                                # цей параметр все одно не використовується, але  
                                                # потрібний за стандартом бібліотеки (метод з параметром index викликається під час відтворення списку)     
    index = questions_listmodel.index(last) # отримуємо об'єкт класу QModelIndex, який відповідає останньому елементу у даних  
    questions_list.setCurrentIndex(index) # робимо відповідний рядок списку на екрані поточним 
    edit_question(index)    # це питання треба завантажити у форму редагування 
                            # кліка мишею у нас тут немає, викличемо потрібну функцію з програми 
    question_text.setFocus(Qt.TabFocusReason) # переводимо фокус на поле редагування питання, щоб одразу прибиралися "заготовки" 
                                             # Qt.TabFocusReason переводить фокус так, ніби була натиснута клавіша "tab"  
                                             # це зручно тим, що виділяє "заготовку", її легко одразу прибрати  
 
def del_form(): 
    ''' видаляє питання та переключає фокус ''' 
    questions_listmodel.removeRows(questions_list.currentIndex().row()) 
    edit_question(questions_list.currentIndex()) 
 
def start_test(): 
    ''' при початку тесту форма пов'язується з випадковим питанням і показується ''' 
    show_random() 
    card_window.show() 
    main_window.showMinimized() 
 
######################################      Установка потрібних з'єднань:    ############################################# 
def connects(): 
    questions_list.setModel(questions_listmodel) # зв'язати список на екрані зі списком питань 
    questions_list.clicked.connect(edit_question) # при натисканні на елемент списку буде відкриватися для редагування потрібне питання 
    add_btn.clicked.connect(add_form) # з'єднали натискання кнопки "нове питання" з функцією додавання 
    delete_btn.clicked.connect(del_form) # з'єднали натискання кнопки "видалити питання" з функцією видалення 
    start_btn.clicked.connect(start_test) # натискання кнопки "почати тест"  
    ok_btn.clicked.connect(click_OK) # натискання кнопки "OK" на формі тесту 
    menu_btn.clicked.connect(back_to_menu) # натискання кнопки "Меню" для повернення з форми тесту у редактор питань 
    timer.timeout.connect(show_card) # показуємо форму тесту після закінчення таймера 
    sleep_btn.clicked.connect(sleep_card) # натискання кнопки "спати" у картці-тесті 
 
######################################            Запуск програми:         ############################################# 
# Основний алгоритм іноді оформляють у функцію, яка запускається, тільки якщо код виконується з цього файлу, 
# а не при підключенні як модуль. Дітям це зовсім не потрібно. 
testlist() 
set_card() 
set_main() 
connects() 
main_window.show() 
app.exec_()