import random

fruits = ("apple", "orange", "banana", "pineapple", "grape")
colours = ("white", "pink", "purple", "black", "green")
countries = ("India", "Switzerland", "America", "Pakistan", "China", "Russia")

categories = ("fruit", "colour", "country")
chosen_category = random.choice(categories)
if chosen_category == "fruit":
    answer = random.choice(fruits)
elif chosen_category == "colour":
    answer = random.choice(colours)
elif chosen_category == "country":
    answer = random.choice(countries)
else:
    pass

wrong_guesses = 0

hangman_art = { 0:  ("   ",
                     "   ",
                     "   "),
                1:  (" o ",
                     "   ",
                     "   "),
                2:  (" o ",
                     " | ",
                     "   "),
                3:  (" o ",
                     "/| ",
                     "   "),
                4:  (" o ",
                     "/|\\",
                     "   "),
                5:  (" o ",
                     "/|\\",
                     "/  "),
                6:  (" o ",
                     "/|\\",
                     "/ \\")
}


def display_man(man):
    for line in hangman_art[wrong_guesses]:
        print(line)



def display_hint(hint):
    print(" ".join(hint))



def display_answer(answer):
    print(" ".join(answer))



def hangman():
    
    hint = " " * len(answer)
    
    guessed_letters = set()
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Enter a letter: ").lower()

        if guess in answer:
            for i in range[len(answer)]:
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1

        if guess == guessed_letters:
            print(f"{guess} is already guessed")
            continue 

        guessed_letters.add(guess)

        if len(guess) != 1 or not guess.alpha():
            print("Invalid input")
            continue
        
        if " " not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print(f"Congrats you won, it took you {wrong_guesses} guesses")
            is_running = False
        elif wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            display_answer(answer)
            print(f"You lose, better luck next time")
            is_running = False


if __name__ == "__hangman__":
    hangman()
