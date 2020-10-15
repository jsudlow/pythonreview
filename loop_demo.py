def greatest_power_2(n):
    i = 1
    answer = 1
    while i <= n:
      #print('running')
      #print(i)
      answer = i * 2
      i = i * 2
    
    return(answer/2)

answer = greatest_power_2(34)
print(answer)