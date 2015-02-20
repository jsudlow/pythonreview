

class Fraction:
  def __init__(self,top,bottom):
    #These values will provide the internal state for the physcial perspective
    self.num = top
    self.denom = bottom
  def __str__(self):
    return str(self.num) + "/" + str(self.denom)
  #add fractions
  #a/b + c/d = ad/bd + cb/bd = ad + cb/bd
  def __add__(self,otherfraction):
    #ad + cb
    new_numer = self.num * otherfraction.denom + otherfraction.num * self.denom 
    new_denom = self.denom * otherfraction.denom
    print new_numer
    print new_denom
    new_gcd = self.gcd(new_numer, new_denom)
    #divide the numerator and denom by the new_gcd so they are expressed in lowest terms
    return Fraction(new_numer/new_gcd,new_denom/new_gcd)
  #GCD of 2 ints m,n is n if n divides m evenly
  #If n does not divide m evenly, then the answer is the GCD on n and the remainder of m/n
  def gcd(self,m,n):
    while m % n != 0:
      oldm = m
      oldn = n 

      m = oldn
      n = oldm % oldn
    return n
  def __cmp__(self,otherfraction):
    num1 = self.num * otherfraction.denom
    num2 = self.denom * otherfraction.num

    if num1 < num2:
      return -1
    else:
      if num1 == num2:
        return 0
      else:
        return 1


myf = Fraction(1,2)
myf2 = Fraction(1,2)
print myf + myf2
print myf == myf2
