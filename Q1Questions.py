# Create a program that will accept a multiple choice question, four answers, and the letter of correct answer. 
# This will be six lines, and then store the questions in the file questions.txt.
while True:
    # Collect inputs from the user
    question = input("Enter the question: ")
    answer_a = input("Enter option A: ")
    answer_b = input("Enter option B: ")
    answer_c = input("Enter option C: ")
    answer_d = input("Enter option D: ")
    correct_answer = input("Enter the correct answer: ").strip()

    # Save the question, options, and correct answer in the desired format
    with open("questions.txt", "a") as file:  # Use 'a' to append to the file
        file.write(f"{question},{answer_a},{answer_b},{answer_c},{answer_d},{correct_answer}\n")

    # Ask if the user wants to add another question
    another = input("Add another question? yes or no: ")
    if another != "yes":
        break

