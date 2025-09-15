from utils import load_words
from game import score_guess
import random


def main():
    TARGET_WORDS = './word_bank/target_words.txt'
    VALID_WORDS = './word_bank/all_words.txt'

    target_words_list = load_words(TARGET_WORDS)
    word_list = load_words(VALID_WORDS)

    target = random.choice(target_words_list)

    players_name = input("Dear player, what is your name? \n").upper() or "Mysterious player"

    print(f"Hi {players_name}, you have 6 chances to guess a five-letter word...")

    guesses = 0
    guessed_correctly = False

    while guesses < 6 and not guessed_correctly:
        guess = input("Enter a word: ").lower()
        while guess not in word_list:
            guess = input(f"{players_name}, try again: ").lower()
        guesses += 1
        guessed_correctly = score_guess(target, guess)
        print(f"{players_name}, you have used {guesses} guess(es)\n")

    print(f"{players_name}, congratulations!" if guessed_correctly else f"The correct word is {target}")

    guessed_status = "successful" if guessed_correctly else "unsuccessful"
    with open("game_history.txt", "a") as file_history:
        file_history.write(f"{players_name}, {target}, {guesses}, {guessed_status}\n")


if __name__ == "__main__":
    main()
