import json

file = open('Data/words.json')
data = json.load(file)

def getPercentage(position, total):
    if position <= 0 or total <= 0 :
        return 0.0
    else :
        return round(((float(position)/total) * 100), 2)

def getOccurenceByPosition(wordList, fileName):
    
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