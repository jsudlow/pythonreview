def draw_right_triangle(triangle_char, triangle_height):
    x = ''
    for i in range(triangle_height):
        x += (triangle_char + ' ') * (i + 1)
        if i == (triangle_height - 1):
        	pass
        else:
        	x += '\n'
    return x


if __name__ == "__main__":

  print('This program will draw a right triangle')
  triangle_char = input('Enter a character:')
  triangle_height = int(input('Enter triangle height:'))
  print(draw_right_triangle(triangle_char,triangle_height))

