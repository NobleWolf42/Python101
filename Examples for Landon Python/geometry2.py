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
    distance = sqrt((x2 - x1)**2 + (y2-y1)**2)
    return distance


def slope(x1, y1, x2, y2):
    '''
    Computes the slope of the line that passes between the points 
    (x1,y1) and (x2,y2).  The function returns Math.inf if a vertical 
    line passes throught the two points.  The funnction's behavior is 
    undefined if the two points are identical.  
    x1, y1, x2, and y2 are numbers.
    '''
    if (x2-x1) == 0:
        return inf
    else:
        slope = (y2-y1)/(x2-x1)
        return slope


def intercept(x1, y1, x2, y2):
    '''
    Computes the y-intercept of the non-vertical line that 
    passes through the points (x1,y1) and (x2,y2).  The 
    function returns the x-intercept if the line is vertical.  
    Two identical points are interpreted to be on a 
    vertical line.
    '''
    if (x2-x1) == 0:
        intercept = x1
    else:
        intercept = y1 - (slope(x1, y1, x2, y2) * x1)
    return intercept


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
    if slope(x1, y1, x2, y2) == inf:
        return "x = " + str(x1)
    elif slope(x1, y1, x2, y2) == 1:
        if intercept(x1, y1, x2, y2) < 0:
            return "y = x" + str(intercept(x1, y1, x2, y2))
        else:
            return "y = x" + " + " + str(intercept(x1, y1, x2, y2))
    elif slope(x1, y1, x2, y2) == 0:
        return "y = " + str(intercept(x1, y1, x2, y2))
    else:
        if intercept(x1, y1, x2, y2) < 0:
            return "y = " + str(slope(x1, y1, x2, y2)) + "x" + " - " + str(abs(intercept(x1, y1, x2, y2)))
        else:
            return "y = " + str(slope(x1, y1, x2, y2)) + "x" + " + " + str(intercept(x1, y1, x2, y2))


def intersection(m1, b1, m2, b2):
    '''
    Computes the (i_x, i_x) intersection point of the lines 
    y = m1x + b1 and y = m2x + b1.  Returns None if the lines 
    do not intersect in a single point.
    '''



if __name__ == '__main__':
    pass

