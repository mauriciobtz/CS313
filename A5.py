
#  File: OfficeSpace.py 100/100

#  Description: This program is a system for requesting office space

#  Student Name: Mauricio Benitez

#  Partner UT EID: mrg3688

#  Course Name: CS 313E

#  Date Created: Feb 23, 2021

#  Date Last Modified: Feb 26, 2021

import sys

#Function will take the coordinates of the rect and apply it to the lxw formula to find area
def area(rect):
    x1 = rect[0]
    y1 = rect[1]
    x2 = rect[2]
    y2 = rect[3]
    area = (y2 - y1) * (x2 - x1)
    return area

#Function checks if rectangles overlap; then it goes into an if, else statement and returns a tuple with coordinates
def overlap (rect1, rect2):
    # def intersects(rect1, rect2):
    #Create vertices (top right & bottom left) to compare
    bottom_left_1 = rect1[0:2]
    top_right_1 = rect1[2:4]
    bottom_left_2 = rect2[0:2]
    top_right_2 = rect2[2:4]
    # top_left_2 = top_right_1
    # top_left_2[0] = bottom_left_1[0]
    # print(top_left_2)
    x = 0
    y = 1
    #This will return True or False if squares overlap by checking if the intersection lies between a certain index
    ck_intersect =  not (top_right_1[x] <= bottom_left_2[x] or bottom_left_1[x] >= top_right_2[x] or top_right_1[y] <= bottom_left_2[y] or bottom_left_1[y] >= top_right_2[y])
    print(ck_intersect)
    if ck_intersect == False:
        return (0,0,0,0)
    else:
        # #This calculates the bottom X coordinate of the overlap by checking if the intersection lies between a certain index
        if rect2[3] >= rect1[1] and rect2[3] <= rect1[3] and (rect1[0] <= rect2[0] < rect1[2]):
            bottom_overlap_x = rect2[0]
        elif rect2[3] >= rect1[1] and rect2[3] <= rect1[3] and (rect2[0] <= rect1[0] <= rect2[2]):
            bottom_overlap_x = rect1[0]
        elif rect1[3] >= rect2[1] and rect1[3] <= rect2[3] and (rect1[0] <= rect2[0] < rect1[2]):
            bottom_overlap_x = rect2[0]
        elif rect1[3] >= rect2[1] and rect1[3] <= rect2[3] and (rect2[0] <= rect1[0] <= rect2[2]):
            bottom_overlap_x = rect1[0]

        #This calculates the bottom Y coordinate of the overlap by checking if the intersection lies between a certain index
        if rect1[3] >= rect2[1] and rect1[3] <= rect2[3] and (rect1[0] <= rect2[0] <= rect1[2]):
            bottom_overlap_y = max(rect1[1], rect2[1])
        elif rect1[3] >= rect2[1] and rect1[3] <= rect2[3] and (rect2[0] <= rect1[0] <= rect2[2]):
            bottom_overlap_y = max(rect1[1], rect2[1])
        elif rect2[3] >= rect1[1] and rect2[3] <= rect1[3] and (rect2[0] <= rect1[0] <= rect2[2]):
            bottom_overlap_y = max(rect1[1], rect2[1])
        elif rect2[3] >= rect1[1] and rect2[3] <= rect1[3] and (rect1[0] <= rect2[0] <= rect1[2]):
            bottom_overlap_y = max(rect1[1], rect2[1])
        elif rect2[1] <= rect1[1] and rect2[3] <= rect1[3] and (rect1[0] <= rect2[0] <= rect1[2]):
            bottom_overlap_y = max(rect1[1], rect2[1])

    #This calculates the top X coordinate of the overlap by checking if the intersection lies between a certain index
        if rect2[3] >= rect1[1] and rect2[3] <= rect1[3] and (rect2[0] <= rect1[2] <= rect2[2]):
            top_overlap_x = rect1[2]
        elif rect2[3] >= rect1[1] and rect2[3] <= rect1[3] and (rect1[0] <= rect2[2] <= rect1[2]):
            top_overlap_x = rect2[2]
        elif rect1[3] >= rect2[1] and rect1[3] <= rect2[3] and (rect2[0] <= rect1[2] <= rect2[2]):
            top_overlap_x = rect1[2]
        elif rect1[3] >= rect2[1] and rect1[3] <= rect2[3] and (rect1[0] <= rect2[2] < rect1[2]):
            top_overlap_x = rect2[2]

    # This calculates the top Y coordinate of the overlap by checking if the intersection lies between a certain index
        if rect1[3] >= rect2[1] and rect1[3] <= rect2[3] and (rect1[0] <= rect2[0] < rect1[2] or rect2[0] <= rect1[0] <= rect2[2]):
            top_overlap_y = rect1[3]
        elif rect2[3] >= rect1[1] and rect2[3] <= rect1[3] and (rect1[0] <= rect2[0] < rect1[2] or rect2[0] <= rect1[0] <= rect2[2]):
            top_overlap_y = rect2[3]

        return (bottom_overlap_x, bottom_overlap_y, top_overlap_x, top_overlap_y)


