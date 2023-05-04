"""Program's instructions & Yes/No Checker - v2
y/n checker will be improved so that the code not only accepts 'yes' & 'no',
but also other variations of answers e,g. 'y' & 'n'
As well as simplifying the input to lower cases
Created by Elme Pieterse
03/05/2023
"""

# Ask if user wants to view instructions
view_instructions = input("Do you want to see the instructions? "
                          "(Yes/No): ").lower()

instructions = "Maori Numerals Quiz Instructions"

# If user input 'yes' or 'y' output will be the instructions
if view_instructions == "yes" or view_instructions == "y":
    print(instructions)

# If user input 'no' or 'n', 'Program continues' will be the output
elif view_instructions == "no" or view_instructions == "n":
    print("Program continues")

# Otherwise the required inputs will be displayed
else:
    print("Please enter either 'Yes' or 'No': ")

print(f"You entered: {view_instructions}")
