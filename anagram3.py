#This solution is based on observing a letter in a string and adding it to its own count. We do this with both strings.
#We can then compare the two counts and they should be equal if the words are anagrams, they wont be equal if the words are not.

def anagramSolution3(s1,s2):
  #Initialize empty count lists with [0] repeated 26 times. If we dont do this and try to access a space in the list python will compalin
  #about an out of bounds access
  c1 = [0] * 26
  c2 = [0] * 26

  for i in range(len(s1)):
    #the ord('a') is 97. Any letters ordinal subtracted with the ordinal of 'a' will get us a value between 0 and 26. Just the kind of impressioning
    #we want for an alphabetical count
    pos = ord(s1[i]) - ord('a')
    c1[pos] = c1[pos] + 1

  #we use the same process here as we did on the first loop
  for i in range(len(s2)):
    pos = ord(s2[i]) - ord('a')
    c2[pos] = c2[pos] + 1


  #now we can go through our lists and compare the counts of the individual charachters.
  #we get equal for every one, stillOK stays equal and we have an anagram. Any other way stillOk
  #will get set to false
  j = 0
  stillOK = True

  while j < 26 and stillOK:
    if c1[j] == c2[j]:
      j = j + 1
    else:
      stillOK = False
  return stillOK


s1 = "earth"
s2 = "hearz"
print anagramSolution3(s1,s2)

#we do not have nested iterators like the first 2 anagram problems. 
#we have 2 iterators based on N, so that makes 2n
#we have an iterator than can take a maximum of 26 steps so that makes t(n) = 2n + 26, or O(n) which is linear
#This algo sacrficed space in order to gain time. The other 2 solutions did not require any additional space beyond the space the strings themselves occupied
