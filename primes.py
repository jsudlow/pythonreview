# should return a list of prime numbers from 1..n (including n)
def sieve(n):
 if n < 2: #there are no prime numbers < 2
  return []
 
 primes = [2] # 2 is the first prime number
 for i in range(3,n+1): #put all of the numbers into primes initially
  primes.append(i)

 #print(primes)

 for i in primes:
   
   for j in primes:
     if j == i: continue
     if j % i == 0:
        #print('multiple found')
        #print(j)
        #if j in primes:
        primes.remove(j)
 print(primes)

sieve(200)