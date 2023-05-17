"""Program quizzing the user of Maori Numerals (True or False quiz) - v5
this takes 04_quizzing_the_numerals_easy_v4 and repeats the program 20 times
Created by Elme Pieterse
17/05/2023
"""


# True or False checker Function:
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


def question_generator_and_answers_easy():
    import random

    MAORI_NUMERALS = ["tahi", "rua", "toru", "wha", "rima", "ono", "whitu",
                      "waru", "iwa", "tekau"]
    NUMBERS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    maori_numeral = random.choice(MAORI_NUMERALS)
    number = random.choice(NUMBERS)
    question = f"Does {maori_numeral} mean {number}? "
    answer = true_false_checker(question).lower()

    def answer_given_t_or_f(true_false_):
        if answer != true_false_:
            print("Correct, Amazing job!")
        else:
            print("Sorry, keep trying, you can do it!")

    if maori_numeral == "tahi" and number == 1:
        answer_given_t_or_f("false")
    elif maori_numeral == "rua" and number == 2:
        answer_given_t_or_f("false")
    elif maori_numeral == "toru" and number == 3:
        answer_given_t_or_f("false")
    elif maori_numeral == "wha" and number == 4:
        answer_given_t_or_f("false")
    elif maori_numeral == "rima" and number == 5:
        answer_given_t_or_f("false")
    elif maori_numeral == "ono" and number == 6:
        answer_given_t_or_f("false")
    elif maori_numeral == "whitu" and number == 7:
        answer_given_t_or_f("false")
    elif maori_numeral == "waru" and number == 8:
        answer_given_t_or_f("false")
    elif maori_numeral == "iwa" and number == 9:
        answer_given_t_or_f("false")
    elif maori_numeral == "tekau" and number == 10:
        answer_given_t_or_f("false")
    else:
        answer_given_t_or_f("true")


# Main Routine
question_generator_and_answers_easy()
