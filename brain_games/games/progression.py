from random import randint
RULE = "What number is missing in the progression?"


def data_generate():
    start = randint(0, 100)
    step = randint(1, 11)
    stop = start + step * 10
    nums = list(range(start, stop, step))
    point = randint(0, 8)
    right_answer = f'{nums[point]}'
    nums[point] = '..'
    question = ' '.join(map(str, nums))
    return question, right_answer
