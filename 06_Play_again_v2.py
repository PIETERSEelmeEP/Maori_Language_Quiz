"""Program's play again function - v1
This program will take 06_Play_again_v1 and format it to become
aesthetically pleasing to the eye with the correct notes
Created by Elme Pieterse
19/05/2023
"""


# Functions:
# function to format text
def formatter(_symbol, _text):
    sides = _symbol * 3
    formatted_text = f"{sides} {_text} {sides}"
    top_bottom = _symbol * len(formatted_text)
    return f"{top_bottom}\n{formatted_text}\n{top_bottom}"


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
    print(formatter("~", "Thank you"))
    print()
    print("Enjoy the rest of your day!")


# Main Routine:
exit_program = yes_no_checker("Do you want to exit the quiz? "
                              "(Yes/No): ").lower()
if exit_program == 'yes':
    thanks_note()
else:
    print("Program restarts")
