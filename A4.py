#  File: Geometry.py 77/100

#  Description: Thinking of objects in 3D while practicing inheritance

#  Student Name: Mauricio Benitez

#  Student UT EID: mrg3688

#  Course Name: CS 313E

#  Date Created: February 9, 2021

#  Date Last Modified: February 12, 2021

import math
import sys


class Point(object):
    # constructor with default values
    def __init__(self, x=0, y=0, z=0):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    # get the distance to another Point object
    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2)

    # string representation of a Point
    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ', ' + str(self.z) + ')'

    # test for equality of two Point objects
    def __eq__(self, other):
        tol = 1.0e-6
        return ((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol) and (abs(self.z - other.z < tol)))


class Sphere(object):
    # sphere constructor
    def __init__(self, x=0, y=0, z=0, radius=1):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
        self.radius = float(radius)
        self.center = Point(x, y, z)

    # string representation of a sphere
    def __str__(self):
        return "Center: " + '(' + str(self.center.x) + ', ' + str(self.center.y) + ', ' + str(
            self.center.z) + '), ' + "Radius: " + str(
            self.radius)

    # area of a sphere
    def area(self):
        return 4 * math.pi * self.radius ** 2

    def volume(self):
        return (4 / 3) * math.pi * self.radius ** 3

    # checks if a point is inside a sphere
    def is_inside_point(self, p):
        return self.center.distance(p) < self.radius

    # checks is a sphere is inside another sphere
    def is_inside_sphere(self, other):
        return self.center.distance(other.center) + other.radius < self.radius

    # checks if a cube is inside a sphere by finding the points of all vertices of a cube
    # and checking if each point is within the sphere
    def is_inside_cube(self, a_cube):
        v1 = Point(a_cube.center.x + a_cube.side / 2, a_cube.center.y - a_cube.side / 2,
                   a_cube.center.z + a_cube.side / 2)
        v2 = Point(a_cube.center.x + a_cube.side / 2, a_cube.center.y + a_cube.side / 2,
                   a_cube.center.z + a_cube.side / 2)

        v3 = Point(a_cube.center.x - a_cube.side / 2, a_cube.center.y + a_cube.side / 2,
                   a_cube.center.z + a_cube.side / 2)
        v4 = Point(a_cube.center.x - a_cube.side / 2, a_cube.center.y - a_cube.side / 2,
                   a_cube.center.z + a_cube.side / 2)

        v5 = Point(a_cube.center.x + a_cube.side / 2, a_cube.center.y + a_cube.side / 2,
                   a_cube.center.z - a_cube.side / 2)
        v6 = Point(a_cube.center.x + a_cube.side / 2, a_cube.center.y - a_cube.side / 2,
                   a_cube.center.z - a_cube.side / 2)

        v7 = Point(a_cube.center.x - a_cube.side / 2, a_cube.center.y - a_cube.side / 2,
                   a_cube.center.z - a_cube.side / 2)
        v8 = Point(a_cube.center.x - a_cube.side / 2, a_cube.center.y + a_cube.side / 2,
                   a_cube.center.z - a_cube.side / 2)

        v_lst = [v1, v2, v3, v4, v5, v6, v7, v8]
        for v in v_lst:
            if self.is_inside_point(v) == False:
                return False
                # break

            else:
                return True

    # checks if a cylinder is inside a sphere by putting the cylinder in a box
    def is_inside_cyl(self, a_cyl):
        boxed_vertices = a_cyl.boxed_cyl_vertices()

        for v in boxed_vertices:
            if self.is_inside_point(v) == False:
                return False
                # break

            else:
                return True

    # checks if a sphere intersects another sphere
    # by putting sphereb in a box
    # and plotting the vertices
    def does_intersect_sphere(self, other):
        boxed_sphere = Cube(other.center.x, other.center.y, other.center.z, other.radius * 2)
        boxed_sphere_vertices = boxed_sphere.find_vertices()

        for v in boxed_sphere_vertices:
            if self.is_inside_point(v) == False:
                return True
                # break

            else:
                return False

    # checks if a cube intersects a sphere
    # same logic as the previous function
    def does_intersect_cube(self, a_cube):  # put sphere in a box

        a_cube_vertices = a_cube.find_vertices()

        for v in a_cube_vertices:
            if self.is_inside_point(v) == False:
                return True
                # break

            else:
                return False

    def circumscribe_cube(self):  # radius of the sphere is half the diagonal of the cube
        # diagonal = self.radius * 2
        # side = self.radius * 2
        return Cube(self.center.x, self.center.y, self.center.z, self.radius * 2)


