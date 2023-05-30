from random import randint
import prompt
ATTEMPTS = 3
RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def data_generate():
    number = randint(1, 100)
    if number % 2 == 0:
        right_answer = "yes"
    elif number % 2 != 0:
        right_answer = "no"
    return number, right_answer

def even():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print(RULE)
    for i in range(ATTEMPTS):
        number, right_answer = data_generate()
        print(f"Question: {number}")
        answer = prompt.string("Your answer: ")
        if right_answer == answer:
            print("Correct")
        else:
            print(
                f"'{answer}'is wrong anser ;(."
                f"Corrcet answer was '{right_answer}'."
                )
            print(f"Let's try again, {name}!")
            break
    else:
        print(f"Congratulations, {name}!")