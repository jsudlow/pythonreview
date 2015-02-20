mytuple = (True, 2, 'jon')

print mytuple

#lets get the length
print len(mytuple)

#grab an index
print mytuple[2]

#concatanation via repitition
print mytuple * 3

#slice out a section
print mytuple[0:2]

#lets try and change a tuple however! error does not support assignment as expected. Tuples are immutable.
mytuple[1] = False