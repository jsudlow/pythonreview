def sequentialSearch(alist,item):
  found = False
  pos = 0

  while pos < len(alist) and not found:
    if alist[pos] == item:
      found = True
    else:
      pos = pos + 1
  return found

mylist = ['birds', 'monkey', 'pigs']
item = 'birds'
print sequentialSearch(mylist, item)