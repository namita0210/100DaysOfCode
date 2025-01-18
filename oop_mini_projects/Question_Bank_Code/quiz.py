from main import question_bank
from data import question_data
from model import Question

class Quiz:

    def __init__(self,q_list):
        self.q_num = 0
        self.q_list = q_list

    def next_question(self):
        current_question = self.q_list[self.q_num]
        self.q_num +=1
        input(f"Q.{self.q_num}: {current_question.text} {True/False} ")    
        