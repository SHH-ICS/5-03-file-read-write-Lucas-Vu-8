# Create a program that will accept a multiple choice question, four answers, and the letter of correct answer. 
# This will be six lines, and then store the questions in the file questions.txt.
# Open the file to store questions
question = input("Enter the question")
answer_a = input("Enter option A")
answer_b = input("Enter option B")
answer_c = input("Enter option C")
answer_d = input("Enter option D")
correct_answer = input("Enter the correct answer").upper()
with open("hello_world.txt","w") as file:

    file.write(answer_a)
    file.write(answer_b)
    file.write(answer_c)
    file.write(answer_d)
    file.write(correct_answer)