# Input: bldg is a 2-D array representing the whole office space
# Output: a single integer denoting the area of the unallocated
#         space in the office
def unallocated_space(bldg):
    unallocated_counter = 0
    for i in range(len(bldg)):
        for j in range(len(bldg[0])):
            if bldg[i][j] == 0:
                unallocated_counter += 1
    return unallocated_counter


# Input: bldg is a 2-D array representing the whole office space
# Output: a single integer denoting the area of the contested
#         space in the office
def contested_space(bldg):
    contested_counter = 0
    for i in range(len(bldg)):
        for j in range(len(bldg[0])):
            if bldg[i][j] > 1:
                contested_counter += 1
    return contested_counter


# Input: bldg is a 2-D array representing the whole office space
#        rect is a rectangle in the form of a tuple of 4 integers
#        representing the cubicle requested by an employee
# Output: a single integer denoting the area of the uncontested
#         space in the office that the employee gets
def uncontested_space(bldg, rect):
    uncontested_counter = 0
    for i in range(rect[1], rect[3]):
        for j in range(rect[2], rect[4]):
            if bldg[i][j] == 1:
                uncontested_counter += 1
    return uncontested_counter


# Input: office is a rectangle in the form of a tuple of 4 integers
#        representing the whole office space
#        cubicles is a list of tuples of 4 integers representing all
#        the requested cubicles
# Output: a 2-D list of integers representing the office building and
#         showing how many employees want each cell in the 2-D list
def request_space(office, cubicles):
    office_space = [[0 for i in range(office[3])] for j in range(office[2])]

    for item in cubicles:
        for a in range(item[1], item[3]):
            for b in range(item[2], item[4]):
                office_space[a][b] += 1

    return office_space


def main():
    # read the data
    office_size = []
    office_size = sys.stdin.readline().split()
    w = int(office_size[0])
    h = int(office_size[1])
    # print(office_size)

    # tuple representing the office rectangle
    # what will be used as an argument for the functions

    rectangle = (0, 0, w, h)

    num_requests = int(sys.stdin.readline().strip())

    employees_list = []

    for line in sys.stdin.readlines():
        curr_employee = []
        curr_employee = line.split()
        curr_employee[1] = int(curr_employee[1])
        curr_employee[2] = int(curr_employee[2])
        curr_employee[3] = int(curr_employee[3])
        curr_employee[4] = int(curr_employee[4])

        employees_list.append(tuple(curr_employee))

    # print the following results after computation

    # compute the total office space
    print("Total", area(rectangle))
    # compute the total unallocated space
    building = request_space(rectangle, employees_list)

    unallocated = unallocated_space(building)
    print("Unallocated", unallocated)

    # compute the total contested space
    contested = contested_space(building)
    print("Contested", contested)

    # compute the uncontested space that each employee gets
    for item in employees_list:
        print(item[0], uncontested_space(building, item))


if __name__ == "__main__":
    main()