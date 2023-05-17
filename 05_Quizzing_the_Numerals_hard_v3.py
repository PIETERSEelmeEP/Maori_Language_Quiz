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
    question = f"What number is {maori_numeral}? "
    error = "Please enter a whole number between 1 and ten: "

    def answer_checker(question_text):
        while True:
            try:

                # Input a question
                answer = int(input(question_text))

                # If user input 1 output will be 'checking if answer
                if answer == 1:
                    answer = 1
                    return answer

                # If user input 2 output will be 'checking if answer
                elif answer == 2:
                    answer = 2
                    return answer

                # If user input 3 output will be 'checking if answer
                elif answer == 3:
                    answer = 3
                    return answer

                # If user input 4 output will be 'checking if answer
                elif answer == 4:
                    answer = 4
                    return answer

                # If user input 5 output will be 'checking if answer
                elif answer == 5:
                    answer = 5
                    return answer

                # If user input 6 output will be 'checking if answer
                elif answer == 6:
                    answer = 6
                    return answer

                # If user input 7 output will be 'checking if answer
                elif answer == 7:
                    answer = 7
                    return answer

                # If user input 8 output will be 'checking if answer
                elif answer == 8:
                    answer = 8
                    return answer

                # If user input 9 output will be 'checking if answer
                elif answer == 9:
                    answer = 9
                    return answer

                # If user input 10 output will be 'checking if answer
                elif answer == 10:
                    answer = 10
                    return answer

                # Otherwise the required inputs will be displayed
                else:
                    print(error)
            except ValueError:
                print(error)

    answer_given = int(answer_checker(question))

    def answer_checker():
        if maori_numeral != "tahi":
            if maori_numeral != "rua":
                if maori_numeral != "toru":
                    if maori_numeral != "wha":
                        if maori_numeral != "rima":
                            if maori_numeral != "ono":
                                if maori_numeral != "whitu":
                                    if maori_numeral != "waru":
                                        if maori_numeral != "iwa":
                                            if maori_numeral == "tekau":
                                                if answer_given == 10:
                                                    print("Correct, Amazing "
                                                          "job!")
                                                else:
                                                    print("Sorry, keep trying,"
                                                          " you can do it!")
                                            else:
                                                print()
                                        else:
                                            if answer_given != 9:
                                                print(
                                                    "Sorry, keep trying, you "
                                                    "can do it!")
                                            else:
                                                print("Correct, Amazing job!")
                                    else:
                                        if answer_given != 8:
                                            print(
                                                "Sorry, keep trying, you can "
                                                "do it!")
                                        else:
                                            print("Correct, Amazing job!")
                                else:
                                    if answer_given != 7:
                                        print(
                                            "Sorry, keep trying, you can do "
                                            "it!")
                                    else:
                                        print("Correct, Amazing job!")
                            else:
                                if answer_given != 6:
                                    print("Sorry, keep trying, you can do it!")
                                else:
                                    print("Correct, Amazing job!")
                        else:
                            if answer_given != 5:
                                print("Sorry, keep trying, you can do it!")
                            else:
                                print("Correct, Amazing job!")
                    else:
                        if answer_given != 4:
                            print("Sorry, keep trying, you can do it!")
                        else:
                            print("Correct, Amazing job!")
                else:
                    if answer_given != 3:
                        print("Sorry, keep trying, you can do it!")
                    else:
                        print("Correct, Amazing job!")
            else:
                if answer_given != 2:
                    print("Sorry, keep trying, you can do it!")
                else:
                    print("Correct, Amazing job!")
        else:
            if answer_given != 1:
                print("Sorry, keep trying, you can do it!")
            else:
                print("Correct, Amazing job!")

    answer_checker()
    return answer_given


# Main Routine
question_generator_and_checker_hard()
