#  File geotest.py

################################################################
#  You should not modify anything in this file
################################################################

from geometry import distance, slope, intercept, lineequation, inf


def print_point(x, y):
    print("(", x, ",", y, ")", sep="", end="")

def do_distance(x1, y1, x2, y2):
    print(end="The distance between ")
    print_point(x1, y1)
    print(end=" and ")
    print_point(x2, y2)
    print("is ", distance(x1, y1, x2, y2))

def do_slope(x1, y1, x2, y2):
    print(end="The slope of the line between ")
    print_point(x1, y1)
    print(end=" and ")
    print_point(x2, y2)
    print(end=" is ")
    m = slope(x1, y1, x2, y2)
    if m == inf:
        print("undefined")
    else:
        print(m)

def do_intercept(x1, y1, x2, y2):
    if slope(x1, y1, x2, y2) == inf:
        print(end="The x-")
    else:
        print(end="The y-")
    print(end="intercept of the line between ")
    print_point(x1, y1)
    print(end=" and ")
    print_point(x2, y2)
    print(" is", intercept(x1, y1, x2, y2))

def do_equation(x1, y1, x2, y2):
    print(end="The equation of the line between ")
    print_point(x1, y1)
    print(end=" and ")
    print_point(x2, y2);
    print(end=" is ")
    print(lineequation(x1, y1, x2, y2))


def main():
    print("Enter the coordinates of the two points")
    while True:   #  Infinite loop, use Control-C to quit
        p_x1 = float(input("Enter x1 (Control-C quits): "))
        p_y1 = float(input("Enter y1 (Control-C quits): "))
        p_x2 = float(input("Enter x2 (Control-C quits): "))
        p_y2 = float(input("Enter y2 (Control-C quits): "))
        do_distance(p_x1, p_y1, p_x2, p_y2)
        do_slope(p_x1, p_y1, p_x2, p_y2)
        do_intercept(p_x1, p_y1, p_x2, p_y2)
        do_equation(p_x1, p_y1, p_x2, p_y2)
        print("-----------------")

main()   #  Run main


