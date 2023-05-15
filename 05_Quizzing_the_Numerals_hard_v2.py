"""Program quizzing the user of Maori Numerals - v1
The question generator and its answer checker, to ensure a valid input is
entered
Created by Elme Pieterse
15/05/2023
"""


def question_generator_and_checker_hard():
    import random
    MAORI_NUMERALS = ["tahi", "rua", "toru", "wha", "rima", "ono", "whitu",
                      "waru", "iwa", "tekau"]
    maori_numeral = random.choice(MAORI_NUMERALS)
    question = input(f"What number is {maori_numeral}? ")

    def answer_checker(question_text):
        while True:

            # Input a question
            answer = input(question_text).lower()

            # If user input 'true' or 't' output will be 'checking if answer
            if answer == "true" or answer == "t":
                answer = "True"
                return answer

            # If user input 'false' or 'f' output will be 'checking if answer
            elif answer == "false" or answer == "f":
                answer = "False"
                return answer

            # Otherwise the required inputs will be displayed
            else:
                print("Please enter either 'True' or 'False': ")

    answer_given = answer_checker(question).lower()
    print("Checking if answer is correct.......")
    return answer_given


# Main Routine
question_generator_and_checker_hard()
