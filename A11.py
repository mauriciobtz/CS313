#  File: Triangle.py 100/100

#  Description: using different algorithmic approaches to find the greatest path sum in a triangle

#  Student Name: Mauricio Benitez

#  Course Name: CS 313E

#  Date Created: March 28, 2021

#  Date Last Modified: March 30, 2021

import sys

from timeit import timeit


# returns the greatest path sum using exhaustive search
def brute_force(grid):
    memo = []  # uses memoization to get the maximum of all of the path sums
    brute_helper(memo, 0, 0, 0, grid)
    return (max(memo))


def brute_helper(memo, greatest_sum, idx, inner_loop, grid):
    if idx >= len(grid):  # base case checks if it reached the last of the triangle
        return memo.append(greatest_sum)
    else:
        greatest_sum += grid[idx][inner_loop]  # keeps a tab of the sum and adds the next number

        return (brute_helper(memo, greatest_sum, idx + 1, inner_loop,
                             grid) or  # the idx and index moves along the triangle
                brute_helper(memo, greatest_sum, idx + 1, inner_loop + 1, grid))


# returns the greatest path sum using greedy approach
def greedy(grid):
    index = 0
    greatest_sum = 0

    for rows in range(len(grid) - 1):
        greatest_sum += grid[rows][index]

        if (grid[rows + 1][index] > grid[rows + 1][index + 1]):  # index moves along the triangle
            index = index
        else:
            index = index + 1

    greatest_sum += grid[rows + 1][index]
    return greatest_sum


# returns the greatest path sum using divide and conquer (recursive) approach
def divide_conquer(grid):
    return divide_conquer_helper(grid, 0, 0, 0)  # calls a helper function


# helper function for divide_conquer
def divide_conquer_helper(grid, path_sum, idx, inner_loop):
    # base case checks if we reached the end of the triangle
    if idx >= len(grid):
        return path_sum

    else:

        path_sum += grid[idx][inner_loop]

        return max((divide_conquer_helper(grid, path_sum, idx + 1, inner_loop),
                    # using and / or did not yield the right results
                    divide_conquer_helper(grid, path_sum, idx + 1,
                                          inner_loop + 1)))  # so we return the max of either recursion


# returns the greatest path sum and the new grid using dynamic programming
def dynamic_prog(grid):
    total_grid = []
    for rows in range(len(grid) - 2, 0,
                      -1):  # goes bottom-up in reverse starting at the last row / 0 end bc it's not inclusive
        # loops through individual numbers in each row
        for col in range(len(grid[rows]) - 1):
            local_max = max(grid[rows][col] + grid[rows + 1][col],
                            grid[rows][col] + grid[rows + 1][col + 1])
            grid[rows][col] = (local_max)

    # had to return a sum because the outer loop stop is not inclusive
    return (max(grid[0][0] + grid[1][1], grid[0][0] + grid[1][0]))


# reads the file and returns a 2-D list that represents the triangle
def read_file():
    # read number of lines
    line = sys.stdin.readline()
    line = line.strip()
    n = int(line)

    # create an empty grid with 0's
    grid = [[0 for i in range(n)] for j in range(n)]

    # read each line in the input file and add to the grid
    for i in range(n):
        line = sys.stdin.readline()
        line = line.strip()
        row = line.split()
        row = list(map(int, row))
        for j in range(len(row)):
            grid[i][j] = grid[i][j] + row[j]

    return grid


def main():
    # read triangular grid from file
    grid = read_file()

    # check that the grid was read in properly
    # print (grid)

    # output greatest path from exhaustive search
    times = timeit('brute_force({})'.format(grid), 'from __main__ import brute_force', number=10)
    times = times / 10
    # print time taken using exhaustive search
    print("The greatest path sum through exhaustive search is ", brute_force(grid))
    print("The time taken for exhaustive search in seconds is ", times)

    # output greatest path from greedy approach
    # times = timeit ('greedy({})'.format(grid), 'from __main__ import greedy', number = 10)
    # times = times / 10
    # print time taken using greedy approach
    print("The greatest path sum through greedy search is ", greedy(grid))
    print("The time taken for greedy approach in seconds is ", times)

    # output greatest path from divide-and-conquer approach
    times = timeit('divide_conquer({})'.format(grid), 'from __main__ import divide_conquer', number=10)
    times = times / 10
    # print time taken using divide-and-conquer approach
    print("The greatest path sum through recursive search is ", divide_conquer(grid))
    print("The time taken for recursive search in seconds is", times)

    # output greatest path from dynamic programming
    times = timeit('dynamic_prog({})'.format(grid), 'from __main__ import dynamic_prog', number=10)
    times = times / 10
    # print time taken using dynamic programming

    print("The greatest path sum through dynamic programming is ", dynamic_prog(grid))
    print("The time taken for dynamic programming in seconds is ", times)


if __name__ == "__main__":
    main()