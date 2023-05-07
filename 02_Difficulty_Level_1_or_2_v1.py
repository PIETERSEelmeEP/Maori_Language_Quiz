"""Program asking difficulty Level - v1
ask what level of difficulty does the user want to play, Easy(1) or Hard(2),
and check if it is a valid input
Created by Elme Pieterse
04/05/2023
"""
# Ask what level difficulty
difficulty = int(input("What level of difficulty do you want to choose: "
                       "Easy(1) or Hard(2): "))

# Continue asking for a valid input if invalid input is given
while not 1 <= difficulty <= 2:
    print("Please retry: Pick a difficulty, Easy(1) or Hard(2)")
    #   Ask for an input again
    difficulty = int(input("Please enter the numerals '1' or '2': "))

print(f"You entered the level {difficulty} difficulty")
