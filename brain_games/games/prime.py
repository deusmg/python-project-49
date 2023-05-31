from random import randint
RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def data_generate():
    question = randint(2, 101)
    count = 0
    for i in range(2, question):
        if question % i == 0:
            count += 1
    if count == 0:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return question, right_answer
