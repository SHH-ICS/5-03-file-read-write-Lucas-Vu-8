def main():
    score = 0
    question_count = 0

    try:
        # Open the file using 'with' for safe handling
        with open("questions.txt", "r") as file:
            for line in file:
                try:
                    # Split the line into parts: question, options, and correct answer
                    parts = line.strip().split(",")
                    if len(parts) != 6:
                        print(f"Skipping improperly formatted line: {line.strip()}")
                        continue
                    
                    question, answer_a, answer_b, answer_c, answer_d, correct_answer = parts
                    question_count += 1

                    # Ask the user the question and show the options
                    print(f"\n{question}")
                    print(f"A. {answer_a}")
                    print(f"B. {answer_b}")
                    print(f"C. {answer_c}")
                    print(f"D. {answer_d}")
                    
                    user_answer = input("Enter your answer (A, B, C, D): ").strip().upper()

                    # Check if the answer is correct
                    if user_answer == correct_answer.upper():
                        print("Correct!")
                        score += 1
                    else:
                        print(f"Wrong! The correct answer is {correct_answer}.")

                except ValueError:
                    print(f"Skipping improperly formatted line: {line.strip()}")

        # Handle case of empty file
        if question_count == 0:
            print("No questions found in the file.")
        else:
            # Display final score
            print(f"\nYour final score is: {score}/{question_count}")

    except FileNotFoundError:
        print("Error: The file 'questions.txt' does not exist. Please create it and try again.")

if __name__ == "__main__":
    main()



