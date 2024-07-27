class Form:
    def __init__(self, question=new_quest_templ,
                 answer=new_answer_templ, wrong_ans_1='',
                 wrong_ans_2='', wrong_ans_3=''):
        self.question = question
        self.answer = answer
        self.wrong_ans_1 = wrong_ans_1
        self.wrong_ans_2 = wrong_ans_2
        self.wrong_ans_3 = wrong_ans_3