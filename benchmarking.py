import time

def sumN(n):
  start = time.clock()
  theSum = 0
  for i in range(1,n+1):
    theSum += i
  finish = time.clock()
  val = finish - start
  mys = "Execution time: %f10" %val
  print "Time took to finish",mys 
  return theSum

#lets list another version of a summation
def badSumN(tom):
  start = time.clock()
  fred = 0
  for bill in range(1,tom + 1):
    barney = bill
    fred = barney + fred
  finish = time.clock()
  val = finish - start
  mys = "Execution time: %f10" %val
  print "Time took to finish",mys
  return fred
print sumN(400)
print badSumN(400)

#we can see the first summation takes just a little less time to complete than the bad sum.

