import getpass # to generate encrypted word so that other can not see

lives = 10
word = getpass.getpass("Player 1 will enter a word to guess: ").lower()
listword = list(word)
final = ["_"]*len(listword)
print(final)

i=0
print(f"Your main word contain {len(word)} letter")
while(i!=len(word)):
    if lives == 0 :
        break
    letter = input("Guess the letter:")
    if(letter == listword[i]):
        print(f"You guessed the write word {letter} now guess next word")
        final[i] = letter
        print(final)
        i += 1
    else:
        lives -= 1
        print(f"oh.. wrong! You lost your one life left with {lives} lives")
        print(f"{letter} is incorrect word")
        print(final)
    
if lives == 0 :
    print(f"Hey you lost the game😢 the word was {word}")
else:
    print(f"Hey you won the game with {lives} lives😎")
