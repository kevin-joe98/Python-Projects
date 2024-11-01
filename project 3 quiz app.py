# Define quiz questions for different categories
quiz_data = {
    "Science": [
        {
            "question": "What is the chemical symbol for water?",
            "choices": ["H2O", "CO2", "NaCl", "O2"],
            "correct": "H2O"
        },
        {
            "question": "What planet is known as the Red Planet?",
            "choices": ["Mars", "Venus", "Earth", "Jupiter"],
            "correct": "Mars"
        }
    ],
    "Math": [
        {
            "question": "What is 12 * 8?",
            "choices": ["96", "98", "100", "102"],
            "correct": "96"
        },
        {
            "question": "What is the square root of 64?",
            "choices": ["6", "7", "8", "9"],
            "correct": "8"
        }
    ],
    "History": [
        {
            "question": "Who was the first president of the United States?",
            "choices": ["Abraham Lincoln", "George Washington", "Thomas Jefferson", "John Adams"],
            "correct": "George Washington"
        },
        {
            "question": "In what year did World War II end?",
            "choices": ["1942", "1945", "1948", "1950"],
            "correct": "1945"
        }
    ]
}

# Function to display the categories and select one
def select_category():
    print("Please select a quiz category:")
    categories = list(quiz_data.keys())
    for i, category in enumerate(categories, 1):
        print(f"{i}. {category}")
    
    # Get user input and validate it
    choice = int(input("Enter the number corresponding to your choice: "))
    if 1 <= choice <= len(categories):
        return categories[choice - 1]
    else:
        print("Invalid selection. Please try again.")
        return select_category()

# Function to display the quiz questions and track the score
def run_quiz(category):
    questions = quiz_data[category]
    score = 0
    
    # Ask each question
    for q in questions:
        print("\n" + q["question"])
        for i, option in enumerate(q["choices"], 1):
            print(f"{i}. {option}")
        
        # Get user's answer and check if it's correct
        answer = int(input("Enter the number of your answer: "))
        if q["choices"][answer - 1] == q["correct"]:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer is {q['correct']}.")
    
    # Return the final score
    return score, len(questions)

# Main function to run the quiz
def main():
    category = select_category()
    print(f"\nYou selected the {category} quiz.")
    
    score, total_questions = run_quiz(category)
    
    # Show final score
    print(f"\nQuiz Over! You scored {score} out of {total_questions}.")

if __name__ == "__main__":
    main()
