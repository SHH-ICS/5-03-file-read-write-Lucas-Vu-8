# Create a program that will accept a multiple choice question, four answers, and the letter of correct answer. 
# This will be six lines, and then store the questions in the file questions.txt.

while True:
    # Collect inputs from the user
    question = input("Enter the question: ")
    answer_a = input("Enter option A: ")
    answer_b = input("Enter option B: ")
    answer_c = input("Enter option C: ")
    answer_d = input("Enter option D: ")
    correct_answer = input("Enter the correct answer (A, B, C, D): ").upper()

    # Validate the correct answer
    while correct_answer not in ["A", "B", "C", "D"]:
        print("Invalid input. Please enter A, B, C, or D.")
        correct_answer = input("Enter the correct answer (A, B, C, D): ").upper()

    # Save the question, options, and correct answer in the desired format
    with open("questions.txt", "a") as file:  # Use 'a' to append to the file
        file.write(f"{question}\n")
        file.write(f"{answer_a}\n")
        file.write(f"{answer_b}\n")
        file.write(f"{answer_c}\n")
        file.write(f"{answer_d}\n")
        file.write(f"{correct_answer}\n\n")  # Add a blank line to separate questions

    # Ask if the user wants to add another question
    another = input("Add another question? (yes/no): ").strip().lower()
    if another != "yes":
        break
