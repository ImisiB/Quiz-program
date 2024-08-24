quiz = {
    "Question 1": {
        "Question": "What is the capital of France",
        "answer": "Paris"
    },
    "Question 2": {
        "Question": "What is the capital of Germany",
        "answer": "Berlin"
    },
    "Question 3": {
        "Question": "what is the capital of Italy",
        "answer": "Rome"
    },
    "Question 4":{
        "Question": "what is the capital of Spain",
        "answer": "Madrid"
    },    
    "Question 5":{
        "Question": "what is the capital of Portugal",
        "answer": "Lisbon"
    },
    "Question 6":{
        "Question": "what is the capital of switzerland",
        "answer": "Bern"
    },    
    "Question 7":{
        "Question": "what is the capital of Austria",
        "answer": "Vienna"
    }
}

score = 0

for  key, value in quiz.items():
    print(value["Question"])
    answer = input("Answer? ")
    
    if answer.lower() == value["answer"].lower():
        print("Correct")
        score = score + 1
        print("Your score is:" + str(score))
        print()
        print()
        
    else:
        print("Wrong")
        print("The answer is:" + value["answer"])
        print("Your score is:" + str(score))
        print()
        print() 

print("You got " + str(score) + " out of 7 questions correctly")
print("Your percentage is ", str(int(score/7 * 100)), "%")
