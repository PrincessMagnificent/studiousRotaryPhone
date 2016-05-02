##basic argv

from sys import argv

for x in argv:
    print x
    
script, filename = argv
print "I am %s and I am opening %s" % (script, filename)
file = open(filename,"r")
for line in file:
    for word in line.split():
        print word.capitalize(),