def anagramSolution2(s1,s2):

  #make a list out of our strings
  alist1 = list(s1)
  alist2 = list(s2)

  #sort them. This become the dominant part of our program actually. Overtime the sorts are the largest part of the steps of T(n)
  #Sorting is actually O(n^2) (quadratic) or O(n log n) (log linear)
  alist1.sort()
  alist2.sort()

  #print alist1
  #print alist2
  pos = 0
  matches = True

  #loop through list 1 and terminate on matches being false
  while pos < len(s1) and matches:
    #I print out a helpful statement so you can visualize which characheres are being compared to which
    print alist1[pos],":",alist2[pos]
    if alist1[pos] == alist2[pos]:
      #If the chars equal eachother than we move on
      pos += 1
    else:
      #If they dont equal eachoher, we have to set matches to false and termiate bc we dont have an anagram
      matches = False

  return matches

s1 = "earth"
s2 = "heart"
print anagramSolution2(s1,s2)