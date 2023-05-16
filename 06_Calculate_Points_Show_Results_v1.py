"""Program calculates the users points - v1
This will calculate the/add/subtract points according to the result_answer,
already put into a function
Created by Elme Pieterse
16/05/2023
"""


def question_generator_hard():
    import random

    MAORI_NUMERALS = ["tahi", "rua", "toru", "wha", "rima", "ono", "whitu",
                      "waru", "iwa", "tekau"]

    maori_numeral = random.choice(MAORI_NUMERALS)
    question = input(f"What number is {maori_numeral}? ")
    return question


# Main Routine
question_generator_hard()