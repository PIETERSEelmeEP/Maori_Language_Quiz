"""Program's base development - v2
This program contains the instructions and yes/no checker & the formatter added
with the difficulty level question
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


def difficulty_level_checker(question):
    error = "Please retry: Pick a numeral: 1 or 2"

    while True:
        try:
            # Ask what level difficulty
            difficulty_chosen = int(input(question))

            # Check if input is a valid numeral/difficulty
            if difficulty_chosen == 1 or difficulty_chosen == 2:
                return difficulty_chosen
            else:
                print(error)
        except ValueError:
            print(error)


# Main Routine:
# Instructions:
view_instructions = yes_no_checker("Do you want to see the instructions? "
                                   "(Yes/No): ").lower()
if view_instructions == 'yes':
    instructions()
else:
    print("Program continues")

# Difficulty Level questions:
difficulty_level = difficulty_level_checker("What level of difficulty do you"
                                            " want to choose: Easy(1) or "
                                            "Hard(2): ")
print(f"You entered the level {difficulty_level} difficulty")
