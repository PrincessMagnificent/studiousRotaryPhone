import string

readings = open("Chaos.txt", "r")

print "If that worked, tell me..."
print "What is the name? It is " + readings.name
fileLineList = []
for line in readings:
    print type(line)
    fileLineList.append(line)
    
print "fileLineList is long %i" % (len(fileLineList))
counter = 0
wordcount = 0
megadict = {}
nuCount = 0
highest = 0

for x in fileLineList:
    counter +=1
    ##This just removes the endline in the original text because we already are inserting an \n automatically with print related problems
    ##The translate replaces all the punctuation. None having a capital N is very important, too.
    x = x.replace("\n","")
    x = x.replace("\"","")
    x = x.translate(None,string.punctuation)
    ##Turns a string into a list using " " automatically, because I didn't specify what he's separating by.
    line = string.split(x)
    
    #Get rid of empty lines, we don't care about them
    if x == " " or x == "":
        print "%i: EMPTY" % counter
        
    ##This is the big counting words in the text portion. If the word isn't already in the megadictionary, it gives it a one. If it is, it adds one.
    else:
        for word in line:
            if word not in megadict:
                ##This actually adds both the key ("word") and the value for it in one line! Huzzah!
                megadict[word] = 1
                nuCount += 1
            else:
                megadict[word] += 1
                if megadict[word] > highest:
                    highest = megadict[word]
                
        print "%i: %s (%i WORDS)" % (counter, x, len(line))
        wordcount += len(line)
    

print "We have %i words here." % wordcount
print "We have %i new words." % nuCount
print "The most frequent word appears %i times." % highest

##But this gives me a more or less random one. I need to print megadict in ORDER.
# print sorted(megadict, megadict[1])
results = open("result" + readings.name, "w")

megaresult = []
for numbers in range(1,highest+1):
    megaresult.append([numbers])
megaresult.insert(0,"CHART")
for x in megaresult:
    print x
##FUCKING THERE WE GO! Finally managed to finagle this dictionary into putting things right. What happens here is, megaresult has openings for all the possible numbers, but they're not numbers, they're lists with only one number. Hence the need for num[0].
##then we just append to them.
##All that remains to be done is to print it out more PRETTILY. 
for entry in megadict:
    for num in megaresult:
        if num[0] == megadict[entry]:
            num.append(entry)


    
for x in megaresult:
    results.write(str(x))
    results.write("\n")

readings.close()
results.close()
# # We are almost ready to check the frequency of words in files!!

##TO DO:

##Figure out a way to actually order the words. Probably need Class to do that, though. 

##WAAAAAIT. I don't need them all in the same line! I can just make a list where the first dimension is the numbers, and the second is a list of all the words who appear that number of times! Brilliant!

##Okay, I now know how long the actual list of words has to be, because I have the highest variable there. 