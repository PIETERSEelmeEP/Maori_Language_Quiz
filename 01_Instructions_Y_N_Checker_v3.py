"""Program to quiz and teach the first ten maori numerals - v3
the instructions will display correctly, & no errors will be present
Created by Elme Pieterse
03/05/2023
"""

view_instructions = input("Do you want to see the instructions? "
                          "(Yes/No): ").lower()
instructions = "Maori Numerals Quiz Instructions:\nThere are to difficulty " \
               "levels, Easy(1) or Hard(2)\nYou will be quizzed based off " \
               "your difficulty\nDifficulty: Easy\nYou will be given the " \
               "maori name of a number\nYou will be asked what "

if view_instructions == "yes":
    print(instructions)
elif view_instructions == "y":
    print(instructions)
elif view_instructions == "no":
    print("Program continues")
elif view_instructions == "n":
    print("Program continues")
else:
    print("Please enter either 'Yes' or 'No': ")

print(f"You entered: {view_instructions}")
