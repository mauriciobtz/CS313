#  File: Hull.py 100/100

#  Description: Given a set of points, outputs the points that compose the convex hull

#  Student Name: Mauricio Benitez

#  Course Name: CS 313E

#  Date Created: February 27, 2021

#  Date Last Modified: March 1, 2021

import sys

import math


class Point(object):
    # constructor
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # get the distance to another Point object
    def dist(self, other):
        return math.hypot(self.x - other.x, self.y - other.y)

    # string representation of a Point
    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    # equality tests of two Points
    def __eq__(self, other):
        tol = 1.0e-8
        return ((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol))

    def __ne__(self, other):
        tol = 1.0e-8
        return ((abs(self.x - other.x) >= tol) or (abs(self.y - other.y) >= tol))

    def __lt__(self, other):
        tol = 1.0e-8
        if (abs(self.x - other.x) < tol):
            if (abs(self.y - other.y) < tol):
                return False
            else:
                return (self.y < other.y)
        return (self.x < other.x)

    def __le__(self, other):
        tol = 1.0e-8
        if (abs(self.x - other.x) < tol):
            if (abs(self.y - other.y) < tol):
                return True
            else:
                return (self.y <= other.y)
        return (self.x <= other.x)

    def __gt__(self, other):
        tol = 1.0e-8
        if (abs(self.x - other.x) < tol):
            if (abs(self.y - other.y) < tol):
                return False
            else:
                return (self.y > other.y)
        return (self.x > other.x)

    def __ge__(self, other):
        tol = 1.0e-8
        if (abs(self.x - other.x) < tol):
            if (abs(self.y - other.y) < tol):
                return True
            else:
                return (self.y >= other.y)
        return (self.x >= other.x)


# Input: p, q, r are Point objects
# Output: compute the determinant and return the value
def det(p, q, r):
    # determinant formula
    return (p.x * q.y + q.x * r.y + p.y * r.x - p.x * r.y - p.y * q.x - q.y * r.x)


# Input: sorted_points is a sorted list of Point objects
# Output: computes the convex hull of a sorted list of Point objects
#         convex hull is a list of Point objects starting at the
#         extreme left point and going clockwise in order
#         returns the convex hull
def convex_hull(sorted_points):
    sorted_points.sort()
    upper_hull = []
    upper_hull.append(sorted_points[0])
    upper_hull.append(sorted_points[1])

    for i in range(2, len(sorted_points)):
        upper_hull.append(sorted_points[i])
        # removes points engulfed by the convex, so only vertices are output
        while ((len(upper_hull) >= 3) and det(upper_hull[-3], upper_hull[-2], upper_hull[-1]) >= 0):
            upper_hull.pop(-2)

    lower_hull = []
    lower_hull.append(sorted_points[-1])
    lower_hull.append(sorted_points[-2])

    for i in range(len(sorted_points) - 3, -1, -1):  # iterating through the list backwards
        lower_hull.append(sorted_points[i])

        while ((len(lower_hull) >= 3) and det(lower_hull[-3], lower_hull[-2], lower_hull[-1]) >= 0):
            lower_hull.pop(-2)

    lower_hull.pop(0)
    lower_hull.pop(-1)
    convex_hull = upper_hull + lower_hull  # combines the hulls
    return convex_hull


# Input: convex_poly is  a list of Point objects that define the
#        vertices of a convex polygon in order
# Output: computes and returns the area of a convex polygon
def area_poly(convex_poly):
    running_determinant_pos = 0
    for i in range(len(convex_poly)):
        if convex_poly[i] != convex_poly[-1]:  # making sure the current point isn't the last
            running_determinant_pos += convex_poly[i].x * convex_poly[i + 1].y
        else:  # when it's the last point, the determinant pattern changes
            running_determinant_pos += convex_poly[-1].x * convex_poly[0].y

    # this part gets the negative part of the determinant
    running_determinant_neg = 0
    for i in range(len(convex_poly)):
        if convex_poly[i] != convex_poly[-1]:
            running_determinant_pos -= convex_poly[i + 1].x * convex_poly[i].y  # im having trouble referencing
        else:
            running_determinant_pos -= convex_poly[0].x * convex_poly[-1].y

    det = running_determinant_pos + running_determinant_neg
    return (1 / 2) * abs(det)


def main():
    # create an empty list of Point objects
    points_list = []

    # read number of points
    line = sys.stdin.readline()
    line = line.strip()
    num_points = int(line)

    # read data from standard input
    for i in range(num_points):
        line = sys.stdin.readline()
        line = line.strip()
        line = line.split()
        x = int(line[0])
        y = int(line[1])
        points_list.append(Point(x, y))

    # sort the list according to x-coordinates
    sorted_points = sorted(points_list)

    # get the convex hull
    convex = convex_hull(sorted_points)

    # print the convex hull
    print("Convex Hull")

    for p in convex:
        print(p)

    # get the area of the convex hull
    print('')
    area = area_poly(convex)
    # print the area of the convex hull
    print("Area of Convex Hull =", area)


if __name__ == "__main__":
    main()