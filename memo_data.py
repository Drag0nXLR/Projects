from PyQt5.QtCore import QAbstractListModel, QModelIndex, Qt 
from random import randint, shuffle 
 
new_quest_templ = 'Нове питання' # такий рядок буде встановлюватися за замовчуванням для нових питань 
new_answer_templ = 'Нова відповідь' # те ж для відповідей 
 
text_wrong = 'Неправильно' 
text_correct = 'Правильно' 
 
class Form(): 
    ''' зберігає інформацію про одне питання''' 
    def __init__(self, question=new_quest_templ, answer=new_answer_templ,  
                       wrong_answer1='', wrong_answer2='', wrong_answer3=''): 
        self.question = question # питання 
        self.answer = answer # правильна відповідь 
        self.wrong_answer1 = wrong_answer1 # вважаємо, що завжди пишуться три неправильні варіанти 
        self.wrong_answer2 = wrong_answer2 #  
        self.wrong_answer3 = wrong_answer3 # 
        self.is_active = True # продовжувати чи задавати це питання? 
        self.attempts = 0 # скільки разів це питання задавалося 
        self.correct = 0 # кількість правильних відповідей 
    def got_right(self): 
        ''' змінює статистику, отримавши правильну відповідь''' 
        self.attempts += 1 
        self.correct += 1 
    def got_wrong(self): 
        ''' змінює статистику, отримавши неправильну відповідь''' 
        self.attempts += 1 
 
class FormView(): 
    ''' зіставляє дані та віджети для відображення питання''' 
    def __init__(self, frm_model, question, answer, wrong_answer1, wrong_answer2, wrong_answer3): 
        # конструктор отримує та запам'ятовує об'єкт з даними і віджети, відповідні полям анкети 
        self.frm_model = frm_model  # може отримати і None - нічого страшного не станеться,  
                                    # але для методу show потрібно буде попередньо оновити дані методом change 
        self.question = question 
        self.answer = answer 
        self.wrong_answer1 = wrong_answer1 
        self.wrong_answer2 = wrong_answer2 
        self.wrong_answer3 = wrong_answer3   
    def change(self, frm_model): 
        ''' оновлення даних, вже пов'язаних з інтерфейсом ''' 
        self.frm_model = frm_model 
    def show(self): 
        ''' виводить на екран усі дані з об'єкта ''' 
        self.question.setText(self.frm_model.question) 
        self.answer.setText(self.frm_model.answer) 
        self.wrong_answer1.setText(self.frm_model.wrong_answer1) 
        self.wrong_answer2.setText(self.frm_model.wrong_answer2) 
        self.wrong_answer3.setText(self.frm_model.wrong_answer3)

class FormEdit(FormView): 
    ''' використовується, якщо потрібно редагувати форму: встановлює обробники подій, які зберігають текст''' 
    def save_question(self): 
        ''' зберігає текст питання ''' 
        self.frm_model.question = self.question.text() # копіюємо дані з віджета в об'єкт 
    def save_answer(self): 
        ''' зберігає текст правильної відповіді ''' 
        self.frm_model.answer = self.answer.text() # копіюємо дані з віджета в об'єкт 
    def save_wrong(self): 
        ''' зберігає всі неправильні відповіді  
        (якщо в наступній версії програми число неправильних відповідей стане змінним  
        і вони будуть вводитися в списку, можна буде змінити цей метод) ''' 
        self.frm_model.wrong_answer1 = self.wrong_answer1.text() 
        self.frm_model.wrong_answer2 = self.wrong_answer2.text() 
        self.frm_model.wrong_answer3 = self.wrong_answer3.text() 
    def set_connects(self): 
        ''' встановлює обробки подій у віджетах так, щоб зберігати дані ''' 
        self.question.editingFinished.connect(self.save_question) 
        self.answer.editingFinished.connect(self.save_answer) 
        self.wrong_answer1.editingFinished.connect(self.save_wrong)  
        self.wrong_answer2.editingFinished.connect(self.save_wrong) 
        self.wrong_answer3.editingFinished.connect(self.save_wrong) 
    def __init__(self, frm_model, question, answer, wrong_answer1, wrong_answer2, wrong_answer3): 
        # перевизначимо конструктор, щоб не викликати вручну set_connects (діти можуть викликати вручну) 
        super().__init__(frm_model, question, answer, wrong_answer1, wrong_answer2, wrong_answer3) 
        self.set_connects() 
 
