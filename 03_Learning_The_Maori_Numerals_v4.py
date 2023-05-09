"""Program teaching the maori numerals 1 to 10 - v4
This program puts 03_Learning_The_Maori_Numerals_v3 into a function
The yes/no checker is reused from 01_Instructions_Y_N_Checker_v4
Created by Elme Pieterse
09/05/2023
"""


# Functions:
# yes/no checker function:
def yes_no_checker(question_text):
    while True:

        # Ask if user wants to view the maori numerals
        answer = input(question_text).lower()

        # If user input 'yes' or 'y' output will be the maori numerals
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


# display maori numerals function:
def display_maori_numerals():
    print("Maori Numerals")


# Main Routine:
review_maori_numerals = yes_no_checker("Do you want to learn or review the "
                                       "maori numerals? (Yes/No): ").lower()
if review_maori_numerals == 'yes' or review_maori_numerals == 'y':
    display_maori_numerals()
else:
    print("Program continues")
