def main():
    score = 0
    question_count = 0

    try:
        # Open the file using 'with' for safe handling
        with open("hello_world.txt", "r") as file:
            for line in file:
                try:
                    question, correct_answer = line.strip().split(",", 1)
                    question_count += 1

                    # Ask the user the question
                    user_answer = input(f"{question} ").strip()

                    # Check if the answer is correct
                    if user_answer.lower() == correct_answer.lower():
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
