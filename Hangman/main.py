import random

def randomWord(genre):
    if genre == "colours":
        f = open("colours.txt", "r")
        words = f.readlines()
        myWord = random.choice(words)
        return myWord

    elif genre == "animals":
        f = open("animals.txt", "r")
        words = f.readlines()
        myWord = random.choice(words)
        return myWord

    elif genre == "countries":
        f = open("countries.txt", "r")
        words = f.readlines()
        myWord = random.choice(words)
        return myWord

    else:
        print("You have entered the genres wrong... Make sure you have spelled it correctly! ")

def hangmanScaffhold(guesses, randomWord):
    if guesses == 0:
        print("""
 _________
|	 |
|
|
|
|
|_________
""")
    elif guesses == 1:
        print("""
 _________
|	 |
|	 O
|
|
|
|_________
""")
    elif guesses == 2:
        print("""
 _________
|	 |
|	 O
|	 |
|	 |
|
|_________
""")
    elif guesses == 3:
        print("""
 _________
|	 |
|	 O
|	\|
|	 |
|
|_________
""")
    elif guesses == 4:
        print("""
 _________
|	 |
|	 O
|	\|/
|	 |
|
|_________
""")
    elif guesses == 5:
        print("""
 _________
|	 |
|	 O
|	\|/
|	 |
|       /
|_________
""")
    elif guesses == 6:
        print("""
 _________
|	 |
|	 O
|	\|/
|	 |
|       / \\
|_________
""")
        print("The word was {}".format(randomWord))

def main():
    print("WELCOME TO HANGMAN")
    print("Choose a genre (please type in lower case)")
    print("colours")
    print("countries")
    print("animals")
    genre = input("Your choice:")

    word = randomWord(genre)
    wordList = list(word)
    blanks = "_"*len(word)
    blanksList = list(blanks)
    anotherBlanksList = list(blanks)
    guessList = []
    guesses = 0

    print("Lets play hangman!")
    hangmanScaffhold(guesses, word)
    print("" + ' '.join(blanksList))

    while guesses < 6:
        
        guess = input(">>> ")
        guess = guess.lower()

        if guess == "":
            print("You didn't enter any letter, please enter 1 letter at a time.")
        elif guess in guessList:
            print("You have already guessed that letter!!")
            print("Try Again.")
            print(' '.join(guessList))
        if len(guess) > 1:
            print("You have typed more than 1 letter. only type 1 please")
        else:
            guessList.append(guess)
            i = 0
            while i < len(word):
                if guess == word[i]:
                    anotherBlanksList[i] = wordList[i]
                i = i + 1
            
            if anotherBlanksList == blanksList:
                print("your guess is incorrect")
                guesses = guesses + 1
                hangmanScaffhold(guesses, word)
                print("You have ", guesses, "/ 6 guesses left.")

                if guesses < 6:
                    print("Guess again")
                    print(' '.join(blanksList))

            elif wordList != blanksList:
                blanksList = anotherBlanksList[:]
                print(' '.join(blanksList))

                if wordList == blanksList:
                    print("You win!")
                    print("WELL DONE - THANKS FOR PLAYING")

main()