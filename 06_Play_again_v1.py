"""Program's play again function - v1
ask if user wants end the quiz of repeat, all ready into functions
I took the template from the instructions program, due to the same structure
Created by Elme Pieterse
19/05/2023
"""


# Functions:
# yes/no checker function:
def yes_no_checker(question_text):
    while True:

        # Ask if user wants to view instructions
        answer = input(question_text).lower()

        # If user input 'yes' or 'y' output will be the instructions
        if answer == "yes" or answer == "y":
            answer = "Yes"
            return answer

        # If user input 'no' or 'n', 'Program continues' will be the output
        elif answer == "no" or answer == 'n':
            answer = "No"
            return answer

        # Otherwise the required inputs will be displayed
        else:
            print("Please enter either 'Yes' or 'No': ")


# thank you function:
def thanks_note():
    print("Thank you")


# Main Routine:
exit_program = yes_no_checker("Do you want to exit the quiz? "
                              "(Yes/No): ").lower()
if exit_program == 'yes':
    thanks_note()
else:
    print("Program restarts")
