##the purpose of all of this is to help me identify what is a verb, a noun or an adjective in a dictionary file

import sys

#command line argumnts
args = sys.argv

#list of word types, either verbs nouns or adjectives
listOfWordTypes = ("v","n","adj")

#this is how we make "v, --v and .v" all the same
for argument in args:
    cleansed = "".join(symbol for symbol in argument if symbol.isalnum())
    print(cleansed)

fillll = open("testFile","w")
fillll.write("Aadrer\n")
##turns out it doesn't insert \n
fillll.write("a second line")