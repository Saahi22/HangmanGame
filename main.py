# Hangman Game
# Written by: Saahi
import random

# Global Variables
# Lists containing words that will be randomly selected to be used
makeupList = ['SEPHORA', 'EYELASHES', 'MASCARA', 'LASH GLUE', 'EYE SHADOW', 'LIP STICK', 'FOUNDATION',
              'LIP GLOSS']
racingList = ['FORMULA ONE', 'NASCAR', 'DRAG REDUCTION SYSTEM', 'FERRARI', 'RED BULL', 'MERCEDES', 'ASTON MARTIN',
              'MCLAREN']
listOfLetters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I','J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' ]


# PrintCategories()
# Is a function that will automatically print the categories to the screen when called upon
def printCategories():
    print('Here are the following topics you can choose:')
    optionA = '\tPress (A) For Words Related To: Makeup'
    optionB = '\tPress (B) Words Related To: Racing'
    print(optionA + "\n" + optionB)


# ProcessInput(string selection)
# Takes the topic selection made by the user and identified which topic they wish to use
def ProcessInput(selection):
    if (selection == 'A') | (selection == 'a'):
        print('You Selected Makeup Related Words\n\nYour Game Is Loading...')
        return makeupList
    elif (selection == 'B') | (selection == 'b'):
        print('You Selected Racing Related Words\n\nYour Game Is Loading...')
        return racingList


def listOptions(choice, listOfLetters):
    print(listOfLetters)


# RunHangMan()
# The Function that Handles the Running of the entire game
def RunHangMan():
    printCategories()
    userSelection = input('Please Select One Of The Above Options: ')
    listOfWords = ProcessInput(userSelection)

    wordSelection = random.randint(0, 7)
    displayGame(wordSelection, listOfWords)


# def removeOptions(selected, listOfLetters):
#     listOfLetters.remove(selected)
#     # print(listOfLetters)

# def selectOption(listOfLetters):
#     selected = input("Please Enter A Capital Letter Out Of The Remaining Options: ")
#     # removeOptions(selected, listOfLetters)
#     # print(selected)


def displayGame(wordnum, wordlist):
    word = wordlist[wordnum]
    # print(word)
    dashes = ""
    wordlen = len(word)
    for x in range(len(word)):
        if word[x] == " ":
            dashes += ' '
        else:
            dashes += "_"
    print("There are " + str(wordlen) + " Characters Including Any Spaces: " + dashes)
    listOptions("", listOfLetters)

    inputs = ""
    dashesList = []
    char_list = [char for char in word]
    # print(char_list)
    firstTime = 0
    while inputs != "exit":
        if firstTime == 0:
            # print("ENTERING")
            for char in word:
                if char == " ":
                    dashesList.append(" ")
                else:
                    dashesList.append("_")
            firstTime = firstTime + 1
            print(firstTime)
        # new_list = [new_value if x == old_value else x for x in original_list]
        inputs = input("Enter a letter: ")
        for i in range(len(char_list)):
            if char_list[i] == inputs:
                dashesList[i] = char_list[i]
                print(dashesList)



        if dashesList == char_list:
            print("Good Job, Thank you for playing")
            inputs = input("Enter (exit) To End The Game: ")


# Main
if __name__ == '__main__':
    print('Welcome to Hangman\n')

    RunHangMan()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
