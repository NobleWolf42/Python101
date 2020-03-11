from tkinter import *
from math import fabs   #  Absolute value function
from geometry import *

def diff(a, b):
    '''
    Compute the absolute value of the difference of a and b
    '''
    return (a - b if a > b else b - a)

class Point:
    '''
    A geometric point consisting of an (x,y) coordinate pair.
    '''
    def __init__(self, x, y):
        '''
        Constructor initializes the (x,y) coordinates of a point. 
        '''
        self.x, self.y = x, y

    def __equals__(self, other):
        '''
        Returns True if the (x,y) coordinates of 'other' equal to the
        (x,y) coordinates of this point object. 
        '''
        return floatequals(self.x, other.x) and floatequals(self.y, other.y)


def tuple_to_point(t):
    """ Returns a Point object with x component equal to t[0] and
        y component equal to t[1].  Returns None if t is None. """
    return Point(t[0], t[1]) if t else None

def point_intersection(p1, p2, p3, p4):
    '''
    Returns the point of intersection of the line p1-p2 and line
    p3-p4.  Returns None if the lines do not intersect in a single
    point.
    '''
    return intersection(slope(p1.x, p1.y, p2.x, p2.y), 
                        intercept(p1.x, p1.y, p2.x, p2.y), 
                        slope(p3.x, p3.y, p4.x, p4.y), 
                        intercept(p3.x, p3.y, p4.x, p4.y))


