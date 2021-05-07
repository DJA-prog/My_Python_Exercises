import hangmanwordbank
import random
guessed_word =""
life = 6
guessed_word = []
guessed_done = []

word_guess = hangmanwordbank.words[random.randint(0, len(hangmanwordbank.words)-1)] # generate random word from list
word_len = len(word_guess)
word_done = len(word_guess)

for a in range(word_len):
    guessed_word.append("_") # fill in blanks

print(f"Letter count {word_len}")

while life > 0:
    guess = input("Your quess: ").lower()
    if (guessed_done.count(guess) > 0): # filters used letters
        print("letter used")

    elif (word_guess.count(guess) == 0): # if letter is not in the word
        life -= 1
        print(hangmanwordbank.HANGMANPICS[6 - life])

    elif (word_guess.count(guess) > 0): # if letter is in the word
        for i in range(word_len):
            if word_guess[i] == guess:
                guessed_word.pop(i) # remove place holder
                guessed_word.insert(i, guess) # insert letter where place holder
                word_done -= 1
    else:
        print("Char not allowed") # error handler

    guessed_done.append(guess) # add to used letter list

    word_fin = ""
    for b in guessed_word:
        word_fin += b
    print(word_fin)

    if (word_done == 0):
        print("You Won")
        break

print("Game over")
