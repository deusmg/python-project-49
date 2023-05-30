import prompt
ATTEMPTS = 3


def game_engine(game):
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print(game.RULE)
    for i in range(ATTEMPTS):
        question, right_answer = game.data_generate()
        print(f"Question: {question}")
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
