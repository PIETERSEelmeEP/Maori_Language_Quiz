"""Program quizzing the user of Maori Numerals (True or False quiz) - v1
This will be only the True or False checker inorder to prevent any invalid
inputs to cause an error/crash (This will go straight into a function)
Created by Elme Pieterse
09/05/2023
"""


# True or False checker Function:
def true_false_checker(question_text):
    while True:

        # Input a true of false question
        answer = input(question_text).lower()

        # If user input 'true' or 't' output will be 'checking if answer
        # is correct'
        if answer == "true" or answer == "t":
            answer = "True"
            return answer

        # If user input 'false' or 'f' output will be 'checking if answer
        # is correct'
        elif answer == "false" or answer == "f":
            answer = "False"
            return answer

        # Otherwise the required inputs will be displayed
        else:
            print("Please enter either 'True' or 'False': ")


# Main Routine
answer_given = true_false_checker("Does Tahi mean 3? ").lower()
print("Checking if answer is correct.......")
