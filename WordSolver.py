import json

file = open('Data/words.json')
data = json.load(file)

def filterByIncorrectLetters(incorrect, wordlist):
    reducedWordlist = wordlist
    for letter in incorrect:
        x = 0
        while x <= len(reducedWordlist)-1:
            if letter in reducedWordlist[x]:
                reducedWordlist.remove(reducedWordlist[x])
            else:
                x += 1
    return reducedWordlist

def filterByOutOfPlaceLetters(outOfPlace, wordlist):
    reducedWordlist = wordlist
    for letter, positions in outOfPlace.items():
        for position in positions:
            x = 0
            while x <= len(reducedWordlist)-1:
                if reducedWordlist[x][position] == letter or letter not in reducedWordlist[x]:
                    reducedWordlist.remove(reducedWordlist[x])
                else:
                    x += 1
    return reducedWordlist

def filterByCorrectLetters(correct, wordlist):
    reducedWordlist = wordlist
    for letter, positions in correct.items():
        for position in positions:
            x = 0
            while x <= len(reducedWordlist)-1:
                if reducedWordlist[x][position] != letter:
                    reducedWordlist.remove(reducedWordlist[x])
                else:
                    x += 1
    return reducedWordlist

def startWordSolver(correct={}, outOfPlace={}, incorrect=[]):
    possibleAnswers = data['solutions']
    if len(incorrect) != 0:
        possibleAnswers = filterByIncorrectLetters(incorrect=incorrect, wordlist=possibleAnswers)
    if len(outOfPlace) != 0:
        possibleAnswers = filterByOutOfPlaceLetters(outOfPlace=outOfPlace, wordlist=possibleAnswers)
    if len(correct) != 0:
        possibleAnswers = filterByCorrectLetters(correct=correct, wordlist=possibleAnswers)
    return possibleAnswers

query = startWordSolver(correct={'o':[1], 't':[3]}, outOfPlace={'o':[2]}, incorrect=['u', 'l','i','p','d','e','a','h','b','y'])

print(query)
print(len(query))
