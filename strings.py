mystring = "Jonathan"
print mystring

print "Lets use some string indexing"
print mystring[-1] #retrieve the last charachter in the string

#duplicate the string
print mystring * 4

#count the length of the string
print len(mystring)

#Using native string methods

#upper case
print mystring.upper()

#center
print mystring.center(20)

#find an a val in the string and return its indexing
print mystring.find('t')

#split some strings on a value
print mystring.split('t')

#count the number of charachters in the string
print mystring.count('a')

#left justify
print mystring.ljust(20)

#lower case
print mystring.lower()

#right justify
print mystring.rjust(20)

#find
print mystring.find('j')
#this should generate an error demonstrating strings are immutable
mystring[0] = 'k'