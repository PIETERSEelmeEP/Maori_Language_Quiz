"""Program's instructions & Yes/No Checker - v6
This program will take 01_Instructions_Y_N_Checker_v5 and format it to become
aesthetically pleasing to the eye
Created by Elme Pieterse
17/05/2023
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


# instructions function:
def instructions():
    print(formatter("~", "Maori Numerals Quiz Instructions"))
    print()
    print("This program will quiz your knowledge on the Maori numbers 1 to 10")
    print("You will have a option at the start of the quiz to view/learn the "
          "maori numbers 1 to 10, if you choose")
    print()
    print(formatter("-", "Difficulty Level:"))
    print("There is option 1, which is for the beginners (Easy):")
    print("In this quiz the questions are true and false questions, giving you"
          " a 50% chance of being correct")
    print()
    print("OR there is option 2, for the experts (Hard):")
    print("In this quiz the question will say a maori number and you have to "
          "type the number it represents,\nresulting in you having a 10% "
          "chance of being correct")
    print()
    print(formatter("-", "Points System:"))
    print("Your total number of points will depend on the number of questions"
          " you get correct")
    print("You will gain 10 points for every answer that is correct")
    print("Or you will lose 5 points if the answer is incorrect")
    print()
    print("Let the quiz begin!")


# Main Routine:
view_instructions = yes_no_checker("Do you want to see the instructions? "
                                   "(Yes/No): ").lower()
if view_instructions == 'yes':
    instructions()
else:
    print("Program continues")
