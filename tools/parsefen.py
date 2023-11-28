import random

questions = []

m8n2 = open("m8n2_edited.txt","r")
question = []
for line in m8n2:
    line = line.strip()
    if line == '#':
        questions.append(question)
        question = []
    else:
        question.append(line)
    

m8n2 = open("m8n3_edited.txt","r")
question = []
for line in m8n2:
    line = line.strip()
    if line == '#':
        questions.append(question)
        question = []
    else:
        question.append(line)
    
    
print(random.shuffle(questions))
print(questions)