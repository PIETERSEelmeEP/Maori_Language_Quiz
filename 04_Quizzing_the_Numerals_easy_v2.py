"""Program quizzing the user of Maori Numerals (True or False quiz) - v2
This will generate a random maori numeral and a random number
between one & ten, all in a random order
Created by Elme Pieterse
10/05/2023
"""

import random

MAORI_NUMERALS = ["tahi", "rua", "toru", "wha", "rima", "ono", "whitu",
                  "waru", "iwa", "tekau"]
NUMBERS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for item in range(20):
    maori_numeral = random.choice(MAORI_NUMERALS)
    number = random.choice(NUMBERS)
    print(f"Does {maori_numeral} mean {number}?")
