import numpy as np

def midpointint(f,a,b,n):
  accumulator = 0
  h = (b - a) / (float(n))
  for i in np.array(range(1,n+1)):
    value = h * np.sum((f(a - (0.5*h) + (i*h))))
    accumulator += value
  return accumulator

print(midpointint(np.sin,0,np.pi,10))