"""Program quizzing the user of Maori Numerals - v1
This will be the question generator/maori numeral generator, already put into
a function
Created by Elme Pieterse
15/05/2023
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
