def spin(s,n):
    arr_list = []
    for i in s:
        arr_list.append(i)
    for x in range(n):  
      last_char = arr_list[-1]
      count = len(arr_list)
      for i in arr_list:
        arr_list[count-1] = arr_list[count -2]
        
        count -=1
      arr_list[0] = last_char
      print(arr_list)

spin('abc',4)