"""Program teaching the maori numerals 1 to 10 - v1
ask if user wants to learn/review the maori numerals 1 to 10
Created by Elme Pieterse
09/05/2023
"""
# Ask if user wants to view instructions
review_maori_numerals = input("Do you want to learn or revise the maori "
                              "numerals? (Yes/No): ")

MAORI_NUMERALS = "Maori Numerals"

# If user inputs 'yes' output the instructions
if review_maori_numerals == "yes":
    print(MAORI_NUMERALS)

# If user inputs 'no' output 'Program continues'
elif review_maori_numerals == "no":
    print("Program continues")

# Otherwise display required inputs
else:
    print("Please enter either 'Yes' or 'No': ")