class VisualGeometry:
    #  Class variable
    NO_POINT = Point(-1, -1)

    def __init__(self):
        '''
        Initializes the visual geometry window and points.
        '''
        self.root = Tk()
        self.canvas = Canvas(self.root, width=600, height=600, 
                             bg='white', cursor='arrow')

        #  The points managed by the program
        self.clear_points()
        
        #  Is the user currently dragging a point?
        self.dragging = False

        self.root.resizable(0, 0)
        #self.root.wm_title('Visual Geometry: ' + str(self.points))
        self.root.wm_title('Visual Geometry')
        self.canvas.pack(fill=BOTH, expand=YES)
        self.canvas.bind('<ButtonPress-1>', self.mouse_pressed)
        self.canvas.bind('<ButtonRelease-1>', self.mouse_released)
        self.canvas.bind('<Motion>', self.mouse_moved)
        self.canvas.bind('<B1-Motion>', self.mouse_moved)
        self.canvas.bind_all('<Key>', self.key_pressed)
        self.repaint()
        self.root.mainloop()

    def match_point(self, x, y):
        '''
        Returns the point located within four pixels of the point
        (x,y).  If no point is within that distance to (x,y), the
        method return VisualGeometry.NO_POINT.
        '''
        if diff(x, self.vertex1.x) < 4 and diff(y, self.vertex1.y) < 4:
            return self.vertex1
        elif diff(x, self.vertex2.x) < 4 and diff(y, self.vertex2.y) < 4:
            return self.vertex2
        elif diff(x, self.vertex3.x) < 4 and diff(y, self.vertex3.y) < 4:
            return self.vertex3
        elif diff(x, self.vertex4.x) < 4 and diff(y, self.vertex4.y) < 4:
            return self.vertex4
        else:
            return VisualGeometry.NO_POINT

    def draw_control_point(self, canvas, pt, color):
        '''
        Draws one of the movable control points.  If the point is
        active (the cursor is over the point), the point is drawn
        larger than normal to provide visual feedback to the user
        that the point is active.
        '''
        #  Draw a big box when mouse cursor is over the point
        if pt == self.active_point:
            canvas.create_rectangle((pt.x - 10, pt.y - 10, 
                                     pt.x + 10, pt.y + 10), outline=color)
            self.point_text(pt, color)
            #canvas.create_text(pt.x, pt.y + 20, 
            #                   text=('(%2.2f,%2.2f)' % (pt.x, pt.y)))
        else:    #  Draw little box when mouse cursor not over the point
            canvas.create_rectangle((pt.x - 4, pt.y - 4, 
                                     pt.x + 4, pt.y + 4), fill=color)

    def draw_point(canvas, pt, color):
        '''
        Draw a point with a given color
        '''
        canvas.create_rectangle((pt.x - 2, pt.y - 2, 
                                 pt.x + 2, pt.y + 2), fill=color)

    def draw_line(self, canvas, p1, p2, color):
        '''
        Draw the line segment between the points p1 and p2 with the
        color color.
        '''
        canvas.create_line(p1.x, p1.y, p2.x, p2.y, fill=color)

    def drawExtendedLine(self, canvas, p1, p2, color):
        '''
        Draw the line that passes through the points p1 and p2.
        The line extends to the border of the window.  The line's
        color is color.
        '''
        m = slope(p1.x, p1.y, p2.x, p2.y)
        b = intercept(p1.x, p1.y, p2.x, p2.y)
        new_x1 = p1.x
        new_y1 = p1.y
        new_x2 = p2.x
        new_y2 = p2.y
        if m == inf:
            new_x1 = new_x2 = p1.x
            new_y1 = 0
            new_y2 = 600
        elif m >= -1.0 and m <= 1.0:
            pi1 = tuple_to_point(intersection(m, b, inf, 0))
            pi2 = tuple_to_point(intersection(m, b, inf, 600))
            if pi1:
                new_x1 = pi1.x
                new_y1 = pi1.y
            if pi2:
                new_x2 = pi2.x
                new_y2 = pi2.y
        else:
            pi1 = tuple_to_point(intersection(m, b, 0, 0))
            pi2 = tuple_to_point(intersection(m, b, 0, 600))
            if pi1:
                new_x1 = pi1.x
                new_y1 = pi1.y
            if pi2:
                new_x2 = pi2.x
                new_y2 = pi2.y
        canvas.create_line(new_x1, new_y1, new_x2, new_y2, fill=color, width=2)
        self.draw_control_point(canvas, p1, color) 
        self.draw_control_point(canvas, p2, color) 

    def point_text(self, pt, color):
        '''
        Draws the string containing the coordinates for point pt in
        color color.
        '''
        self.canvas.create_text(pt.x, pt.y + 20, 
                           text=('(%2.1f,%2.1f)' % 
                           (pt.x - 300, 300 - pt.y)), fill=color)

    def line_text(self, x, y, p1, p2, color):
        '''
        Draws the string representing the equation of the line 
        passing through points p1 and p2 in y = mx + b form.
        The color is color, and the string is displayed at (x,y).
        '''
        eqn = lineequation(p1.x - 300, 300 - p1.y, 
                           p2.x - 300, 300 - p2.y)
        self.canvas.create_text(x, y, text=eqn, fill=color)

    def draw_axes(self, canvas):
        '''
        Draws the x- and y-axes and accessory grid lines at 20 unit
        intervals.
        '''
        for x in range(0, 600, 50):
            canvas.create_line((x, 0, x, 600), fill='lightblue')
        for y in range(0, 600, 50):
            canvas.create_line((0, y, 600, y), fill='lightblue')
        canvas.create_line((0, 300, 600, 300), fill='black')
        canvas.create_line((300, 0, 300, 600), fill='black')

    def draw(self, canvas):
        '''
        Draws the contents of the window.
        '''
        #  Draw the axes
        self.draw_axes(canvas)
        #  Draw the control points
        if self.vertex1 != VisualGeometry.NO_POINT:
            self.draw_control_point(canvas, self.vertex1, 'blue')
            if self.vertex2 != VisualGeometry.NO_POINT:
                self.draw_control_point(canvas, self.vertex2, 'blue')
                self.drawExtendedLine(canvas, self.vertex1, self.vertex2, 'blue')
                self.line_text(50, 500, self.vertex1, self.vertex2, 'blue')
                if self.vertex3 != VisualGeometry.NO_POINT:
                    self.draw_control_point(canvas, self.vertex3, 'green')
                    if self.vertex4 != VisualGeometry.NO_POINT:
                        self.draw_control_point(canvas, self.vertex4, 'green')
                        self.drawExtendedLine(canvas, self.vertex3, 
                                              self.vertex4, 'green')
                        self.line_text(50, 530, self.vertex3, 
                                       self.vertex4, 'green')
                        inter = point_intersection(self.vertex1, self.vertex2, 
                                                   self.vertex3, self.vertex4)
                        inter = tuple_to_point(inter)
                        if inter != None:
                            self.intersection = inter
                            self.draw_control_point(canvas, self.intersection, 
                                                    'red')
                            self.point_text(self.intersection, 'red')
                        else:
                            self.intersection = VisualGeometry.NO_POINT

    def do_quit():
        '''
        Quit the application
        '''
        close()  #  Quit the application

    def mouse_released(self, event):
        if not self.dragging and self.vertex4 == VisualGeometry.NO_POINT \
                and self.active_point == VisualGeometry.NO_POINT:
            pt = Point(event.x, event.y)
            if self.vertex1 == VisualGeometry.NO_POINT:
                self.vertex1 = pt
            elif self.vertex2 == VisualGeometry.NO_POINT:
                self.vertex2 = pt
            elif self.vertex3 == VisualGeometry.NO_POINT:
                self.vertex3 = pt
            else:
                self.vertex4 = pt
            self.repaint()
        self.dragging = False
        #self.active_point = VisualGeometry.NO_POINT

    def mouse_moved(self, event):
        x = event.x
        y = event.y
        if self.dragging:
            self.active_point.x = x
            self.active_point.y = y
            self.repaint()
        else:
