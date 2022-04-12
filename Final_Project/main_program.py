"""Final Project: Present user with 10 multiple choice questions. Once all questions are 
answered, save user's name, id, and results in a new file"""

"""JSON is a syntax for storing and exchanging data. JSON is text, written with JavaScript 
object notation.
Python has a built-in package called json, which can be used to work with JSON data"""
import json

"Dictionary to store user's name and id number"
basic_data_dict = {

    "name": "Name",
    "ID": "ID"

}

"Dictionary to hold user's final score"
score_dict = {

    "score": 0
}

"Dictionary to store the correct answer of each question in the Question File"
correct_answer = {

    "answer": " "
}

"""Open a new file, append the user's data and the final score to this file. (File will
hold the data of every run through.)"""
def print_final_data():
    file = open('Question_data.txt','a')
    file.write(json.dumps(basic_data_dict))
    file.write("\n")
    file.write(json.dumps(score_dict))
    file.write("\n\n\n")

"""Take user's answer and compare with the correct one. Based off its correctness,
update the score and return it"""
def answering_question(file, x):
    y = 0
    score = 0
    user_answer = (str(input("Please enter the letter associated with your answer: ")))
    
    while file[x][y] != ":":
        y += 1
    y += 1
    correct_answer.update({"answer": file[x][y]})

    if correct_answer['answer'] == user_answer:
        score += 1
    return(score)

"""Display each question (and its answer choices), have user answer the question
and keep track of the score. Print final score and store in a dictionary"""
def going_through_questions(file):
    i = 0
    score = 0

    while i < len(file):
        mini_counter = 0
        while i < len(file):
            if mini_counter <= 5:
                print(file[i])
            else:
                score += answering_question(file, i)
                i += 1
                break 
            mini_counter += 1
            i += 1   
    print('You scored a ' + str(score) + ' out of 10')
    score_dict.update({"score": score})

"""Open the questions file and use the readlines function.
The readlines() method returns a list containing each line in the file as a list item"""
def question_answer():
    open_file = open('Question_File.txt', "r")
    file = open_file.readlines()
    going_through_questions(file)

"Have user input name and id and store them in a dictionary"
def get_user_data():
    name = (str(input("Please input your first name: ")))
    id = (int(input("Please input your Student ID: ")))
    basic_data_dict.update({"name": name})
    basic_data_dict.update({"ID": id})

"Get user data first, have user answer questions, and store results in a separate file"
def runner_function():
    get_user_data()
    question_answer()
    print_final_data()

runner_function()