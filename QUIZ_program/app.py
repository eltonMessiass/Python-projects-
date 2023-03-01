# a dictionary that stores questions and answers
# have a variable that tracks the score of the player
# loop through the dictionary using key values pairs
# display each question to the user and allow them to answer
# tell them if they are right or wrong
# show the final result when quiz is completed


quiz = {
    "question1": {
        "question": "What is the capital of france",
        "answer": "Paris"
    },
    "question2":{
        "question": "what is the capital of Germany?",
        "answer": "Berlin"
    },
    "question3":{
        "question": "what is the capital of Italy?",
        "answer": "Rome"
    },
    "question4":{
        "question": "what is the capital of Spain?",
        "answer": "Madrid"
    },
    "question5":{
        "question": "what is the capital of Portugal?",
        "answer": "Lisbon"
    },
    "question6":{
        "question": "what is the capital of Switzerland?",
        "answer": "Bern"
    },
    "question7":{
        "question": "what is the capital of Austria?",
        "answer": "Vienna"
    },
}

score = 0

for key, value in quiz.items():
    print(value['question'])
    answer = input("Answer? ")

    if answer.lower() == value['answer'].lower():
        print("Correct")
        score += 1
        print (f"Your score is: {str(score)}")

    else:
        print("Wrong!")
        print(f"The answer is : {value['answer']}")
        print (f"Your score is: {str(score)}")
print(f"\n {30 * '*'}" )
print(f"You got {str(score)} out of 7 questions correctly")
print(f"Your percentage is {str(int(score/7 * 100))}%")