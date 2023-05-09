"""Program's instructions & Yes/No Checker - v3
This converts the program from 01_Instructions_Y_N_Checker_v2 into a loop
inorder to make it easier and more effective to test
Created by Elme Pieterse
03/05/2023
"""

view_instructions = ""
instructions = "Maori Numerals Quiz Instructions"
while view_instructions != "a":

    # Ask if user wants to view instructions
    view_instructions = input("Do you want to see the instructions? "
                              "(Yes/No): ").lower()

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
