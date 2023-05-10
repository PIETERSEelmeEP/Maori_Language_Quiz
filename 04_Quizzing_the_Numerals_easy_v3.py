"""Program quizzing the user of Maori Numerals (True or False quiz) - v3
The ture/false combined with the random numbers/maori numerals to create
a question that has an input, as well as the question generator being turned
into a function
Created by Elme Pieterse
10/05/2023
"""


def question_generator():
    import random
    MAORI_NUMERALS = ["tahi", "rua", "toru", "wha", "rima", "ono", "whitu",
                      "waru", "iwa", "tekau"]
    NUMBERS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    maori_numeral = random.choice(MAORI_NUMERALS)
    number = random.choice(NUMBERS)
    question = input(f"Does {maori_numeral} mean {number}? (True or False): ")
    return question


# True or False checker Function:
def true_false_checker(question_text):
    while True:

        # Input a true of false question
        answer = question_text.lower()

        # If user input 'true' or 't' output will be 'checking if answer
        # is correct'
        if answer == "true" or answer == "t":
            answer = "True"
            return answer

        # If user input 'false' or 'f' output will be 'checking if answer
        # is correct'
        elif answer == "false" or answer == "f":
            answer = "False"
            return answer

        # Otherwise the required inputs will be displayed
        else:
            answer = input("Please enter either 'True' or 'False': ")


# Main Routine
answer_given = true_false_checker(question_generator()).lower()
print("Checking if answer is correct.......")
