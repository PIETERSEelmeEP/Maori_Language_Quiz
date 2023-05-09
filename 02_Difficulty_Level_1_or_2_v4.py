"""Program asking difficulty Level - v4
This program puts 02_Difficulty_Level_1_or_2_v3 into a function
Created by Elme Pieterse
05/05/2023
"""


# Function:
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


# Main Routine
difficulty_level = difficulty_level_checker("What level of difficulty do you"
                                            " want to choose: Easy(1) or "
                                            "Hard(2): ")
print(f"You entered the level {difficulty_level} difficulty")