class Cube(object):
    # Cube is defined by its center (which is a Point object)
    # and side. The faces of the Cube are parallel to x-y, y-z,
    # and x-z planes.
    def __init__(self, x=0, y=0, z=0, side=1):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
        self.center = Point(x, y, z)
        self.side = float(side)

    # string representation of a Cube of the form:
    # Center: (x, y, z), Side: value
    def __str__(self):
        return "Center: " + '(' + str(self.center.x) + ', ' + str(self.center.y) + ', ' + str(
            self.center.z) + '), ' + "Side: " + str(self.side)

    # compute the total surface area of Cube (all 6 sides)
    def area(self):
        return 6 * self.side ** 2

    # compute volume of a Cube
    def volume(self):
        return self.side ** 3

    def find_vertices(self):
        vFRU = Point(self.center.x + (self.side / 2), self.center.y - (self.side / 2), self.center.z + (self.side / 2))
        vBRU = Point(self.center.x + (self.side / 2), self.center.y + (self.side / 2), self.center.z + (self.side / 2))

        vFLU = Point(self.center.x - (self.side / 2), self.center.y + (self.side / 2), self.center.z + (self.side / 2))
        vBLU = Point(self.center.x - (self.side / 2), self.center.y - (self.side / 2), self.center.z + (self.side / 2))

        vFRD = Point(self.center.x + (self.side / 2), self.center.y + (self.side / 2), self.center.z - (self.side / 2))
        vBRD = Point(self.center.x + (self.side / 2), self.center.y - (self.side / 2), self.center.z - (self.side / 2))

        vFLD = Point(self.center.x - (self.side / 2), self.center.y - (self.side / 2), self.center.z - (self.side / 2))
        vBLD = Point(self.center.x - (self.side / 2), self.center.y + (self.side / 2), self.center.z - (self.side / 2))

        vertices_list = [vFRU, vBRU, vFLU, vBLU, vFRD, vBRD, vFLD, vBLD]
        return vertices_list

    # determines if a Point is strictly inside this Cube
    # p is a point object
    # returns a Boolean
    def is_inside_point(self, p):

        if self.center.x + self.side / 2 > p.x > self.center.x - self.side / 2:
            if self.center.y + self.side / 2 > p.y > self.center.y - self.side / 2:
                if self.center.z + self.side / 2 > p.z > self.center.z - self.side / 2:
                    return True

        return False

    def is_inside_sphere(self, a_sphere):
        # This creates the max/min of the cube
        cube_max_x = self.center.x + (.5 * self.side)
        cube_max_y = self.center.y + (.5 * self.side)
        cube_max_z = self.center.z + (.5 * self.side)
        cube_min_x = self.center.x - (.5 * self.side)
        cube_min_y = self.center.y - (.5 * self.side)
        cube_min_z = self.center.z - (.5 * self.side)

        # This creates the max/min of the SPHERE
        x_max = a_sphere.center.x + a_sphere.radius
        y_max = a_sphere.center.y + a_sphere.radius
        z_max = a_sphere.center.z + a_sphere.radius
        x_min = a_sphere.center.x - a_sphere.radius
        y_min = a_sphere.center.y - a_sphere.radius
        z_min = a_sphere.center.z - a_sphere.radius

        # As long as the max value of cube are larger than max of sphere and the min value of cube is smaller than sphere; return boolean
        return (cube_max_x > x_max) and (cube_min_x < x_min) and (cube_max_y > y_max) and (cube_min_y < y_min) and (
                    cube_max_z > z_max) and (cube_min_z < z_min)

        # determine if another Cube is strictly inside this Cube
        # other is a Cube object
        # returns a Boolean

    def is_inside_cube(self, other):
        # This creates the max/min of the cube
        cube_max_x = self.center.x + (.5 * self.side)
        cube_max_y = self.center.y + (.5 * self.side)
        cube_max_z = self.center.z + (.5 * self.side)
        cube_min_x = self.center.x - (.5 * self.side)
        cube_min_y = self.center.y - (.5 * self.side)
        cube_min_z = self.center.z - (.5 * self.side)

        # This creates the max/min of the SPHERE
        cube2_max_x = other.center.x + (.5 * other.side)
        cube2_max_y = other.center.y + (.5 * other.side)
        cube2_max_z = other.center.z + (.5 * other.side)
        cube2_min_x = other.center.x - (.5 * other.side)
        cube2_min_y = other.center.y - (.5 * other.side)
        cube2_min_z = other.center.z - (.5 * other.side)

        # As long as the max value of cube are larger than max of sphere and the min value of cube is smaller than sphere; return boolean
        return (cube_max_x > cube2_max_x) and (cube_min_x < cube2_min_x) and (cube_max_y > cube2_max_y) and (
                    cube_min_y < cube2_min_y) and (cube_max_z > cube2_max_z) and (cube_min_z < cube2_min_z)

    def is_outside_cube(self, other):

        other_vertices = other.find_vertices()
        for v in other_vertices:
            if self.is_inside_point(v) == True:
                return True
                # break

            else:
                return False

    def does_intersect_cube(self, other):
        return self.is_inside_cube(other) == False and self.is_outside_cube(other) == False

    def is_inside_cylinder(self, a_cyl):
        boxed_vertices = a_cyl.boxed_cyl_vertices()

        for v in boxed_vertices:
            if self.is_inside_point(v) == False:
                return False
                # break

            else:
                return True

    # def intersection_volume (self, other):

    def inscribe_sphere(self):
        d = self.side * math.sqrt(3)
        largest_radius = d / 2
        return Sphere(self.center.x, self.center.y, self.center.z, largest_radius)


