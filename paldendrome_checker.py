from dequeue import Dequeue

def check_word_for_palindrome(word):
  palindrome = True
  d = Dequeue()
  
  #enqueue the inidividual charachters of the word into our queue
  for item in word:
    d.addRear(item)

  while d.size() > 1 and palindrome == True:
    first = d.removeFront()
    last = d.removeRear()
    if first != last:
      palindrome = False
  return palindrome

word = "XANAXX"
print check_word_for_palindrome(word)

