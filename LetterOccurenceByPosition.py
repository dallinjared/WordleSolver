import json

file = open('Data/words.json')
data = json.load(file)

def getPercentage(portion, total):
    if portion <= 0 or total <= 0 :
        return 0.0
    else :
        return round(((float(portion)/total) * 100), 2)

def getOccurenceByPosition(wordList, fileName):
    
    alphabet = ["a", "b", "c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

    occurenceByPosition = {}

    for letter in alphabet:
        letterData = {}
        letters = [0,0,0,0,0]
        wordsContaining = 0
    
        for x in range(5):
            for s in wordList:
                if x == 0 and s != None and letter in s:
                    wordsContaining += 1

                if s[x] == letter:
                    letters[x] += 1

        totalOccurence = sum(letters)
        letterData.update(
            {
                'total': totalOccurence,
                'containedIn': wordsContaining,
                'appearancePercent': getPercentage(wordsContaining, len(wordList)),
                'occurrence' : {
                    '1': (letters[0]), 
                    '2': (letters[1]),
                    '3': (letters[2]),
                    '4': (letters[3]),
                    '5': (letters[4]),
                }
            }
        )
        occurenceByPosition.update({letter: letterData})

    with open('Data/'+ fileName + 'Occurence.json', 'w') as f:
        json.dump(occurenceByPosition, f)

getOccurenceByPosition(data['solutions'], "solutions")
getOccurenceByPosition(data['guesses'], "guesses")