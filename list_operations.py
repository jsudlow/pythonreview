mylist = ['Jonstele',1,1.5]

#Appends a new item to the end of the list
mylist.append(False)
print mylist

#Insert at the i'th piont in the list
mylist.insert(0,'Another string')
print mylist

#pop - removes and returns last item in list
print mylist.pop()

#pop the i'th element of our list
print mylist.pop(0)

#sort - sorts the list
mylist.sort()
print mylist

#reverse the list
mylist.reverse()
print mylist

#delete an item at mylist[i]
del mylist[1]

print mylist

#Return an index of the first occurance of an object
print mylist.index(1)

#Count the ouccurances of an item in the list
print mylist.count('Dodgy')

#remove - removes the first occurance of item
mylist.remove(1)
print mylist

#note the dot notation we are using. even simple data ints can do this
print (54).__add__(24)