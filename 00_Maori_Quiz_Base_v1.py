"""This will be the draft for the final version - v1
This will have all the other programs combined throughout the development,
continuously adding new programs
Created by Elme Pieterse
09/05/2023"""


# Functions:..........
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


# Instructions function:
def instructions():
    print("Maori Numerals Quiz Instructions")


# Ask for what difficulty function:
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


# display maori numerals function:
def display_maori_numerals():
    print("Maori Numerals")


# Main Routine:
# Instructions:
view_instructions = yes_no_checker("Do you want to see the instructions? "
                                   "(Yes/No): ").lower()
if view_instructions == 'yes' or view_instructions == 'y':
    instructions()
else:
    print()

# Difficulty level:
difficulty_level = difficulty_level_checker("What level of difficulty do you"
                                            " want to choose: Easy(1) or "
                                            "Hard(2): ")
print(f"You entered the level {difficulty_level} difficulty")

# Review Maori Numerals:
review_maori_numerals = yes_no_checker("Do you want to learn or review the "
                                       "maori numerals? (Yes/No): ").lower()
if review_maori_numerals == 'yes' or review_maori_numerals == 'y':
    display_maori_numerals()
else:
    print()
