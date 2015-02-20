#creates a new var sum. The right hand side gets evaluated at 0 and a reference to this 0 data object gets stored in the varaiable called sum

sum = 0
print sum

#increment sum by 1, note ites still an integer
sum += 1
print sum

#Now we change the reference of sum to a boolean True. This turns sum into a boolean data type now. This is cool because 
#sum can be used to represent all kinds of different types and it can change bc of the way python handles assignement and
#employes the user of references. 
sum = True
print sum