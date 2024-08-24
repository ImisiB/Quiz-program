#   Quiz-program

To create a quiz program, you have to follow a few steps:

1. Make a dictionary with a variable(quiz), then write out the question like this:
quiz = {
    "Question 1": {
        "Question": "What is the capital of France",
        "answer": "Paris"
    },
}
Notice the comma i made in the the 2nd to the last bracket, in case you want to add other questions
2. I added other questions to it using the same method i used above, then i made a variable(user) to keep track of the score of the user, then i used for loop like this;
for key, value in quiz.items():
    print(value["Question"])
    Answer = input("Answer = ")
3. I made an if statement for(Answer.lower() == value["answer"].lower()). I added lower() so if the user type the answer in lower or upper case or both, the answer will be correct.
4. After the if statement, something so the user will know if they are correct("correct"). Then use the variable(score) and add 1 to it(score = score + 1). Then print something like;
print("Your score is: ", str(score))
print()
print()
5. Make an else statement to print 'incorrect', so if the user's answer is wrong they will know, then print something like;
print("your score is", str(score))
print()
print()
So the user will know their score. Notice the spaces i added by using: print()
6. After all that, in another line but not under the else statement or the for loop, print;
print("You got ", score, "out of 7")
print("Your percentage is ", str(int(score / 7 * 100)), "%")
So the user will know their total score

