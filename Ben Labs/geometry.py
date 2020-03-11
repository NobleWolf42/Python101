'''
geometry.py
Contains analytical geometry functions to compute line slope, 
distance between points, line intercepts, and line intersections.
'''

from math import sqrt, fabs

#  Python 3.5 has math.inf, but 3.4 does not
from sys import version_info
if version_info.major == 3 and version_info.minor == 5:
    from math import inf
else:
    inf = float("inf")


def floatequals(a, b):
    '''
    Returns True if the floating-point values a and b are
    close enough in value to be considered equal; otherwise,
    the function returns False.  The parameters are considered
    equal when they are within 0.001 of each other.
    '''
    return a == b or fabs(a - b) < 0.001


def distance(x1, y1, x2, y2):
    '''
    Computes the distance between the points (x1,y1) and (x2,y2),
    where x1, y1, x2, and y2 are numbers.
    '''
    return sqrt(((x2-x1)**2)+((y2-y1)**2))


def slope(x1, y1, x2, y2):
    '''
    Computes the slope of the line that passes between the points 
    (x1,y1) and (x2,y2).  The function returns Math.inf if a vertical 
    line passes through the two points.  The function's behavior is
    undefined if the two points are identical.  
    x1, y1, x2, and y2 are numbers.
    '''
    if (x2-x1) == 0:
        return inf
    else:
        return (y2-y1)/(x2-x1)


def intercept(x1, y1, x2, y2):
    '''
    Computes the y-intercept of the non-vertical line that 
    passes through the points (x1,y1) and (x2,y2).  The 
    function returns the x-intercept if the line is vertical.  
    Two identical points are interpreted to be on a 
    vertical line.
    '''
    if x1 == x2:
        return x1
    else:
        return y1-slope(x1, y1, x2, y2)*x1


def lineequation(x1, y1, x2, y2):
    '''
    Returns a string representation of a line passing through the points
    (x1,y1) and (x2,y2).  The result is in the form y = mx + b for 
    non-vertical lines and x = b for vertical lines.  The representation
    is as simple as possible; e.g., 
         y = 3x - 2      not y = 3x + -2
         y = x + 3       not y = 1x + 3
         y = 5           not y = 0x + 5
         x = 4           a vertical line
    '''
    inter = intercept(x1, y1, x2, y2)
    slpe = slope(x1, y1, x2, y2)
    if inter < 0:
        sym = " - "
        pinter = abs(inter)
    else:
        sym = " + "
        pinter = inter
    if slpe == inf:
        return "x = " + str(x1)
    elif slpe == 0:
        return "y = " + str(inter)
    elif slpe == 1 and inter == 0:
            return "y = " + "x"
    elif slpe == 1:
        return "y = " + "x" + sym + str(pinter)
    elif inter == 0:
        return "y = " + str(slpe) + "x"
    else:
        return "y = " + str(slpe) + "x" + sym + str(pinter)

def intersection(m1, b1, m2, b2):
    '''
    Computes the (i_x, i_x) intersection point of the lines 
    y = m1x + b1 and y = m2x + b1.  Returns None if the lines 
    do not intersect in a single point.
    '''
    if m1 == m2:
        return None
    elif m1 != inf and m2 != inf:
        xv = (b2 - b1) / (m1 - m2)
        yv = (m1 * xv) + b1
        return (xv, yv)
    elif m1 == inf:
        xv = b1
        yv = (m2 * xv) + b2
        return (xv, yv)
    elif m2 == inf:
        xv = b2
        yv = (m1 * xv) + b1
        return (xv, yv)




if __name__ == '__main__':
    pass

