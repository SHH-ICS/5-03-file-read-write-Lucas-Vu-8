# Create a program that will accept a multiple choice question, four answers, and the letter of correct answer. 
# This will be six lines, and then store the questions in the file questions.txt.
# Open the file to store questions
with open("questions.txt", "a") as file:
    # Accept the question from the user
    question = input("Enter the multiple-choice question: ")
    
    # Accept the four answers
    answer_a = input("Enter answer A: ")
    answer_b = input("Enter answer B: ")
    answer_c = input("Enter answer C: ")
    answer_d = input("Enter answer D: ")
    
    # Accept the correct answer letter
    correct_answer = input("Enter the correct answer (A/B/C/D): ").upper()
    
    # Store the formatted question in the file
    file.write(f"{question}\nA) {answer_a}\nB) {answer_b}\nC) {answer_c}\nD) {answer_d}\nCorrect Answer: {correct_answer}\n\n")

print("Question added to questions.txt!")
