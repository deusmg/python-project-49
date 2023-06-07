from random import randint
RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def generate_data():
    question = randint(2, 101)
    right_answer = 'yes' if is_prime(question) else 'no'
    return question, right_answer
