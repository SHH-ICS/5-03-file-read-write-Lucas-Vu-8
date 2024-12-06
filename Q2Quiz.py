
score = 0
question_count = 0

try:
    # Open the file using 'with' for safe handling
    with open("hello_world.txt", "r") as file:
        for line in file: #loop that iterates through each line in the file
            try:
                question, correct_answer = line.strip().split(",", 1)
                question_count += 1
                # Splits the string into two parts based on the first comma it encounters
                #.strip removes any leading
                # Ask the user the question
                user_answer = input(f"{question} ").strip()

                # Check if the answer is correct
                if user_answer.lower() == correct_answer.lower():
                    print("correct")
                    score += 1
                else:
                    print(f"Wrong the answer was {correct_answer}.")
            except ValueError:
                print("")
    
    # Handle case of empty file
    if question_count == 0:
        print("No questions found in the file.")
    else:
        # Display final score
        print(f"\nYour final score is: {score}/{question_count}")

except FileNotFoundError:
    print("Error")

