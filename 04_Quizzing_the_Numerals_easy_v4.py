"""Program quizzing the user of Maori Numerals (True or False quiz) - v3
Creating the answers
Created by Elme Pieterse
11/05/2023
"""


# together
def question_generator_and_checker():
    import random
    MAORI_NUMERALS = ["tahi", "rua", "toru", "wha", "rima", "ono", "whitu",
                      "waru", "iwa", "tekau"]
    NUMBERS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    maori_numeral = random.choice(MAORI_NUMERALS)
    number = random.choice(NUMBERS)
    question = f"Does {maori_numeral} mean {number}? "

    def true_false_checker(question_text):
        while True:

            # Input a true of false question
            answer = input(question_text).lower()

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
                print("Please enter either 'True' or 'False': ")

    answer_given = true_false_checker(question).lower()
    print("Checking if answer is correct.......")
    return answer_given


# answers
def answers_checker(answer):
    answers_to_questions = [["tahi", 1],["rua", 2], ["toru", 3], ["wha", 4],
                            ["rima", 5], ["ono", 6], ["whitu", 7], ["waru", 8],
                            ["iwa", 9], ["tekau", 10]]


# Main Routine
question_generator_and_checker()
