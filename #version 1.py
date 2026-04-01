# ==============================
# Football Trivia Quiz (Final)
# ==============================

# Constants
MIN_AGE = 11
MAX_AGE = 18


# -------- Functions --------

def displayInstructions():
    print("\n⚽ Welcome to the Football Trivia Quiz! ⚽")
    print("Instructions:")
    print("- You will be asked multiple-choice questions.")
    print("- Answer using A, B, C, or D.")
    print("- Your score will be shown at the end.\n")


def getAge():
    while True:
        try:
            age = int(input(f"Enter your age ({MIN_AGE}-{MAX_AGE}): "))
            if age < MIN_AGE or age > MAX_AGE:
                print(f"Age must be between {MIN_AGE} and {MAX_AGE}.")
            else:
                return age
        except ValueError:
            print("Please enter a valid number.")


def readyQuiz():
    while True:
        ready = input("Are you ready to start? (yes/no): ").lower().strip()
       
        if ready == "yes":
            print("\nStarting quiz...\n")
            return True
        elif ready == "no":
            print("Come back when you're ready!")
            return False
        else:
            print("Please enter 'yes' or 'no'.")


def askQuestion(q_num, q_data):
    print(f"\nQuestion {q_num}: {q_data['question']}")
   
    for option in q_data["options"]:
        print(option)
   
    while True:
        answer = input("Your answer (A/B/C/D): ").upper().strip()
        if answer in ["A", "B", "C", "D"]:
            return answer
        else:
            print("Invalid input. Please enter A, B, C, or D.")


def runQuiz(quiz):
    score = 0
   
    for q_num, q_data in quiz.items():
        user_answer = askQuestion(q_num, q_data)
       
        if user_answer == q_data["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! Correct answer: {q_data['answer']}")
   
    return score


def showResults(score, total):
    print(f"\nFinal Score: {score}/{total}")
   
    if score == total:
        print("Perfect score! You're a football expert!")
    elif score >= total * 0.7:
        print("Great job! You know your football!")
    elif score >= total * 0.4:
        print("Not bad! Keep learning!")
    else:
        print("Better luck next time!")


# -------- Main Program --------

def main():
    quiz = {
        1: {
            "question": "Which country won the FIFA World Cup in 2018?",
            "options": ["A. Germany", "B. Brazil", "C. France", "D. Argentina"],
            "answer": "C"
        },
        2: {
            "question": "Who is known as 'The GOAT' by many fans?",
            "options": ["A. Messi", "B. Ronaldo", "C. Neymar", "D. Mbappe"],
            "answer": "A"
        },
        3: {
            "question": "Which club has the most Champions League titles?",
            "options": ["A. Barcelona", "B. Bayern", "C. Real Madrid", "D. Milan"],
            "answer": "C"
        },
        4: {
            "question": "How many players are on the field per team?",
            "options": ["A. 9", "B. 10", "C. 11", "D. 12"],
            "answer": "C"
        },
        5: {
            "question": "Which country is known for Total Football?",
            "options": ["A. Spain", "B. Netherlands", "C. Italy", "D. England"],
            "answer": "B"
            
        },

        6: {
        "question": "Who won the Ballon d'Or in 2021?",
        "options": ["A. Lewandowski", "B. Messi", "C. Ronaldo", "D. Benzema"],
        "answer": "B"
        },
        7: {
        "question": "Which club does Erling Haaland play for (as of 2024)?",
        "options": ["A. Real Madrid", "B. Manchester City", "C. PSG", "D. Dortmund"],
        "answer": "B"
        },
        8: {
        "question": "What is the name of Barcelona's stadium?",
        "options": ["A. Santiago Bernabeu", "B. Camp Nou", "C. Anfield", "D. Old Trafford"],
        "answer": "B"
        },
        9: {
        "question": "Which country hosted the 2014 FIFA World Cup?",
        "options": ["A. South Africa", "B. Germany", "C. Brazil", "D. Russia"],
        "answer": "C"
        },
        10: {
        "question": "Who is the all-time top scorer in World Cup history?",
        "options": ["A. Miroslav Klose", "B. Pele", "C. Ronaldo Nazario", "D. Zidane"],
        "answer": "A"
        }
}
        

    
    displayInstructions()
    getAge()

    if readyQuiz():
        score = runQuiz(quiz)
        showResults(score, len(quiz))
    
# Run program safely
if __name__ == "__main__":
    main()

