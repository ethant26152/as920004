# Football Trivia Quiz (Buggy Version)

def displayInstructions():
    print("\n⚽ Welcome to the Football Trivia Quiz! ⚽")
    print("Answer all questions\n")

def readyQuiz():
    while True:
        ready = input("Are you ready? (yes/no): ").lower().strip()
       
        if ready == "yes":
            return True
        elif ready == "no":
            return    # ERROR: should be False (capital F)
        else:
            print("Invalid input")


# Age input
while True:
    try:
        age = input("Enter your age: ")   # ERROR: not converted to int
       
        if age < 11 or age > 18:          # ERROR: comparing string with int
            print("valid age")
        
        else:
            break
    except:
        print("Error")


displayInstructions()

if not readyQuiz():
    quit()


quiz = {
    1: {
        "question": "Which country won the 2018 World Cup?",
        "options": ["A. Germany", "B. France"],
        "answer": "B"
    }
}

score = 0

for q_num, q_data in quiz.items():
    print(q_data["question"])
   
    for option in q_data["options"]:
        print(option)
   
    user_answer = input("Answer: ").upper()
   
    if user_answer == q_data["answer"]:
        score = score + 1
    else:
        print("Wrong")
   
    print("Current score: " + score)   # ERROR: string + int

print("Final Score:", score)  #This is the error one

#This is the fixed one 
# Football Trivia Quiz (Fixed Version)

def displayInstructions():
    print("\n⚽ Welcome to the Football Trivia Quiz! ⚽")
    print("Answer all questions\n")


def readyQuiz():
    while True:
        ready = input("Are you ready? (yes/no): ").lower().strip()
       
        if ready == "yes":
            return True
        elif ready == "no":
            return False   # FIXED
        else:
            print("Invalid input")


# Age input
while True:
    try:
        age = int(input("Enter your age: "))   # FIXED
       
        if age < 11 or age > 18:
            print("Invalid age")
        else:
            break
    except ValueError:
        print("Please enter a number")   # FIXED specific exception


displayInstructions()

if not readyQuiz():
    quit()


quiz = {
    1: {
        "question": "Which country won the 2018 World Cup?",
        "options": ["A. Germany", "B. France"],
        "answer": "B"
    }
}

score = 0

for q_num, q_data in quiz.items():
    print(q_data["question"])
   
    for option in q_data["options"]:
        print(option)
   
    user_answer = input("Answer: ").upper().strip()
   
    if user_answer == q_data["answer"]:
        score += 1
    else:
        print("Wrong")
   
    print("Current score:", score)   # FIXED

print("Final Score:", score)

