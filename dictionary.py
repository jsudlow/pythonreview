capitals = {'Chicago':'Illinois', 'St Louis':'Missouri' }
print capitals
print capitals['Chicago']
capitals['Utah'] = 'Salt Lake City'
print capitals
capitals['Sacremento'] = 'California'
print capitals

print len(capitals)

#lets try some dictionary operations
print capitals.keys()
print capitals.values()
print capitals.items()
print capitals.get('Chicago')
#optional second param to get do speicify return type if key not in dict
print capitals.get('Santa fe', "CAPITAL NOT IN LIST")

print 'Chicago' in capitals

print capitals.has_key('Chicago')
del capitals['St Louis']
print capitals