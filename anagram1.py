#this is the first solution to the anagram problem
#It takes s1 and s2. Converts s2 into a list
def anagramSolution1(s1,s2):
  #converts s2 in a list so we can 'check off' values
  alist = list(s2)
  
  #print alist

  #counter for while loop 1
  pos1 = 0

  #terminator flag for while loop 1
  stillOK = True
  
  #loop over every charachter in string one. Stop until we run out of charachters or we find a charachter that is in one string but not the other
  while pos1 < len(s1) and stillOK:
    #counter for while loop 2
    pos2 = 0

    #terminator for while loop 2
    found = False

    #go throught every value in the length of s2 in list break out of inner loop if we find a value (If we find the val, we dont have to keep checking)
    while pos2 < len(alist) and not found:
      #Test the first charachter of s1 with a alist[n]
      if s1[pos1] == alist[pos2]:
        #print s1[pos1],":",alist[pos2]
        #If we find a charachter match in both strings we set our found flag to true
        found = True
      else:
        #print "in else statement"
        #print s1[pos1],":",alist[pos2]
        #We did not find our charachter is this position. We have to keep moving through the list
        pos2 = pos2 + 1
    
    #we the flag found happens to be set we can 'check off' that value in the last by replacing it with None    
    if found:
      alist[pos2] = None
    else:
      #sadly we did not find  match. This means we do not have an anagram and can terminate :(
      stillOK = False
    #we foudn a match, move on to the next charachter!!  
    pos1 = pos1 + 1
  #return our flag to tell if the two strings are anagrams or not  
  return stillOK

#set some strings and call the anagram function
ana1 = "heat"
ana2 = "teah"

print anagramSolution1(ana1, ana2)