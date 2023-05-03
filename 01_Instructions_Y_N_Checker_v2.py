"""Program to quiz and teach the first ten maori numerals - v2
y/n checker will be improved so that the code not only accepts 'yes' & 'no',
but also other variations of answers e,g. 'y' & 'n'
Created by Elme Pieterse
03/05/2023
"""

view_instructions = input("Do you want to see the instructions? "
                          "(Yes/No): ")
instructions = "Maori Numerals Quiz Instructions"

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
