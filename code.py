import getpass # to generate encrypted word so that others cannot see

lives = 10
word = getpass.getpass("Player 1 will enter a word to guess: ").lower()
listword = list(word)
final = ["_"] * len(listword)
print(final)

i = 0
print(f"Your main word co<ains {len(word)} letters")
while i < len(word):
    if lives == 0:
        break
    letter = input("Guess the letter: ").lower()
    if letter == listword[i]:
        final[i] = letter
        print(f"You guessed the right word {letter}.")
        print(f"You have {len(listword) - 1 - i} letters left to guess.")
        print(final)
        i += 1
        if i == len(word):  # Check if the game is won
            break
    else:
        lives -= 1
        print("Oh.. wrong!")
        print(f"{letter} is an incorrect word.")
        print(f"Left with {lives} lives.")
        print(final)

if lives == 0:
    print(f"Hey, you lost the game 😢 The word was {word}")
else:
    print(f"Hey, you won the game with {lives} lives left 😎")
