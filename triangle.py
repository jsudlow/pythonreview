import math
import logging
""" A collection of methods for dealing with triangles specified by the length
    of three sides (a, b, c)

    If the sides cannot form a triangle,then return None for the value

"""

## @TODO - add the errlog method and use wolf fencing to identify the errors in this code



def validate_triangle(sides):
    """
    This method should return True if and only if the sides form a valid triangle
        Given three side lengths, the sum of smallest two should be greater than longest sides

    :param sides: a tuple with side lengths
    :return: True if sides form a triangle, False otherwise
    """
    #This is an unfinished method that validates every triangle...lets fix it
    #logging.error(sides)
    sorted_sides = sorted(sides)
    #logging.error("This is the length of the sorted sides", len(sorted_sides))
    #logging.error("The  triangle coming in is", sorted_sides)

    #we have to add a check to make sure we are actually getting 3 sides
    if len(sorted_sides) != 3:
        return False
    
    sum_of_two = sorted_sides[0] + sorted_sides[1]
    #logging.error("The sum of two is: ", sum_of_two)
    if sum_of_two > sorted_sides[2]:

      return True
    else:
        return False

def get_angle(sides):
    """
    Returns the angle C defined for the triangle defined by side lengths (a, b, c)
    first value in the tuple point
    :param sides: a tuple with 3 side lengths
    :return: the angle (in radians) of the angle opposite side c; return None if invalid
    """
    # Using the law of cosines
    #  c^2 = a^2 + b^2 - 2abcos(C)
    #  cos(C) = (a^2 + b^2 - c^2)/(2ab)

    a = sides[0]
    b = sides[1]
    #logging.error("The side indices are blowing up. I want to see what the acutal sides are", sides)
    #the tuple is ((3,4,5),)
    #and sides=[3] is causing the error because of an off by one mistake. sides[3] is asking for a 4th number and that doesn't make sense
    #because we are trying to make triangle, not a rectangle. 

    c = sides[2]
   
    num = math.pow(a, 2) + math.pow(b,2) - math.pow(c,2)
    #c^2 should be subtracted - not added
    den = 2*a*b

    val = num/den
    #logging.error("What is it about these sides that is triggering an error", sides)
    #logging.error("Why is val throwing a math domain error?", val)
    #val seems to be a floating point number
    #the acos only takes a value from -1 to 1 and we are getting a number greater then one. Let me check the math

    angle = math.acos(val)

    return angle

def get_height(sides):
    """
    Returns the height of triangle defined by side lengths (a, b, c)

    Given angle C between sides a & b, the height h from side b to vertex of a and c is
    given by sin(C) = h/a so that h = a*sin(C)
       /|\
      / | \
    a/  |  \ c
    / C |h  \
   /____|____\
         b
    :param sides:
    :return: height from b side to a-c vertex; None if invalid sides
    """

    C = get_angle(sides) # angle formed by sides a and b, opposite side c
    height = sides[0]*math.sin(C)
    return height

def get_area(sides):
    """
    Returns the area of triangle defined by side lengths (a, b, c)
    :param sides:
    :return: area
    """
    if (not validate_triangle(sides)):
      return None
    base   = sides[1]
    height = get_height(sides)
    area = (1/2.)*base*height
    return area

def get_area_heron(sides):
    """
    Returns the area of triangle defined by side lengths (a, b, c)
    using https://www.mathsisfun.com/geometry/herons-formula.html

    This method is intended to be correct to assist you in debugging other methods

    :param sides:
    :return: area
    """
    if (not validate_triangle(sides)):
        return None


    a  = sides[0]
    b  = sides[1]
    c  = sides[2]
    s  = 0.5*(a + b + c)
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    return area

print('name is',__name__)
if __name__ == "__main__":
    sides = (3, 4, 5)
    areaHeron = get_area_heron(sides) # This should be 6.0
    area      = get_area(sides)
    print('Area of triangle with sides={} is {} {}'.format(str(sides), str(area), str(areaHeron)))

    sides = (4, 5, 3)
    areaHeron = get_area_heron(sides) # This should be 6.0 (same as 3,4,5)
    area      = get_area(sides)
    print('Area of triangle with sides={} is {} {}'.format(str(sides), str(area), str(areaHeron)))

    sides = (2, 2, 2*math.sqrt(2)) # equilateral right triangle
    areaHeron = get_area_heron(sides) # This should be 2.0
    area      = get_area(sides)
    print('Area of triangle with sides={} is {} {}'.format(str(sides), str(area), str(areaHeron)))

    sides = (4, 4, 5) # This is an invalid triangle
    #input error, this is actually a valid triangle
    areaHeron = get_area_heron(sides) #
    area      = get_area(sides)
    print('Area of triangle with sides={} is {} {}'.format(str(sides), str(area), str(areaHeron)))

    sides = (3, 4, 8) # This is an invalid triangle
    areaHeron = get_area_heron(sides) # This should be None
    #logging.error('Is area heron actually invalding correctly', areaHeron)
    area      = get_area(sides)
    print('Area of triangle with sides={} is {} {}'.format(str(sides), str(area), str(areaHeron)))

    sides = (3, 4) # This is an invalid triangle
    areaHeron = get_area_heron(sides) # This should be None
    area      = get_area(sides)
    print('Area of triangle with sides={} is {} {}'.format(str(sides), str(area), str(areaHeron)))
