from random import randint
RULE = "Find the greatest common divisor of given numbers."


def data_generate():
    first_number = randint(1, 101)
    second_number = randint(1, 101)
    question = f"{first_number} {second_number}"
    right_answer = 1
    for i in range(1, min(first_number, second_number) + 1):
        if first_number % i == 0 and second_number % i == 0:
            divisor = i
            if divisor > right_answer:
                right_answer = divisor
    return question, str(right_answer)
