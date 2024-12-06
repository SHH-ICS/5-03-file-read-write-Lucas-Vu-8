# Create a program that will accept a multiple choice question, four answers, and the letter of correct answer. 
# This will be six lines, and then store the questions in the file questions.txt.
def main():
    while True:
        # Collect inputs from the user
        question = input("Enter the question: ")
        answer_a = input("Enter option A: ")
        answer_b = input("Enter option B: ")
        answer_c = input("Enter option C: ")
        answer_d = input("Enter option D: ")
        correct_answer = input("Enter the correct answer: ").strip()

        # Save the question, options, and correct answer in the desired format
        with open("hello_world.txt", "a") as file:  # Use 'a' to append to the file
            file.write(f"{question},{correct_answer},{answer_a},{answer_b},{answer_c},{answer_d}\n")

        # Ask if the user wants to add another question
        another = input("Add another question? (yes/no): ").strip().lower()
        if another != "yes":
            break

if __name__ == "__main__":
    main()

