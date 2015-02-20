import math
print math.sqrt(16)

print "Ints order of ops: expecting 14"
print 2+3*4
print "Using parens to influence operator precedence"
print (2+3)*4
print "Using exponentiation"
print 2**10
print "Using integer division"
print 6/3
print "Using integer division which wll produce fractional remainder"
print 7/3
print "Same thign before but lets introduce a float"
print 7/3.0
print "Using modulus"
print 7%3
print "Using integer division which would product fractional number between 0 and 1"
print 3/4
print "Same thing as above but with the introduction of just one float"
print 3/4.0
print "Now lets produce a LONG"
print 2**10000