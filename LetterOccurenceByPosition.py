import json

file = open('Data/words.json')
data = json.load(file)

def getPercentage(position, total):
    return round(((position/total) * 100), 2)

def getOccurenceByPosition(wordList, fileName):
    #For each Letter in alphabet
    #from 0-4 (1-5) check string at index for that letter
    #sum count and append to dictionary for that letter with the key being the letter
    #occurenceByPosition = ["y": {'totalOccurence': 425, 'letter1': 25, 'letter2': 75, 'letter3': 25, 'letter4': 25, 'letter5': 275}]
    alphabet = ["a", "b", "c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

    occurenceByPosition = {}

    for letter in alphabet:
        letterData = {}
        letters = [0,0,0,0,0]
    
        for x in range(5):
            for s in wordList:
                if s[x] == letter:
                    letters[x] += 1

        totalOccurence = sum(letters)
        letterData.update(
            {
                'total': totalOccurence, 
                '1': getPercentage(letters[0], totalOccurence), 
                '2': getPercentage(letters[1], totalOccurence),
                '3': getPercentage(letters[2], totalOccurence),
                '4': getPercentage(letters[3], totalOccurence),
                '5': getPercentage(letters[4], totalOccurence),
            }
        )
        occurenceByPosition.update({letter: letterData})

    with open('Data/'+ fileName + 'Occurence.json', 'w') as f:
        json.dump(occurenceByPosition, f)

getOccurenceByPosition(data['solutions'], "solutions")
getOccurenceByPosition(data['guesses'], "guesses")