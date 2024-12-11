score = 0
question_count = 0

try:
    # Open the file using 'with' for safe handling
    with open("questions.txt", "r") as file:
        lines = file.readlines()
        
        i = 0
        while i < len(lines):
            # Read the question block
            question = lines[i].strip()
            answer_a = lines[i + 1].strip()
            answer_b = lines[i + 2].strip()
            answer_c = lines[i + 3].strip()
            answer_d = lines[i + 4].strip()
            correct_answer = lines[i + 5].strip()
            
            question_count += 1

            # Ask the user the question and show the options
            print(f"\n{question}")
            print(f"A. {answer_a}")
            print(f"B. {answer_b}")
            print(f"C. {answer_c}")
            print(f"D. {answer_d}")
            
            user_answer = input("Enter your answer (A, B, C, D): ").upper()

            # Check if the answer is correct
            if user_answer == correct_answer.upper():
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The correct answer is {correct_answer}.")

            # Move to the next question block
            i += 7  # Skip to the next question block (6 lines + 1 blank line)

    # Handle case of empty file
    if question_count == 0:
        print("No questions found in the file.")
    else:
        # Display final score
        print(f"\nYour final score is: {score}/{question_count}")

except FileNotFoundError:
    print("Error: The file 'questions.txt' does not exist. Please create it and try again.")
