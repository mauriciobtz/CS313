#  File: Intervals.py 100/100

#  Description: Merges tuples and sorts them by size

#  Student Name: Mauricio Benitez

#  Course Name: CS 313E

#  Date Created: February 2, 2021

#  Date Last Modified: February 4, 2021

import sys


def merged_tuples(list_of_tuples):
    list_of_tuples.sort()

    merged_list = [list_of_tuples[0]]

    # iterates through the tuples list, and compares the end of the tuples list item
    # to the start of the last item in merged_list
    for item in range(1, len(list_of_tuples)):
        if merged_list[-1][1] >= list_of_tuples[item][0]:
            new_min = min(merged_list[-1][0], list_of_tuples[item][0])
            new_max = max(merged_list[-1][1], list_of_tuples[item][1])

            temp_tup_list = [new_min, new_max]

            # if there is overlap, it removes the last item of merged list before appending a new item
            merged_list.pop()
            merged_list.append(tuple(temp_tup_list))


        else:
            # if there is no overlap, the new item is appended
            merged_list.append(list_of_tuples[item])

    return merged_list


def sort_by_interval_size(tuples_list):
    # We initiate a list where we will store the distance (y-x) of each interval
    distance = []

    # This will take the difference of each interval and append it to the previous list (distance)
    for x, point in enumerate(tuples_list):
        difference = tuples_list[x][1] - tuples_list[x][0]
        distance.append(difference)

    # Will relate the two so that when we sort it will reference distance to tuples_list and store it into list sort
    sort = [tuples_list for _, tuples_list in sorted(zip(distance, tuples_list))]
    return sort


def main():
    num_intervals = int(sys.stdin.readline().strip())

    # initiate the empty tuples_list which will be populated by stdin
    tuples_list = []

    # populates the tuples_list using stdin
    for line in sys.stdin.readlines():
        curr_tup = []
        curr_tup = line.split()
        curr_tup[0] = int(curr_tup[0])
        curr_tup[1] = int(curr_tup[1])
        tuples_list.append(tuple(curr_tup))

    tuples_list.sort()
    merged_tup_list = merged_tuples(tuples_list)

    # delivers specification output
    print(merged_tup_list)
    print(sort_by_interval_size(merged_tup_list))


if __name__ == "__main__":
    main()