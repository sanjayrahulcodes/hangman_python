#Hangman game using python
import random

words = ("director", "programmer", "hangman", "python", "computer", "science", "developer", "software")
hangman_animation = {
    0: ("     ",),
    1: ("   O ",),
    2: ("   O ", "   | "),
    3: ("   O ", "  /| "),
    4: ("   O ", "  /|\\"),
    5: ("   O ", "  /|\\", "  /  "),
    6: ("   O ", "  /|\\", "  / \\"),
}

def display_hangman(attempts):
    print("---------------")
    for line in hangman_animation[attempts]:
        print(line)
    print("---------------")

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(words)
    hint = len(answer) * ["_"]
    wrong_guesses = 0
    correct_guesses = set()
    is_running = True

    while is_running:
        print("Welcome to Hangman!")
        display_hangman(wrong_guesses)
        display_hint(hint)
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1
        if "_" not in hint:
            print("Congratulations! You've guessed the word:")
            display_answer(answer)
            is_running = False
        if wrong_guesses >= 6:
            print("Game over! The correct word was:")
            display_answer(answer)
            is_running = False

if __name__ == "__main__":
    main()  
    