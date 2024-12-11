score = 0
question_count = 0

try:
    # Open the file using 'with' for safe handling
    with open("questions.txt", "r") as file:
        lines = iter(file.readlines())  # Create an iterator for the file lines
        
        for line in lines:
            question = line.strip()
            if not question:  # Skip empty lines
                continue

            # Read the next lines for the options and correct answer
            answer_a = next(lines).strip()
            answer_b = next(lines).strip()
            answer_c = next(lines).strip()
            answer_d = next(lines).strip()
            correct_answer = next(lines).strip()

            question_count += 1

            # Ask the user the question and show the options
            print(f"{question}")
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

    # Handle case of empty file
    if question_count == 0:
        print("No questions found in the file.")
    else:
        # Display final score
        print(f"Your final score is: {score}/{question_count}")

except FileNotFoundError:
    print("Error")
except StopIteration:
    print("Error")
