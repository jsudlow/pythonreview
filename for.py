for item in [1,2,3,4,5]:
  print item

for item in range(5):
  print item ** 2

wordlist = ['Jon', 'Bill', 'Tom']
letterlist = []
for word in wordlist:
  for char in word:
    letterlist.append(char)

print letterlist