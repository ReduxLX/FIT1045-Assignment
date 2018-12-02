import random
import string
wordDictionary = {
    1: "READ",2: "WRITE",3: "LONG",4: "POST",5:"YEARN",6:"TELL",7:"WITHER",8:"WORK",9:"INVADE",10:"HEART",11:"SOOTHE"
}
wordList = ["READ","WRITE","LONG","POST","YEARN","TELL","WITHER","WORK","INVADE","HEART","SOOTHE"]

def generateBlock():
    block = []
    numberOfRows, numberOfColumns = 10,20
    alreadyChosenWords = []  # Stores already chosen words
    for row in range(numberOfRows):
        # Generates a random number to use as a key for the wordDictionary
        chosenWord = wordDictionary[random.randint(1,len(wordDictionary))]
        # Ensures no previously chosen word is rechosen
        while chosenWord in alreadyChosenWords:
            chosenWord = wordDictionary[random.randint(1, len(wordDictionary))]
        alreadyChosenWords.append(chosenWord)
        # Generates the starting row index of the chosen word based on word length (so it doesn't overflow)
        insertStart = random.randint(0,((numberOfColumns-1)-len(chosenWord)))
        rowCount = 0
        rowBlock = ""
        for column in range(numberOfColumns):
            rowBlock += (random.choice(string.ascii_uppercase))
            rowCount += 1
            if column == insertStart:
                rowBlock += chosenWord
                # After inserting the chosen word at the generated row index, fill the rest of the row with random letters then break
                for remaining in range(numberOfColumns-rowCount-len(chosenWord)):
                    rowBlock += (random.choice(string.ascii_uppercase))
                break
        block.append(rowBlock)
    return block

def displayBlock(block):
    for rowBlock in block:
        print(rowBlock)
# IMPORTANT: I HAVE NOT IMPLEMENTED EXTENSIVE ERROR CATCHING
# PLEASE DON"T ENTER ANY WEIRD/INVALID VALUES OR ELSE IT WILL CAUSE A RUNTIME ERROR
def mainActivity(block):
    score = 0
    # Makes a copy of the original word List
    wordListCopy = wordList[:]
    displayBlock(block)
    print("FIND ",wordListCopy)
    # Loops until the copy of the word list is empty
    while(len(wordListCopy)>0):
        try:
            rowNumber = int(input("Enter Row Number[0-9]: "))
        except:
            print("Invalid Row Number")
            break
        userChosenRow = block[rowNumber]
        # Display the selected row (with numberings for user aid)
        print("\n"+"          1111111111\n""01234567890123456789\n"+userChosenRow)
        startIndex = int(input("Enter String Start Index: "))
        endIndex = int(input("Enter String End Index: "))
        # Uses user inputs to find the word in string via String Indexing
        userChosenWord = userChosenRow[startIndex:endIndex]
        if userChosenWord in wordListCopy:
            print("Valid Word Found\n")
            # Ensures user can't pick the same word again
            wordListCopy.remove(userChosenWord)
            displayBlock(block)
            print("FIND ", wordListCopy)
            score += len(userChosenWord)
        else:
            print("Word Not Found, try again\n")
            displayBlock(block)
            print("FIND ", wordListCopy)
    # word list empty, all words found so return the final score
    return score

print("Welcome to the word search game!")
print("In this game you will be given a list of words to find")
print("You will have to use proper String formatting syntax to find the words \nGOOD LUCK!")
startGame = input("Start Game?(Y/N)")
while startGame != "Y" and startGame != "N":
    startGame = input("Start Game?(Y/N): ")
if startGame == "Y":
    print("")
    thisGameBlock = generateBlock()
    finalscore = mainActivity(thisGameBlock)
    print("This is the end of the Word Search game, your final score is",finalscore)
else:
    print("Nice")