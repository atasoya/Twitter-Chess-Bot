m8n2 = open("m8n2.txt","r")
lines = []
for line in m8n2:
    if not line.isspace():
      lines.append(line.strip())

questionList = []
question = []
for i in range(len(lines)):
   question.append(lines[i])
   if (i +1) % 3 == 0:
      questionList.append(question)
      question = []
print(questionList)

m8n2_edited = open("m8n2_edited.txt","a")

for q in questionList:
   m8n2_edited.write(f"2\n{q[0]}\n{q[1]}\n{q[2]}\n#\n")