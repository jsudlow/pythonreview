class Dequeue:
  def __init__(self):
    self.items = []
  def addFront(self,item):
    self.items.insert(0,item)
  def addRear(self,item):
    self.items.append(item)
  def removeFront(self):
    return self.items.pop()
  def removeRear(self):
    return self.items.pop(0)
  def size(self):
    return len(self.items)
  def isEmpty(self):
    return self.items == []
'''
d = Dequeue()
print d.isEmpty()
d.addFront('dog')
d.addFront('cat')
d.addRear('elephant')
print d.size()
print d.isEmpty()
print d.removeFront()
print d.removeRear()

'''