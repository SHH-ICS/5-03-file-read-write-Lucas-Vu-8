# Create a second program that will read the file questions.txt, formatted as described above, and pose the questions to the user. 
# The program will keep score of the number of questions answered correctly.
def main():
    score = 0

    # Open the file (assumes the file exists)
    file = open("questions.txt", "r")
    for line in file:
        question, correct_answer = line.strip().split(",")

        # Ask the user the question
        user_answer = input(f"{question} ").strip()

        # Check if the answer is correct
        if user_answer.lower() == correct_answer.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {correct_answer}.")

    file.close()

    # Display final score
    print(f"\nYour final score is: {score}")

if __name__ == "__main__":
    main()


