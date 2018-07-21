import json
from difflib import get_close_matches

data = json.load(open("076 data.json"))

def translate(word):
    if word in data :
        return data[word]
    elif word.title() in data :
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys(),cutoff=0.8)) > 0 :

        yn = input("Did you mean {} instead? If Yes Enter Y otherwise N ".format( get_close_matches(word,data.keys(),cutoff=0.8)[0]))
        if yn.lower() == 'y':
            return data[get_close_matches(word,data.keys(),cutoff=0.8)[0]]
        elif yn.lower() == 'n':
            return 'The word does not exits in dictionary. Please recheck it'
        else:
            return "We didn't understand your input"
    else:
        return "The word does not exits in dictionary data. Please recheck it"
while True :
    word = input("Enter word: ")
    print()
    ctr = 0
    s = translate(word.lower())
    if type(s)== list:
        for i in s:
            ctr+=1
            print("Defination",ctr,':',i)
        print()
    else:
        print('\t',s)
    y = input("Do you want to search again? if yes enter Y otherwise N :")
    if y.lower() == 'y':
        continue
    elif y.lower() == 'n':
        break
    else:
        print('You Fool Just type what the program has asked. I Quit')
        break