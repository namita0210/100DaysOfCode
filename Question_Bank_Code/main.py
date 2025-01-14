from data import question_bank

class Question:
    def __init__(self, text, ans):
        self.text = text
        self.ans = ans

#Iterate over question_data
for key in question_bank:
    #Create question object from each entry in question_data
    q_obj = Question(key, val=question_bank.get(key))        
    #Append each question object to question_bank
    question_bank.append(q_obj)