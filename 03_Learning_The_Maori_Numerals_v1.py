"""Program teaching the maori numerals 1 to 10 - v1
ask if user wants to learn/review the maori numerals 1 to 10
Created by Elme Pieterse
09/05/2023
"""
MAORI_NUMERALS = "Maori Numerals"


# functions:
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


# main routine:
review_maori_numerals = yes_no_checker("Do you want to learn or revise the "
                                       "maori numerals? (Yes/No): ")
if review_maori_numerals == "yes":
    print(MAORI_NUMERALS)
else:
    print("Program continues")
