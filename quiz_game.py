questions = (
    "What is the capital city of Nepal?",
    "How many eyes does a normal human being have?",
    "The most abundant element in the atmosphere is:",
    "How many elements are there in the periodic table?",
    "The hottest planet in the solar system is:"
)

options = (
    ("A. Pokhara", "B. Kathmandu", "C. Butwal",  "D. Biratnagar"), 
    ("A. 2", "B. 1", "C. 3",  "D. None"), 
    ("A. Oxygen", "B. Fluorine", "C. Carbon",  "D. Nitrogen"), 
    ("A. 118", "B. 117", "C. 116",  "D. 120"),
    ("A. Earth", "B. Jupiter", "C. Mercury",  "D. Venus")
)

correct_answers = ("B", "A", "D", "A", "D")
guesses = []

score = 0
question_num = 0

for question in questions:
    print("--------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == correct_answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{correct_answers[question_num]} is the correct answer")
    question_num += 1

print("--------------------------")
print("RESULTS")
print("--------------------------")

print("Correct answers:", end=" ")
for answer in correct_answers:
    print(answer, end=" ")
print()

print("Your guesses:", end=" ")
for guess in guesses:
    print(guess, end=" ")
print()

score_percentage = int((score / len(questions)) * 100)
print(f"Your score is: {score_percentage}%")
