n = 1

if n > 0:
  print "N is greater then 0"
else:
  print "N is LESS than 0"


#nested if else if statement
score = 48

if score >= 90:
  print 'A'
else:
  if score >= 80:
    print 'B'
  else:
    if score >= 70:
      print 'C'
    else:
      if score >= 60:
        print 'D'
      else:
        if score >=50:
          print 'F'

#using elif this can be much more simplified and include a default case for the else
if score >=90:
  print 'A'
elif score >= 80:
  print 'B'
elif score >= 70:
  print 'C'
elif score >= 60:
  print 'D'
else:
  print 'F'