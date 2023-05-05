"""Program asking difficulty Level - v3
This program puts 02_Difficulty_Level_1_or_2_v2 into a function
Created by Elme Pieterse
05/05/2023
"""


# Functions:
def difficulty_level_checker(question):
    while True:

        # Ask what level difficulty
        difficulty_chosen = int(input(question))

        # If user inputs '1' output the easy level questions
        if difficulty_chosen == 1:
            difficulty_chosen = 1
            return difficulty_chosen

        # If user inputs '2' output the hard level questions
        elif difficulty_chosen == 2:
            difficulty_chosen = 2
            return difficulty_chosen

        # Otherwise display required inputs
        else:
            print("Please enter the numerals '1' or '2'")


# Main Routine
difficulty_level = difficulty_level_checker("What level of difficulty do you "
                                            "want to choose: Easy(1) or "
                                            "Hard(2): ")

if difficulty_level == 1:
    print("Easy level questions")
else:
    print("Hard level questions")

