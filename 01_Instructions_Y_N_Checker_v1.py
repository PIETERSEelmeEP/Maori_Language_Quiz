"""Program to quiz and teach the first ten maori numerals - v1
ask if user wants to view instructions & yes/no checker
Created by Elme Pieterse
03/05/2023
"""

view_instructions = input("Do you want to see the instructions? (Yes/No): ")
instructions = "Maori Numerals Quiz Instructions"

if view_instructions == "yes":
    print(instructions)
elif view_instructions == "no":
    print("Program continues")
else:
    print("Please enter either 'Yes' or 'No': ")

print(f"You entered: {view_instructions}")
