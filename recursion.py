def listsum(l):

  #base case
  if len(l) == 1:
    return l[0]
  else:
    return l[0] + listsum(l[1:])

mylist=[1,4,3,2,5]
print listsum(mylist)