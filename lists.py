mylist = [1.3, True,2,2L,'A string']
print mylist

#get a particular element out of a list(using indexing)
print mylist[0:3]

#duplicate the list(using concatentation)
print mylist + mylist

#check for values in a list
print True in mylist

#concatante a repeated number of times using repitition
print mylist * 4

#get the length of a list
print len(mylist)

#illustrate important aspect of the repitation operator
mylist = [1,2,3,4]

#A holds a collection of 3 references to the original list. This example is important because
#if you change the data object of a single list component, the change shows up in all three lists
#this is because of the way the references are pointing to the lists.
A = [mylist] * 3
print A
mylist[2] = 99
print A