class AnswerCheck(FormView): 
    ''' Вважаючи, що питання анкети візуалізуються чек-боксами, перевіряє, чи обрано правильну відповідь.''' 
    def __init__(self, frm_model, question, answer, wrong_answer1, wrong_answer2, wrong_answer3, showed_answer, result): 
        ''' запам'ятовує всі властивості. showed_answer - це віджет, в якому записується правильна відповідь (показується пізніше) 
        result - це віджет, в який буде записаний txt_right або txt_wrong''' 
        super().__init__(frm_model, question, answer, wrong_answer1, wrong_answer2, wrong_answer3) 
        self.showed_answer = showed_answer 
        self.result = result 
    def check(self): 
        ''' відповідь заноситься в статистику, але перемикання у формі не відбувається:  
        цей клас нічого не знає про панелі на формі ''' 
        if self.answer.isChecked(): 
            # відповідь правильна, запишемо і відобразимо в статистиці 
            self.result.setText(text_correct) # напис "правильно" або "неправильно" 
            self.showed_answer.setText(self.frm_model.answer) # пишемо сам текст відповіді у відповідному віджеті 
            self.frm_model.got_right() # оновити статистику, додавши одну правильну відповідь 
        else: 
            # відповідь неправильна, запишемо і відобразимо в статистиці 
            self.result.setText(text_wrong) # напис "правильно" або "неправильно" 
            self.showed_answer.setText(self.frm_model.answer) # пишемо сам текст відповіді у відповідному віджеті 
            self.frm_model.got_wrong() # оновити статистику, додавши неправильну відповідь
class QuestionListModel(QAbstractListModel): 
    ''' у даних знаходиться список об'єктів типу Question,  
    а також список активних питань, щоб показувати його на екрані ''' 
    def __init__(self, parent=None): 
        super().__init__(parent) 
        self.form_list = [] 
    def rowCount(self, index): 
        ''' кількість елементів для показу: обов'язковий метод для моделі, з якою буде пов'язаний віджет "список" ''' 
        return len(self.form_list) 
    def data(self, index, role): 
        ''' обов'язковий метод для моделі: які дані вона надає за запитом від інтерфейсу ''' 
        if role == Qt.DisplayRole: 
            # інтерфейс хоче намалювати цей рядок, дамо йому текст питання для відображення 
            form = self.form_list[index.row()] 
            return form.question 
    def insertRows(self, parent=QModelIndex()): 
        ''' цей метод викликається, щоб вставити до списку об'єктів нові дані; 
        генерується і вставляється одне пусте питання. ''' 
        position = len(self.form_list) # ми вставляємо в кінець, це потрібно повідомити наступним рядком: 
        self.beginInsertRows(parent, position, position) # вставка даних повинна бути після цього вказівки і перед endInsertRows() 
        self.form_list.append(Form()) # додали нове питання до списку даних 
        self.endInsertRows() # закінчили вставку (тепер можна продовжувати працювати з моделлю) 
        QModelIndex() 
        return True # повідомляємо, що все пройшло добре 
    def removeRows(self, position, parent=QModelIndex()): 
        ''' стандартний метод для видалення рядків - після видалення з моделі рядок автоматично видаляється з екрана ''' 
        self.beginRemoveRows(parent, position, position) # повідомляємо, що ми збираємося видаляти рядок - від position до position  
            # (взагалі кажучи, стандарт методу removeRows пропонує прибирати кілька рядків, але ми напишемо одну) 
        self.form_list.pop(position) # видаляємо зі списку елемент з номером position 
            # у правильній реалізації програми видаляти питання зі статистикою не можна, можна їх деактивувати,  
            # але це помітно ускладнює модель (потрібно підтримувати список усіх питань для статистики  
            # і список активних для відображення у списку редагування) 
        self.endRemoveRows() # закінчили видалення (далі бібліотека сама оновлює список на екрані) 
        return True # все гаразд  
            # (по-хорошому нам може прийти неіснуючий position, 
            # правильніше було б писати try except і повертати True тільки в дійсно спрацювавшому випадку) 
    def random_question(self): 
        ''' Видає випадкове питання ''' 
        # тут варто перевіряти, що питання активне... 
        total = len(self.form_list) 
        current = randint(0, total - 1) 
        return self.form_list[current] 
 
def random_AnswerCheck(list_model, w_question, widgets_list, w_showed_answer, w_result): 
    '''повертає новий екземпляр класу AnswerCheck,  
    з випадковим питанням та випадковим розподілом відповідей по віджетам''' 
    frm = list_model.random_question() 
    shuffle(widgets_list) 
    frm_card = AnswerCheck(frm, w_question, widgets_list[0], widgets_list[1], widgets_list[2], widgets_list[3], w_showed_answer, w_result) 
    return frm_card