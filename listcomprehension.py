#Make an emtpy list and fill it with consecutive numberse * 2

a = []
for x in range(10):
  a.append(x*2)
print a

#if you wanted to compact this kind of code you do whats called a list comprehension
a =[x*2 for x in range(10)]