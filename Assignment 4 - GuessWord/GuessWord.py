"""
@author: Adeildo Vieira Silva Neto (av259)
"""

import random


def handleUserInputDifficulty():
    """
This function prompts the user to select the difficulty level of the game,
either "h" for hard or "e" for easy. Based on the user's selection,
the function returns the number of allowed misses for the game.
In case of hard mode it would return a lower number of allowed misses and for
easy mode, it would return a higher number.
    """

    print("You have two options for missing. Hard has 8 and Easy has 12.")
    x = input("(h)ard or (e)asy> ")
    if x == "h":
        return 8
    else:
        return 12


def getWord(words, length):
    """
    It selects a secret word that the user must guess. This is done by randomly
    selection of a word from the words that is of length "length" (lenght n).
    """

    AWords = [w for w in words if len(w) == length]
    randomInt = random.randint(0, len(AWords) - 1)
    secretWord = AWords[randomInt]
    return secretWord


def createDisplayString(lettersGuessed, missesLeft, guessedWordAsList):
    """
    Creates the string that will be displayed to the user, using the information
    in the parameters.
    """

    lettersGuessed.sort()
    displayString = "letters you've guessed: " + " ".join(lettersGuessed) + "\n"
    displayString += "misses remaining = " + str(missesLeft) + "\n"
    displayString += " ".join(guessedWordAsList)
    return displayString


def handleUserInputLetterGuess(lettersGuessed, displayString):
    """
    It prints displayString, asking the user to input a letter to
    guess. This function handles the user input of the new letter guessed
    and can check if it is a repeated letter.
    """

    print(displayString)
    x = input("letter> ")
    while x in lettersGuessed:
        print("Oh! You almost guessed that")
        x = input("letter> ")
    return x


def updateGuessedWordAsList(thereisguessedLetter, secretWord,
                            guessedWordAsList):
    """
    It updates guessedWordAsList according to whether guessedLetter is in
    secretWord and where in secretWord guessedLetter is in.
    """

    if thereisguessedLetter in secretWord:
        guessedLetterIndexes = []
        listSecretWord = list(secretWord)
        for x in range(len(listSecretWord)):
            if listSecretWord[x] == thereisguessedLetter:
                guessedLetterIndexes.append(x)
        for dex in guessedLetterIndexes:
            guessedWordAsList[dex] = thereisguessedLetter
        return guessedWordAsList
    else:
        return guessedWordAsList


def processUserGuess(guessedLetter, secretWord, guessedWordAsList, missesLeft):
    """
    It uses the information in the parameters to update the user's progress
    in the GuessWord game.
    """

    NewguessedWordAsList = updateGuessedWordAsList(guessedLetter, secretWord,
                                                   guessedWordAsList)
    if guessedLetter not in secretWord:
        updatedMissesLeft = missesLeft - 1
        indexTwoBool = False
    else:
        updatedMissesLeft = missesLeft
        indexTwoBool = True

    list = [NewguessedWordAsList, updatedMissesLeft, indexTwoBool]
    return list


def runGame(filename):
    """
    This function sets up the game, runs each round, and prints a final
    message on whether the user won.
    True is returned if the user won the game.
    If the user lost the game, False is returned.
    """

    f = open(filename)
    wordsList = [w.strip() for w in f.read().split()]

    missesTotal = handleUserInputDifficulty()
    print("you have " + str(missesTotal) + " misses to guess word.")
    missesLeft = missesTotal

    length = random.randint(5, 10)
    secretWord = getWord(wordsList, length)

    guessedWordAsList = []
    for x in range(length):
        guessedWordAsList.append("_")
    lettersGuessed = []

    while missesLeft > 0 and "_" in guessedWordAsList:

        displayString = createDisplayString(lettersGuessed, missesLeft,
                                            guessedWordAsList)
        guessedLetter = handleUserInputLetterGuess(lettersGuessed,
                                                   displayString)
        lettersGuessed.append(guessedLetter)
        guessedWordAsList = \
            processUserGuess(guessedLetter, secretWord, guessedWordAsList,
                             missesLeft)[0]
        missesLeft = \
            processUserGuess(guessedLetter, secretWord, guessedWordAsList,
                             missesLeft)[1]
        if not processUserGuess(guessedLetter, secretWord, guessedWordAsList,
                                missesLeft)[
            -1]:
            print("you missed: " + guessedLetter + " is not in word. You"
                                                   "better try again :P.")

    guessesMade = len(lettersGuessed)
    missesMade = missesTotal - missesLeft

    if "_" not in guessedWordAsList:
        won = True
        print("Hey, you guessed the word: " + secretWord)
        print("you made " + str(guessesMade) + " guesses with " + str(
            missesMade) + " misses :P")

    else:
        won = False
        print("Yay!" + "\n" + "word is " + secretWord)
        print("you've made " + str(guessesMade) + " guesses with " + str(
            missesMade) + " misses :(")

    return won


if __name__ == "__main__":
    """
    Runs the game with the file provided, called lowerwords.txt.
    """
    runGame('lowerwords.txt')
