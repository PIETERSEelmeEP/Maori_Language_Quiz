"""Program teaching the maori numerals 1 to 10 - v2
learn/review maori numerals will be improved so that the code not only
accepts 'yes' & 'no', but also other variations of answers e,g. 'y' & 'n'
As well as simplifying the input to lower cases
Created by Elme Pieterse
09/05/2023
"""

# Ask if user wants to view instructions
review_maori_numerals = input("Do you want to learn or revise the maori "
                              "numerals? (Yes/No): ").lower()

MAORI_NUMERALS = "Maori Numerals"

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
