import os, sys

location = "C:\\Users\\alexc\\Documents\\GitHub\\studiousRotaryPhone"
fileTarget = "fileMessing.txt"

os.chdir(location)
fileListing = open(fileTarget, "w")

StringOne = "martyrs are believers"
StringTwo = "a mass murder in WACO"

fileListing.write(StringOne)
fileListing.write("\n")
fileListing.write(StringTwo)