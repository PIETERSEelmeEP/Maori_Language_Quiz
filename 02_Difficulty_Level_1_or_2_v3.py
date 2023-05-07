"""Program asking difficulty Level - v3
This includes valid numerals/difficulties as the basis of the while loop,
resulting in the 'valid' variable being eliminated, creating a more efficient
program
Created by Elme Pieterse
05/05/2023
"""

# Main Routine
error = "Please retry: Pick a difficulty, Easy(1) or Hard(2)"
difficulty = 0

# Continuously asking until a valid input is given
while not 1 <= difficulty <= 2:
    try:
        difficulty = int(input("What level of difficulty do you want to "
                               "choose: Easy(1) or Hard(2): "))

    except ValueError:
        print(error)

print(f"You entered the level {difficulty} difficulty")
