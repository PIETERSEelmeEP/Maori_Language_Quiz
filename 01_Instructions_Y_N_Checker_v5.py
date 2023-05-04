"""Program's instructions & Yes/No Checker - v4
This program will have the instructions put into a function
Created by Elme Pieterse
04/05/2023
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


# instructions function:
def instructions():
    print("Maori Numerals Quiz Instructions")


# Main Routine:
view_instructions = yes_no_checker("Do you want to see the instructions? "
                                   "(Yes/No): ").lower()
if view_instructions == 'yes' or view_instructions == 'y':
    instructions()
else:
    print("Program continues")
