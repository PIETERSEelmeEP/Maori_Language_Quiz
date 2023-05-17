"""Program teaching the maori numerals 1 to 10 - v1
this puts Maori numerals into a function with the correct results with the
formatter
Created by Elme Pieterse
09/05/2023
"""


def formatter(_symbol, _text):
    sides = _symbol * 3
    formatted_text = f"{sides} {_text} {sides}"
    top_bottom = _symbol * len(formatted_text)
    return f"{top_bottom}\n{formatted_text}\n{top_bottom}"


def maori_numerals():
    print(formatter("~", "Maori Numerals:"))
    print()
    print("Tahi = 1")
    print("Rua = 2")
    print("Toru = 3")
    print("Wha = 4")
    print("Rima = 5")
    print("Ono = 6")
    print("Whitu = 7")
    print("Waru = 8")
    print("Iwa = 9")
    print("Tekau = 10")
    print()


def yes_no_checker(question_text):
    while True:

        # Ask if user wants to view instructions
        answer = input(question_text).lower()

        # If user input 'yes' or 'y' output will be the instructions
        if answer == "yes" or answer == "y":
            answer = "Yes"
            return answer

        # If user input 'no' or 'n', 'Program continues' will be the output
        elif answer == "no" or answer == 'n':
            answer = "No"
            return answer

        # Otherwise the required inputs will be displayed
        else:
            print("Please enter either 'Yes' or 'No': ")


review_maori_numerals = yes_no_checker("Do you want to learn or revise the "
                                       "maori numerals? (Yes/No): ").lower()
if review_maori_numerals == "yes":
    maori_numerals()
else:
    print("Program continues")
