questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Madrid", "Rome"],
        "answer": "Paris"
    },
    {
        "question": "Who invented the telephone?",
        "options": ["Thomas Edison", "Alexander Graham Bell", "Nikola Tesla", "Marie Curie"],
        "answer": "Alexander Graham Bell"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["Venus", "Jupiter", "Mercury", "Mars"],
        "answer": "Jupiter"
    }
]

def ask_question(question):
    print(question["question"])
    for i, option in enumerate(question["options"]):
        print(f"{i+1}. {option}")
    answer = input("Enter your answer (1-4): ")
    return question["options"][int(answer)-1] == question["answer"]

def play_quiz():
    score = 0
    for question in questions:
        if ask_question(question):
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect! The correct answer is {question['answer']}")
    print(f"Your final score is {score}/{len(questions)}")

play_quiz()