class Cylinder(object):

    # Cylinder is defined by its center (which is a Point object),
    # radius and height. The main axis of the Cylinder is along the
    # z-axis and height is measured along this axis
    def __init__(self, x=0, y=0, z=0, radius=1, height=1):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
        self.center = Point(x, y, z)
        self.radius = float(radius)
        self.height = float(height)

    # returns a string representation of a Cylinder of the form:
    # Center: (x, y, z), Radius: value, Height: value
    def __str__(self):
        return "Center: " + '(' + str(self.x) + ', ' + str(self.y) + ', ' + str(self.z) + '), Radius: ' + str(
            self.radius) + ', Height: ' + str(
            self.height)

    # compute surface area of Cylinder
    # returns a floating point number
    def area(self):
        return (2 * math.pi * self.radius) * (self.radius + self.height)

    # compute volume of a Cylinder
    # returns a floating point number
    def volume(self):
        return math.pi * self.height * self.radius ** 2

    # determine if a Point is strictly inside this Cylinder
    # p is a Point object
    # returns a Boolean
    def is_inside_point(self, p):
        z_max = self.center.z + (self.height / 2)
        z_min = self.center.z - (self.height / 2)

        cyl_axis = Point(self.center.x, self.center.y, p.z)
        return z_max > p.z > z_min and Point.distance(cyl_axis, p) < self.radius

    # determine if a Sphere is strictly inside this Cylinder
    # a_sphere is a Sphere object
    # returns a Boolean
    def is_inside_sphere(self, a_sphere):
        # d = self.side * math.sqrt(3)
        # largest_radius = d / 2
        # return Sphere(self.center.x, self.center.y, self.center.z, largest_radius)

        a_box = Cube(a_sphere.center.x, a_sphere.center.y, a_sphere.center.z, a_sphere.radius)
        box_vertices = a_box.find_vertices()  # would it know the function is from the cube class?

        for v in box_vertices:
            if self.is_inside_point(v) == True:
                return False
                # break

            else:
                return True

    # determine if a Cube is strictly inside this Cylinder
    # determine if all eight corners of the Cube are inside
    # the Cylinder
    # a_cube is a Cube object
    # returns a Boolean
    def is_inside_cube(self, a_cube):
        cube_vertices = a_cube.find_vertices()  # would it know the function is from the cube class?

        for v in cube_vertices:
            if self.is_inside_point(v) == False:
                return False
                # break

            else:
                return True

    # determine if another Cylinder is strictly inside this Cylinder
    # other is Cylinder object
    # returns a Boolean
    def is_inside_cylinder(self, other):
        boxed_vertices = other.boxed_cyl_vertices()

        for v in boxed_vertices:
            if self.is_inside_point(v) == False:
                return False
                # break

            else:
                return True

    # determine if another Cylinder intersects this Cylinder
    # two Cylinder object intersect if they are not strictly
    # inside and not strictly outside each other
    # other is a Cylinder object
    # returns a Boolean
    def does_intersect_cylinder(self, other):
        return self.is_outside_cylinder == True and self.is_inside_cylinder == False

    def is_outside_cylinder(self, other):
        return self.is_inside_cylinder(other) == False and (
                abs(self.center.z - other.center.z) >= (self.height + other.height))

    # returns the points of the vertices when you put a cylinder in a box
    def boxed_cyl_vertices(self):

        vFRU = Point(self.center.x + self.radius, self.center.y - self.radius, self.center.z + self.height / 2)
        vBRU = Point(self.center.x + self.radius, self.center.y + self.radius, self.center.z + self.height / 2)

        vFLU = Point(self.center.x - self.radius, self.center.y + self.radius, self.center.z + self.height / 2)
        vBLU = Point(self.center.x - self.radius, self.center.y - self.radius, self.center.z + self.height / 2)

        vFRD = Point(self.center.x + self.radius, self.center.y + self.radius, self.center.z - self.height / 2)
        vBRD = Point(self.center.x + self.radius, self.center.y - self.radius, self.center.z - self.height / 2)

        vFLD = Point(self.center.x - self.radius, self.center.y - self.radius, self.center.z - self.height / 2)
        vBLD = Point(self.center.x - self.radius, self.center.y + self.radius, self.center.z - self.height / 2)

        vertices_list = [vFRU, vBRU, vFLU, vBLU, vFRD, vBRD, vFLD, vBLD]
        return vertices_list


