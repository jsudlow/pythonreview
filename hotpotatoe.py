from queue import Queue

def hotPotato(namelist, N):

  q = Queue()
  for name in namelist:
    q.enqueue(name)
  while q.size() > 1:
    for i in range(N):
      q.enqueue(q.dequeue())
    q.dequeue()
  return q.dequeue()



namelist = ['Bill', 'Suzy', 'Jon', 'Jeff', 'David']
print hotPotato(namelist, 5)