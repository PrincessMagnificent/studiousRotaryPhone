import os, sys
from random import randint


location = "C:\\Users\\alexc\\Documents\\GitHub\\studiousRotaryPhone\\DictRANDOM"
os.chdir(location)


nounFile = open("nouns.txt","r")
adjFile = open("adjectives.txt", "r")
verbFile = open("verbs.txt", "r")

nounArrayThing = nounFile.readlines()
adjArrayThing = adjFile.readlines()
verbArrayThing = verbFile.readlines()

NOUNArrayLen = len(nounArrayThing)
ADJarrayLen = len(adjArrayThing)
VERBarrayLen = len(verbArrayThing)

randomADJ = adjArrayThing[randint(0,ADJarrayLen-1)]
randomVERB = verbArrayThing[randint(0,VERBarrayLen-1)]
randomNOUN = nounArrayThing[randint(0,NOUNArrayLen-1)]

print(randomVERB[:-1] + " the " + randomADJ[:-1] + " " + randomNOUN[:-1])

print("\nthere are " + str(NOUNArrayLen * ADJarrayLen) + " permutations")