"""Program's base development - v5
This program contains the instructions and yes/no checker & the formatter &
the difficulty level question & maori numerals teaching program & quizzing the
numerals easy added with the quizzing numerals hard
Created by Elme Pieterse
17/05/2023
"""


# Functions:
# function to format text
def formatter(_symbol, _text):
    sides = _symbol * 3
    formatted_text = f"{sides} {_text} {sides}"
    top_bottom = _symbol * len(formatted_text)
    return f"{top_bottom}\n{formatted_text}\n{top_bottom}"


# number checker Function:
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


# yes/no checker function:
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


# instructions function:
def instructions():
    print(formatter("~", "Maori Numerals Quiz Instructions"))
    print()
    print("This program will quiz your knowledge on the Maori numbers 1 to 10")
    print("You will have a option at the start of the quiz to view/learn the "
          "maori numbers 1 to 10, if you choose")
    print()
    print(formatter("-", "Difficulty Level:"))
    print("There is option 1, which is for the beginners (Easy):")
    print("In this quiz the questions are true and false questions, giving you"
          " a 50% chance of being correct")
    print()
    print("OR there is option 2, for the experts (Hard):")
    print("In this quiz the question will say a maori number and you have to "
          "type the number it represents,\nresulting in you having a 10% "
          "chance of being correct")
    print()
    print(formatter("-", "Points System:"))
    print("Your total number of points will depend on the number of questions"
          " you get correct")
    print("You will gain 10 points for every answer that is correct")
    print("Or you will lose 5 points if the answer is incorrect")
    print()
    print("Let the quiz begin!")


# difficulty level checker function:
def difficulty_level_checker(question):
    error = "Please retry: Pick a numeral: 1 or 2"

    while True:
        try:
            # Ask what level difficulty
            difficulty_chosen = int(input(question))

            # Check if input is a valid numeral/difficulty
            if difficulty_chosen == 1 or difficulty_chosen == 2:
                return difficulty_chosen
            else:
                print(error)
        except ValueError:
            print(error)


# Viewing maori numerals function:
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


# Questions (Easy) function:
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

    return answer


# questions (hard) function:
def question_generator_and_checker_hard():
    import random
    MAORI_NUMERALS = ["tahi", "rua", "toru", "wha", "rima", "ono", "whitu",
                      "waru", "iwa", "tekau"]
    maori_numeral = random.choice(MAORI_NUMERALS)
    question = f"What number is {maori_numeral}? "
    answer_given = int(answer_checker_numbers(question))

    def answer_given_marked(number):
        if answer_given == number:
            print("Correct, Amazing job!")
        else:
            print("Sorry, keep trying, you can do it!")

    if maori_numeral == "tahi":
        answer_given_marked(1)
    elif maori_numeral == "rua":
        answer_given_marked(2)
    elif maori_numeral == "toru":
        answer_given_marked(3)
    elif maori_numeral == "wha":
        answer_given_marked(4)
    elif maori_numeral == "rima":
        answer_given_marked(5)
    elif maori_numeral == "ono":
        answer_given_marked(6)
    elif maori_numeral == "whitu":
        answer_given_marked(7)
    elif maori_numeral == "waru":
        answer_given_marked(8)
    elif maori_numeral == "iwa":
        answer_given_marked(9)
    elif maori_numeral == "tekau":
        answer_given_marked(10)
    else:
        answer_given_marked(13)


# Main Routine:
# Instructions:
view_instructions = yes_no_checker("Do you want to see the instructions? "
                                   "(Yes/No): ").lower()
if view_instructions == 'yes':
    instructions()
else:
    print()

# Difficulty Level questions:
difficulty_level = difficulty_level_checker("What level of difficulty do you"
                                            " want to choose: Easy(1) or "
                                            "Hard(2): ")
print(f"You entered the level {difficulty_level} difficulty")

# Maori numeral teaching
review_maori_numerals = yes_no_checker("Do you want to learn or revise the "
                                       "maori numerals? (Yes/No): ").lower()
if review_maori_numerals == "yes":
    maori_numerals()
else:
    print()

# The questions for each level of difficulty
for item in range(10):
    if difficulty_level == 1:
        question_generator_and_answers_easy()
    else:
        question_generator_and_checker_hard()
