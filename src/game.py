# src/game.py
def score_guess(the_target, the_guess):
    position = 0
    symbol = ""
    for letter in the_guess:
        if letter == the_target[position]:
            symbol += "+ "
        elif letter in the_target:
            symbol += "? "
        else:
            symbol += "_ "
        position += 1
    print(*the_guess.upper())
    print(symbol)
    return symbol == "+ + + + + "
