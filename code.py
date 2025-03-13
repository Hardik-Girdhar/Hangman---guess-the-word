import getpass # to generate encrypted word so that other can not see

lives = 10
word = getpass.getpass("Player 1 will enter a word to guess: ").lower()
listword = list(word)

i=0
print(f"Your main word contain {len(word)} letter")
hint = "An ___ a day keeps the doctor away."
print(hint)
while(i!=len(word)):
    if lives == 0 :
        break
    letter = input("Guess the letter:")
    if(letter == listword[i]):
        print(f"You guessed the write word {letter} now guess next word")
        i += 1
    else:
        lives -= 1
        print(f"oh.. wrong! You lost your one life left with {lives} lives")
    
if lives == 0 :
    print(f"Hey you lost the game😢 the word was {word}")
else:
    print(f"Hey you won the game with {lives} lives😎")
