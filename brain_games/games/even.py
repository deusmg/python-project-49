from random import randint
RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def generate_data():
    question = randint(1, 100)
    right_answer = "yes" if is_even(question) else "no"
    return question, right_answer
