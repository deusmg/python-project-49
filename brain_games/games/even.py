from random import randint
RULE = 'Answer "yes" if the number is even, otherwise answer "no".'
NUMBER_MIN = 1
NUMBER_MAX = 100


def is_even(number):
    return number % 2 == 0


def generate_data():
    question = randint(NUMBER_MIN, NUMBER_MAX)
    right_answer = "yes" if is_even(question) else "no"
    return question, right_answer
