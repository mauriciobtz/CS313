#  File: Spiral.py 100/100

#  Description: This headache of a program creates a spiral and then returns sums of adjacent values

#  Name: Mauricio Benitez

#  Course Name: CS 313E

#  Date Created: January 26, 2021

#  Date Last Modified: January 31, 2021


from itertools import count
from collections import namedtuple
from math import sqrt, ceil
import sys


def create_spiral(n):
    # create variables and empty matrix
    size_matrix = n
    lenSpiral = int(size_matrix ** 2)
    matrix = []

    # creates an 11 x 11 list with blanks to be filled with later algorithm
    for i in range(size_matrix):
        a = ['  '] * (size_matrix)
        matrix.append(a)

    # This tuple creates the movement of the spiral and is used in function turns()
    move = namedtuple("move", ["fx", "fy"])
    RIGHT = move(1, 0)
    LEFT = move(-1, 0)
    DOWN = move(0, 1)
    UP = move(0, -1)

    # this function checks to see if it's an even/odd number and moves accordingly
    def turns():
        for n in count(start=1):
            if n % 2:
                yield RIGHT
                for i in range(n):
                    yield DOWN
                for i in range(n):
                    yield LEFT
            else:
                yield LEFT
                for i in range(n):
                    yield UP
                for i in range(n):
                    yield RIGHT

    # this function converts the item from int to str
    def output(item):
        return str(item)

    # start matrix by putting a 1 in the center:
    x = y = (size_matrix // 2)
    matrix[y][x] = output(1)

    for i, move in enumerate(turns(), start=2):
        if i > lenSpiral:
            break
        else:
            x += move.fx
            y += move.fy
            matrix[y][x] = output(i)

    return matrix


def sum_adjacent_numbers(matrix, n, lookup):
    # creates a tuple of all of the coordinates of each value
    indexes = [(i, j) for i, nl in enumerate(matrix) for j, nle in enumerate(nl)]
    # print(indexes, sep="\n")

    # for lookup_num in lookup_list:
    num = lookup

    # find the x, y coordinates of value
    def find_coor(num):
        for x, point in enumerate(matrix):
            try:
                y = point.index(num)
            except ValueError:
                continue
            yield x, y

    # We then use the coordinates of the value to calculate surrounding values and append to list values = []
    for value in find_coor(num):
        x, y = value
        # print(x,y)
        values = []

        if x == 0 and y == n - 1:  # Top Right Corner (121)
            values.append(matrix[x + 1][y])  # down
            values.append(matrix[x][y - 1])  # left
            values.append(matrix[x + 1][y - 1])  # one down one left
        elif x == n - 1 and y == n - 1:  # Bottom Right Corner (91)
            values.append(matrix[x][y - 1])  # left
            values.append(matrix[x - 1][y])  # up
            values.append(matrix[x - 1][y - 1])  # one left one up
        elif x == 0 and y == 0:  # Top Left Corner (111)
            values.append(matrix[x][y + 1])  # right
            values.append(matrix[x + 1][y])  # down
            values.append(matrix[x + 1][y + 1])  # one down one right
        elif x == n - 1 and y == 0:  # Bottom Left Corner (101)
            values.append(matrix[x][y + 1])  # right
            values.append(matrix[x - 1][y])  # up
            values.append(matrix[x - 1][y + 1])  # up and right
        elif x == 0:  # All values at top
            values.append(matrix[x][y + 1])  # right
            values.append(matrix[x + 1][y + 1])  # one down one right
            values.append(matrix[x + 1][y])  # down
            values.append(matrix[x + 1][y - 1])  # one down one left
            values.append(matrix[x][y - 1])  # left
        elif x == n - 1:  # All values on bottom
            values.append(matrix[x][y - 1])  # left
            values.append(matrix[x - 1][y - 1])  # one left one up
            values.append(matrix[x - 1][y])  # up
            values.append(matrix[x - 1][y + 1])  # up and right
            values.append(matrix[x][y + 1])  # right
        elif y == 0:  # All vavlues on left
            values.append(matrix[x - 1][y])  # up
            values.append(matrix[x - 1][y + 1])  # up and right
            values.append(matrix[x][y + 1])  # right
            values.append(matrix[x + 1][y + 1])  # one down one right
            values.append(matrix[x + 1][y])  # down
        elif y == n - 1:  # All values on right
            values.append(matrix[x + 1][y])  # down
            values.append(matrix[x + 1][y - 1])  # one down one left
            values.append(matrix[x][y - 1])  # left
            values.append(matrix[x - 1][y - 1])  # one left one up
            values.append(matrix[x - 1][y])  # up
        else:  # ALL 'REGULAR' values in middle
            values.append(matrix[x][y + 1])  # right
            values.append(matrix[x + 1][y + 1])  # one right one down
            values.append(matrix[x + 1][y])  # down
            values.append(matrix[x + 1][y - 1])  # one down one left
            values.append(matrix[x][y - 1])  # left
            values.append(matrix[x - 1][y - 1])  # one left one up
            values.append(matrix[x - 1][y])  # up
            values.append(matrix[x - 1][y + 1])  # up and right

        # Changes values to integers
        for i in range(0, len(values)):
            values[i] = int(values[i])

        # Adds and prints the SUM of integers in the list values
        sum_of_values = sum(values)
        print(sum_of_values)
        return sum_of_values


def main():
    size_matrix = int(sys.stdin.readline().strip())

    # this ensures the dimensions of the spirals are odd numbers
    if (size_matrix % 2) == 0:
        size_matrix += 1
    else:
        size_matrix = size_matrix

    txt_list = []  # this is gonna store the numbers who adjacent sums we have to find

    for line in sys.stdin.readlines():
        num = line.strip()
        txt_list.append(num)

    matrix = create_spiral(size_matrix)  # captures the list of the spiral and stores into a variable

    for number_to_lookup in range(len(txt_list)):
        if int(txt_list[number_to_lookup]) > 0 and int(txt_list[number_to_lookup]) < size_matrix ** 2:
            sum_adjacent_numbers(matrix, size_matrix,
                                 txt_list[number_to_lookup])  # passing returned spiral and stdin into arguments
        else:
            print(0)


# if __name__ == "__main__":

main()