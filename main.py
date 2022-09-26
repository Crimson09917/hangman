# Patrick Russell
# 20/05/2022
# Hangman

from random import randint
from string import ascii_lowercase

# Format file into array for python
def formatFile(fileName, minSize):
    file = open(fileName, "r")
    lines = []
    for line in file:
        line = "".join(list(line)[:-1]).lower()
        if len(line) >= minSize:
            lines.append(line)
    print(lines)
    return lines

dictionary = formatFile("famous.txt", 5)



while True:
    usedLetters = []

    # This is NOT displayed to the user
    word = dictionary[randint(0,len(dictionary))]

    # All the letters in the word
    wordArray = []
    for i in word:
        if i != "/":
            wordArray.append(i)

    # Creates the obscured string
    outputWord = ""
    outputArray = []
    for i in word:
        if i != " ":
            outputWord+= "-"
            outputArray.append("-")
        else:
            outputWord += "/"
            outputArray.append("/")

    # Checks the letter is a valid input
    def validateLetter(input):
        # alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        alphabet = list(ascii_lowercase)
        if len(input) != 1:
            return False 
        for i in alphabet:
            if i == input:
                return True
        return False


    # Returns a list of all the indexes featuring the input letter
    def checkLetter(word, input):
        indexes = []
        for i in range(len(word)):
            if input == word[i]:
                indexes.append(i)
        return indexes

    def checkComplete(array):
        for i in array:
            if i == "-":
                return False
        return True


    # print(f"word is: {word}")

    lives = 6
    while lives != 0:
        print(f"\n\nlives={lives}")
        print(outputWord)
        guess = input("\nGuess a letter: ").lower()
        if validateLetter(guess) == False:
            print("That is not a valid letter")
        else:
            used = False
            for i in usedLetters:
                if i == guess:
                    used = True
            if used == True:
                print("You've already used that letter")
            else:
                usedLetters.append(guess)
                indexes = checkLetter(wordArray, guess)
                if len(indexes) == 0:
                    lives -= 1
                    print("That isn't in the word")
                else:
                    for i in indexes:
                        outputArray[i] = guess
                    outputWord = ""
                    for i in outputArray:
                        if i != "/":
                            outputWord += i
                        else:
                            outputWord += "/"
                    
                    if checkComplete(outputArray) == True:
                        print(f"\n\nThe word is {word}")
                        print("You win!!")
                        break

    if lives == 0:
        print(f"Word is {word}")
        print('Fat L')
        print("That guy's been hanged now")
