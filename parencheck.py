from stack import Stack

def parenCheck(symbolString):
  s = Stack()
  balanced = True
  index = 0

  while index < len(symbolString) and balanced:
    symbol = symbolString[index]
    if symbol == '(':
      s.push(symbol)
    else:
      if s.isEmpty():
        balanced = False
      else:
        s.pop()
    index +=1

  if balanced and s.isEmpty():
    return "The parens are balanced"
  else:
    return "The parens are unbalanced"
print parenCheck("((()))")
