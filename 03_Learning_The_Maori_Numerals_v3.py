"""Program teaching the maori numerals 1 to 10 - v3
This converts the program form 03_Learning_The_Maori_Numerals_v2 into a loop
inorder to make it easier and more effective to test
Created by Elme Pieterse
09/05/2023
"""

review_maori_numerals = ""
MAORI_NUMERALS = "Maori Numerals"
while review_maori_numerals != "a":

    # Ask if user wants to learn/review the maori numerals
    review_maori_numerals = input("Do you want to see the instructions? "
                                  "(Yes/No): ").lower()

    # If user input 'yes' or 'y' output will be the maori numerals
    if review_maori_numerals == "yes" or review_maori_numerals == "y":
        print(MAORI_NUMERALS)

    # If user input 'no' or 'n', 'Program continues' will be the output
    elif review_maori_numerals == "no" or review_maori_numerals == "n":
        print("Program continues")

    # Otherwise the required inputs will be displayed
    else:
        print("Please enter either 'Yes' or 'No': ")

    print(f"You entered: {review_maori_numerals}")
