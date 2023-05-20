"""Program's instructions & Yes/No Checker - v1
ask if user wants to view instructions & yes/no checker
Created by Elme Pieterse
03/05/2023
"""
# Ask if user wants to view instructions
view_instructions = input("Do you want to see the instructions? (Yes/No): ")

instructions = "Maori Numerals Quiz Instructions"

# If user inputs 'yes' output the instructions
if view_instructions == "yes":
    print(instructions)

# If user inputs 'no' output 'Program continues'
elif view_instructions == "no":
    print("Program continues")

# Otherwise display required inputs
else:
    print("Please enter either 'Yes' or 'No': ")
