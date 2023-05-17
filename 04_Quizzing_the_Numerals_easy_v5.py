"""Program quizzing the user of Maori Numerals (True or False quiz) - v4
this takes 04_quizzing_the_numerals_easy_v4 and repeats it twenty times
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
    true_false_checker(question)
    answer = question

    one = "tahi" and 1
    two = "rua" and 2
    three = "toru" and 3
    four = "wha" and 4
    five = "rima" and 5
    six = "ono" and 6
    seven = "whitu" and 7
    eight = "waru" and 8
    nine = "iwa" and 9
    ten = "tekau" and 10

    def answer_given_t_or_f(true_false_):
        if answer != true_false_:
            print("Correct, Amazing job!")
        else:
            print("Sorry, keep trying, you can do it!")

    if maori_numeral and number != one:
        if maori_numeral and number != two:
            if maori_numeral and number != three:
                if maori_numeral and number != four:
                    if maori_numeral and number != five:
                        if maori_numeral and number != six:
                            if maori_numeral and number != seven:
                                if maori_numeral and number != eight:
                                    if maori_numeral and number != nine:
                                        if maori_numeral and number != ten:
                                            print()
                                        else:
                                            answer_given_t_or_f("false")
                                    else:
                                        answer_given_t_or_f("true")
                                else:
                                    answer_given_t_or_f("true")
                            else:
                                answer_given_t_or_f("true")
                        else:
                            answer_given_t_or_f("true")
                    else:
                        answer_given_t_or_f("true")
                else:
                    answer_given_t_or_f("true")
            else:
                answer_given_t_or_f("true")
        else:
            answer_given_t_or_f("true")
    else:
        answer_given_t_or_f("true")


# Main Routine
question_generator_and_answers_easy()
