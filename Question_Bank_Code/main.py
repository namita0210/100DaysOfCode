from data import question_data
from model import Question

question_bank = []

#Iterate over question_data
for key in question_data:
    text = key["text"]
    ans = key["ans"]
    #Create question object from each entry in question_data
    q_obj = Question(key, ans)        
    #Append each question object to question_data
    question_bank.append(q_obj)

print(question_bank)    