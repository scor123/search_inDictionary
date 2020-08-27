"""
this script for searching for a word in pre-built file "data.json" and this file contains the eaning of words and you input a word and the program return its definition
ideas about developing this script is building web app where users enter the world and instead of using a file json fil here maybe searching different website and 
scraping the definition
"""



import json
from difflib import get_close_matches

data = json.load(open("076 data.json"))


def translate(word):
    if word in data:
        return data[word]
    else:
        word=word.lower()
        if word in data:
            return data["word"]
        elif len(get_close_matches(word, data.keys())) > 0:
            yn = input("Did you mean {} instead? enter Y if yes and N if no".format(get_close_matches(word, data.keys())[0]))
            if yn == "Y":
                return data[get_close_matches(word, data.keys())[0]]
            elif yn == "N":
                return "Please double check your "
            else:
                return "Sorry we don't uderstand your query "


        else:
            return "This word is not available now in our dectionry help us and at it from here!"


word = input("Enter word: ")
output = translate(word)
if type(output) == list:

    for sentence in output:
        print(sentence)
else:
    print(output)



