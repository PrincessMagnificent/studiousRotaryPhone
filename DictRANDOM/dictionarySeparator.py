import os, sys

location = "C:\\Users\\alexc\\Documents\\GitHub\\studiousRotaryPhone\\DictRANDOM"
fileTarget = "OxfordEnglishDictionary.txt"

def cleanseInput(input):
    cleansed = "".join(symbol for symbol in input if symbol.isalpha())
    return cleansed

os.chdir(location)
fileListing = open(fileTarget, encoding="utf8")
##The file is encoded in UTF8 and will have charmaps map to <undefined> if you don't tell python this, because python assumes Latin-1
listOfWordTypes = ("v","n","adj")

nounFile = open("nouns.txt","w")
adjFile = open("adjectives.txt", "w")
verbFie = open("verbs.txt", "w")

for line in fileListing:
    if len(line) > 4:

        words = line.split();
        for x in words:
            if cleanseInput(x.lower()) in listOfWordTypes:
                myWordType = cleanseInput(x.lower())
                myWord = cleanseInput(words[0])
                if myWordType == "adj":
                    print("ADJRECTIVE")
                    adjFile.write(myWord)
                    adjFile.write("\n")
                elif myWordType == "v":
                    print("VERB")
                    verbFie.write(myWord)
                    verbFie.write("\n")
                elif myWordType == "n":
                    print("NOUN")
                    nounFile.write(myWord)
                    nounFile.write("\n")
                print(myWordType + " " + words[0])

nounFile.close()
adjFile.close()
verbFie.close()
fileListing.close()