"""Program asking difficulty Level - v2
Use try/except and pull the error message out of the loop
Created by Elme Pieterse
05/05/2023
"""

error = "Please retry: Pick a difficulty, Easy(1) or Hard(2)"
valid = False

# Continuously asking until a valid input is given
while not valid:
    try:
        # Ask what difficulty the user would prefer
        difficulty = int(input("What level of difficulty do you want to "
                               "choose: Easy(1) or Hard(2): "))

        # Check if input is a valid numeral/difficulty
        if difficulty == 1 or difficulty == 2:
            print(f"You entered the level {difficulty} difficulty")
            valid = True
        else:
            print(error)
    except ValueError:
        print(error)
