quiz ={ 
    "Question 1": {
        "Question" : "what is the capital of France?",
        "answer" : "Paris"
    }, 
    "Question 2": {
        "Question" : "what is the capital of Austria?",
        "answer" : "Vienna"
    }, 
    "Question 3": {
        "Question" : "what is the capital of Italy?",
        "answer" : "Rome"
    }, 
    "Question 4": {
        "Question" : "what is the capital of Switzerland?",
        "answer" : "Bern"
    }, 
    "Question 5": {
        "Question" : "what is the capital of Portugal?",
        "answer" : "Lisbon"
    }, 
    "Question 6": {
        "Question" : "what is the capital of Germany?",
        "answer" : "Berlin"
    }, 
    "Question 7": {
        "Question" : "what is the capital of Spain?",
        "answer" : "Madrid"
    }
}
score = 0

for key, value in quiz.items():
    print(value["Question"])
    Answer = input("Answer = ")
    
    if Answer.lower() == value["answer"].lower():
            print("Correct")
            score = score + 1
            print("your score is: ", str(score))
            print()
            print()
    else:
        print("Incorrect!")
        print("The answer is : " , value["answer"])
        print("your score is", str(score))
        print()
        print()
        

print("You got ", score, "out of 7")
print("Your percentage is ", str(int(score / 7 * 100)), "%")