##            self.active_point = self.match_point(event.x, event.y)
##            if self.active_point != VisualGeometry.NO_POINT:
##                self.repaint()
            prev = self.active_point
            self.active_point = self.match_point(x, y)
            if self.active_point != VisualGeometry.NO_POINT:
                self.canvas.config(cursor='fleur')
            else:
                self.canvas.config(cursor='arrow')
            if self.active_point == VisualGeometry.NO_POINT and \
                             prev != VisualGeometry.NO_POINT:
                self.repaint()
            elif self.active_point != VisualGeometry.NO_POINT:
                self.repaint()

    def mouse_pressed(self, event):
        x = event.x
        y = event.y
        self.active_point = self.match_point(x, y)
        if self.active_point != VisualGeometry.NO_POINT:
            self.active_point.x = x
            self.active_point.y = y
            self.dragging = True
        self.repaint()

    def clear_points(self):
        '''
        Removes all the points from the viewport to (re)start the
        session.
        '''
        self.vertex1 = VisualGeometry.NO_POINT
        self.vertex2 = VisualGeometry.NO_POINT
        self.vertex3 = VisualGeometry.NO_POINT
        self.vertex4 = VisualGeometry.NO_POINT
        self.intersection = VisualGeometry.NO_POINT
        self.active_point = VisualGeometry.NO_POINT

    def repaint(self):
        '''
        Force the window to redraw itself.  Remove the current
        graphical objects.
        '''
        #  Remove current graphical objects
        self.canvas.delete(ALL)
        self.draw(canvas=self.canvas)
        
    def key_pressed(self, event):
        '''
        Respond to user key strokes.  The 'Z' key clears the
        points from the viewport.
        '''
        ch = event.char
        if ch == 'z' or ch == 'Z':
            self.clear_points()
        elif ch == 'V' or ch == 'v':
            if self.vertex1 != VisualGeometry.NO_POINT \
               and self.vertex2 == VisualGeometry.NO_POINT:
                x, y = self.vertex1.x, self.vertex1.y
                self.vertex2 = Point(x, y + 10)
            elif self.vertex3 != VisualGeometry.NO_POINT \
                 and self.vertex4 == VisualGeometry.NO_POINT:
                x, y = self.vertex3.x, self.vertex3.y
                self.vertex4 = Point(x, y + 10)
        elif ch == 'H' or ch == 'h':
            if self.vertex1 != VisualGeometry.NO_POINT \
               and self.vertex2 == VisualGeometry.NO_POINT:
                x, y = self.vertex1.x, self.vertex1.y
                self.vertex2 = Point(x + 10, y)
            elif self.vertex3 != VisualGeometry.NO_POINT \
                 and self.vertex4 == VisualGeometry.NO_POINT:
                x, y = self.vertex3.x, self.vertex3.y
                self.vertex4 = Point(x + 10, y)
        else:
            print("Unrecognized key pressed")
        self.repaint()


def main():
    """ Execute the graphical application. """
    VisualGeometry()


if __name__ == '__main__':
    main()

