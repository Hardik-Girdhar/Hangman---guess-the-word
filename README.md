# Hangman Game Description
This Python script implements a simple Hangman game where the player has to guess the letters of a given word. The game starts with 10 lives. The word to guess is "apple," converted to lowercase. The player is prompted to guess each letter in sequence. If the guessed letter is correct, the player moves on to the next letter. If the guess is incorrect, the player loses a life. The game continues until the player either guesses all the letters correctly or runs out of lives. The script provides feedback on the player's progress and remaining lives.

### Importing getpass
The getpass module is used to securely input the word without displaying it on the screen.

### Setting Initial Variables
**lives**: The number of attempts the player has to guess the word (initially set to 10).

**word**: The word to be guessed, entered by Player 1 and converted to lowercase.

**listword**: A list of characters in the word.

**final**: A string to store the correctly guessed letters.

**i**: An index to track the position of the current letter being guessed.


### Game Loop
> The game informs the player of the number of letters in the word.

> The player guesses letters one by one.

> If the guessed letter matches the current letter in the word, it is added to the final string, and the player is prompted to guess the next letter.

> If the guessed letter is incorrect, the player loses a life.

> The loop continues until the player either guesses the entire word or runs out of lives.


### End of Game
> If the player runs out of lives, a message is displayed indicating they lost and revealing the word.

> If the player guesses the word correctly, a congratulatory message is displayed along with the remaining lives.
