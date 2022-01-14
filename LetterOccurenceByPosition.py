import json

file = open('Data/words.json')
data = json.load(file)

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
        letterData.update({'total': totalOccurence, '1': letters[0], '2': letters[1], '3': letters[2], '4': letters[3], '5': letters[4]})
        occurenceByPosition.update({letter: letterData})

    with open('Data/'+ fileName + 'Occurence.json', 'w') as f:
        json.dump(occurenceByPosition, f)

getOccurenceByPosition(data['solutions'], "solutions")
getOccurenceByPosition(data['guesses'], "guesses")