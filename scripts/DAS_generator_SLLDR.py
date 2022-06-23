#Access statement generating tool
import json
import sys

# Import json file containing questions with answers
with open ('question_data.json') as json_file:
    question_data = json.load(json_file)
    json_file.close()


# Display each question
inputs = []
for question in question_data:
    question_text = question["question"]
    print(question_text)
    answers = question["answers"]
    i = 0
    for ans in answers:
        i = i+1
        print(str(i) + ". " + ans)
    input_option = input("Input the number of all options that apply (as 1,2,4): ")
    input_split = input_option.split(',')
    inputs.append(input_split)

# Map input for question 1 to answers
choices_q1 = []
i = 0
for i in inputs[0]:
    i = int(i)
    input = question_data[0]["answers"][i-1]
    choices_q1.append(input)

# Map input for question 2 to answers
choices_q2 = []
i = 0
for i in inputs[1]:
    i = int(i)
    input = question_data[1]["answers"][i-1]
    choices_q2.append(input)

# Map input for question 3 to the answers corresponding text in the statement
choices_q3 = []
i = 0
for i in inputs[2]:
    i = int(i)
    input = question_data[2]["text_in_statement"][i-1]
    choices_q3.append(input)

# Convert inputted answers to each question to text for the data access statement
# Q1
if (len(choices_q1))==1:
    choices_q1_das = ", ".join(choices_q1)
else:
    choices_q1_das = ", ".join(choices_q1[0:len(choices_q1)-1])
    choices_q1_das = str(choices_q1_das)+" and "+ str(choices_q1[len(choices_q1)-1])
# Q2
if (len(choices_q2))==1:
    choices_q2_das = ", ".join(choices_q2)
else:
    choices_q2_das = ", ".join(choices_q2[0:len(choices_q2)-1])
    choices_q2_das = str(choices_q2_das)+" and "+ str(choices_q2[len(choices_q2)-1])
# Q3
if (len(choices_q3))==1:
    choices_q3_das = ", ".join(choices_q3)
else:
    choices_q3_das = ", ".join(choices_q3[0:len(choices_q3)-1])
    choices_q3_das = str(choices_q3_das)+" and "+ str(choices_q3[len(choices_q3)-1])

# Print suggested acces statement example 2 as a coherent text
print("\nSuggested Access statement:\nThe data is not openly avaliabe due to: "+ choices_q1_das + ". To submit an access request please indicate: "+ choices_q2_das +". Once the application is received and assessed, access will be granted " + choices_q3_das+".\n")
