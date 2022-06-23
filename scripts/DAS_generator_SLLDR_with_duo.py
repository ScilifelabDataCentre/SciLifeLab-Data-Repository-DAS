# Access statement generating tool for SciLifeLab Data Repository
import json
import csv
import sys

# Import json file containing questions with answers
with open ('DAS_tool_SLLDR/question_data.json') as json_file:
    question_data = json.load(json_file)
    json_file.close()

# Import dou codes as csv file
duo_data= {}
with open('DAS_tool_SLLDR/duo.json') as duo_csv:
    csv_reader = csv.DictReader(duo_csv)
    for rows in csv_reader:
        label = rows["label"]
        duo_data[label] = rows

# Remove, to SciLifeLab data repository, irrelevant DUO codes
irrelevant_duo = ["no restriction", "publication moratorium", "return to database or resource"]
for i in irrelevant_duo:
    del duo_data[i]

# Write duo codes csv to json
with open("duo.json", "w") as duo_json:
    duo_json.write(json.dumps(duo_data, indent =4))

# Collect all duo labels in one array
answers_duo = []
for labels in duo_data:
    answers_duo.append(labels)

# Display each question and their answers
inputs = []
print("\nData access statement generator for the SciLifeLab Data Repository\n")
for question in question_data:
    question_text = question["question"]
    print("\n" + question_text)
    if question["question_number"]== 1:
        answers = answers_duo
    else:
        answers = question["answers"]
    i = 0
    for ans in answers:
        i = i+1
        print(str(i) + ". " + ans)
    input_option = input("\nInput the number of all options that apply (as 1,2,4): ")
    input_split = input_option.split(',')
    inputs.append(input_split)

# Map input for question 1 to duo codes
choices_q1 = []
i = 0
for i in inputs[0]:
    i = int(i)
    input = answers_duo[i-1]
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

# Print suggested acces statement example 1
# print("\nSuggested Access statement: \n\n The following use conditions appplies: ")
# for i in choices_q1:
#     a = str(choices_q1.index(i) + 1)
#     print(a + "." + i)
# print("\nTo submit an access request please indicate:  ")
# for i in choices_q2:
#     a = str(choices_q2.index(i) + 1)
#     print(a + "." + i)
# print("\nOnce the application is received and assessed, access will be granted   ")
# for i in choices_q3:
#     a = str(choices_q3.index(i) + 1)
#     print(a + "." + i)
# print("\n")

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

#Print suggested access statement example 2 with answers as lists
# print("\nSuggested Access statement:\n\nThe data is not openly avaliabe due to: ")
# for i in choices_q1:
#     a = str(choices_q1.index(i) + 1)
#     print(a + "." + i)
# print("\nTo submit an access request please indicate:  ")
# for i in choices_q2:
#     a = str(choices_q2.index(i) + 1)
#     print(a + "." + i)
# print("\nOnce the application is received and assessed, access will be granted " + choices_q3_das+".\n")
