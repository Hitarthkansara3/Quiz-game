# quiz game

questions = ("Which of the following is a python data type ?",
            "What does SQL stand for ?",
            "Which library is mainly used for data manipulation in Python ?",
            "Who is known as father of computer ?",
            "Which company develop the programming language Python ?")

options = (("A. HTML", "B. Tuple", "C. CSS", "D. SQL"),
           ("A. Structured Query Language", "B. Strong Question List," "C.Simple Query Logic", "D. System Query Link"),
           ("A. Pandas", "B.NumPy", "C. Matplotlib", "D. Scikit-learn"),
           ("A. Charlse Babbage", "B. Alan Turing", "C. Chris gayle", "D. John Von Neumann"),
           ("A. Google", "B. Microsoft", "C. Python Softwear Foundation", "D. Guido van Rossum"))

answers = ("B", "A", "A", "A", "D")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("--------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A B C D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct!")
    else:
        print("INCORRECT")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("--------------------------------")
print("------------RESULTS-------------")
print("--------------------------------")

print("Answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(question) * 100)
print(f"Your score is {score}%")
