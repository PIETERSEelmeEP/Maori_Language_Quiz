"""Program quizzing the user of Maori Numerals - v2
The question generator and its answer checker, to ensure a valid input is
entered
Created by Elme Pieterse
15/05/2023
"""


# functions:
# number answer checker function:
def answer_checker_numbers(question_text):
    error = "Please enter a whole number between 1 and ten: "
    while True:
        try:

            # Input a question
            answer = int(input(question_text))

            # If user input 1 output will be 'checking if answer is correct
            if answer == 1:
                answer = 1
                return answer

            # If user input 2 output will be 'checking if answer is correct
            elif answer == 2:
                answer = 2
                return answer

            # If user input 3 output will be 'checking if answer is correct
            elif answer == 3:
                answer = 3
                return answer

            # If user input 4 output will be 'checking if answer is correct
            elif answer == 4:
                answer = 4
                return answer

            # If user input 5 output will be 'checking if answer is correct
            elif answer == 5:
                answer = 5
                return answer

            # If user input 6 output will be 'checking if answer is correct
            elif answer == 6:
                answer = 6
                return answer

            # If user input 7 output will be 'checking if answer is correct
            elif answer == 7:
                answer = 7
                return answer

            # If user input 8 output will be 'checking if answer is correct
            elif answer == 8:
                answer = 8
                return answer

            # If user input 9 output will be 'checking if answer is correct
            elif answer == 9:
                answer = 9
                return answer

            # If user input 10 output will be 'checking if answer is correct
            elif answer == 10:
                answer = 10
                return answer

            # Otherwise the required inputs will be displayed
            else:
                print(error)
        except ValueError:
            print(error)


# question generator (hard) function:
def question_generator_and_checker_hard():
    import random
    MAORI_NUMERALS = ["tahi", "rua", "toru", "wha", "rima", "ono", "whitu",
                      "waru", "iwa", "tekau"]
    maori_numeral = random.choice(MAORI_NUMERALS)
    question = f"What number is {maori_numeral}? "
    answer_given = int(answer_checker_numbers(question))
    print("Checking if answer is correct.......")
    return answer_given


# Main Routine
question_generator_and_checker_hard()
