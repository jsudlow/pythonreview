def draw_arrow_base(base_height,base_width,head_width,symbol):
  while head_width <= base_width:
      head_width = int(input('Enter arrow head width:\n'))
  print()

  for i in range(base_height):
      for x in range(base_width):
          print(symbol, end='')
      print()


def draw_arrow_head(head_width,symbol):      
  for i in range(head_width):
      for x in range(head_width - i):
          print(symbol, end='')
      print()


if __name__ == "__main__":
  symbol = input('Enter a character:')	
  base_height = int(input('Enter arrow base height:\n'))
  base_width = int(input('Enter arrow base width:\n'))
  head_width = int(input('Enter arrow head width:\n'))      

  draw_arrow_base(base_height,base_width,head_width,symbol)
  draw_arrow_head(head_width,symbol)