def main():
    # read the coordinates of the first Point p
    Point_list = sys.stdin.readline().split(' ')  # gives a list of strings
    lst = [float(x) for x in Point_list]

    # create a Point object
    Point_p = Point(lst[0], lst[1], lst[2])

    # read the coordinates of the second Point q
    Point_list = sys.stdin.readline().split(' ')
    lst = [float(x) for x in Point_list]

    # create a point object
    Point_q = Point(lst[0], lst[1], lst[2])

    # read the coordinates of the center and radius of sphereA
    Sphere_list = sys.stdin.readline().split(' ')
    lst = [float(x) for x in Sphere_list]

    # create sphereA
    sphereA = Sphere(lst[0], lst[1], lst[2], lst[3])

    # read the coordinates of the center and radius of sphereB
    Sphere_list = sys.stdin.readline().split(' ')
    lst = [float(x) for x in Sphere_list]

    # create sphereB
    sphereB = Sphere(lst[0], lst[1], lst[2], lst[3])

    # read the coordinates of the center and side of cubeA
    Cube_list = sys.stdin.readline().split(' ')
    lst = [float(x) for x in Cube_list]

    # create cubeA
    cubeA = Cube(lst[0], lst[1], lst[2], lst[3])
    # print(cubeA)

    # read the coordinates of the center and side of cubeB
    Cube_list = sys.stdin.readline().split(' ')
    lst = [float(x) for x in Cube_list]

    # create cube B
    cubeB = Cube(lst[0], lst[1], lst[2], lst[3])

    # read the coordinates of the center, radius and height of cylA
    Cyl_list = sys.stdin.readline().split(' ')
    lst = [float(x) for x in Cyl_list]

    # create a Cylinder object
    cylA = Cylinder(lst[0], lst[1], lst[2], lst[3], lst[4])

    # read the coordinates of the center, radius and height of cylB
    Cyl_list = sys.stdin.readline().split(' ')
    lst = [float(x) for x in Cyl_list]

    # create a Cylinder object
    cylB = Cylinder(lst[0], lst[1], lst[2], lst[3], lst[4])

    # print if the distance of p from the origin is greater
    # than the distance of q from the origin
    origin = Point(0, 0, 0)

    if origin.distance(Point_p) > origin.distance(Point_q):
        print("Distance of Point p from the origin is greater than the distance of Point q from the origin")
    else:
        print("Distance of Point p from the origin is not greater than the distance of Point q from the origin")

    # print if Point p is inside sphereA
    if sphereA.is_inside_point(Point_p) == True:
        print("Point p is inside sphereA")
    else:
        print("Point is not inside sphereA")

    # print if sphereB is inside sphereA
    if sphereA.is_inside_sphere(sphereB) == True:
        print("sphereB is inside sphereA")
    else:
        print("sphereB is not inside sphereA")

    # print if cubeA is inside sphereA
    if sphereA.is_inside_cube(cubeA) == True:
        print("cubeA is inside sphereA")
    else:
        print("cubeA is not inside sphereA")

    # print if cylA is inside sphereA
    if sphereA.is_inside_cyl(cylA) == True:
        print("cylA is inside sphereA")
    else:
        print("cylA is not inside sphereA")

    # print if sphereA intersects with sphereB
    if sphereA.does_intersect_sphere(sphereB) == True:
        print("sphereA does not intersect sphereB")
    else:
        print("sphereA does intersect sphereB")

    # print if cubeB intersects with sphereB
    if sphereB.does_intersect_cube(cubeB) == True:
        print("cubeB does not intersect sphere")
    else:
        print("cubeB does intersect sphereB")

    # print if the volume of the largest Cube that is circumscribed
    # by sphereA is greater than the volume of cylA
    circum_cube = sphereA.circumscribe_cube()
    if circum_cube.volume() > cylA.volume():  # ask if this notation is correct
        print("Volume of the largest Cube that is circumscribed by sphereA is greater than the volume of cylA")
    else:
        print("Volume of the largest Cube that is circumscribed by sphereA is not greater than the volume of cylA")

    # print if Point p is inside cubeA
    if cubeA.is_inside_point(Point_p) == True:
        print("Point p is inside cubeA")
    else:
        print("Point p is not inside cubeA")

    # print if sphereA is inside cubeA
    if cubeA.is_inside_sphere(sphereA) == True:
        print("sphereA is inside cubeA")
    else:
        print("sphereA is not inside cubeA")

    # print if cubeB is inside cubeA
    if cubeA.is_inside_cube(cubeB) == True:
        print("cubeB is inside cubeA")
    else:
        print("cubeB is not inside cubeA")

    #  print if cylA is inside cubeA
    if cubeA.is_inside_cylinder(cylA) == True:
        print("cylA is inside cubeA")
    else:
        print("cylA is not inside cubeA")
    #
    # # print if cubeA intersects with cubeB
    if cubeA.is_inside_cube(cubeB) == False and cubeA.is_outside_cube(cubeB) == False:
        print("cubeA does intersect cubeB")
    else:
        print("cubeA does not intersect cubeB")

    # print if the intersection volume of cubeA and cubeB
    # is greater than the volume of sphereA

    # print if the surface area of the largest Sphere object inscribed
    # by cubeA is greater than the surface area of cylA
    cubic_sphere = cubeA.inscribe_sphere()
    if cubic_sphere.area() > cylA.area():
        print("Surface area of the largest Sphere object inscribed by cubeA is greater than the surface area of cylA")
    else:
        print(
            "Surface area of the largest Sphere object inscribed by cubeA is not greater than the surface area of cylA")

    # print if Point p is inside cylA
    if cylA.is_inside_point(Point_p):
        print("Point p is inside cylA")
    else:
        print("Point p is not inside cylA")

    # print if sphereA is inside cylA
    if cylA.is_inside_sphere(sphereA):
        print("sphereA is inside cylA")
    else:
        print("sphereA is not inside cylA")

    # print if cubeA is inside cylA
    if cylA.is_inside_cube(cubeA):
        print("cubeA is inside cylA")
    else:
        print("cubeA is not inside cylA")

    # print if cylB is inside cylA

    if cylA.is_inside_cylinder(cylB):
        print("cylB is inside cylA")
    else:
        print("cylB is not inside cylA")

    # print if cylB intersects with cylA
    if cylA.does_intersect_cylinder(cylB):
        print("cylB does intersect cylA")
    else:
        print("cylB does not intersect cylA")


if __name__ == "__main__":
    main()
