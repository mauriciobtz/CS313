#  File: Radix.py 100/100

#  Description: It will sort both digits & letters using ASCII and output a sorted list using a radix sort algorithm

#  Student Name: Mauricio Benitez

#  Course Name: CS 313E

#  Date Created: April 4, 2021

#  Date Last Modified: April 7, 2021

import sys


class Queue(object):
    def __init__(self):
        self.queue = []

        # add an item to the end of the queue

    def enqueue(self, item):
        self.queue.append(item)

        # remove an item from the beginning of the queue

    def dequeue(self):
        return (self.queue.pop(0))

        # check if the queue if empty

    def is_empty(self):
        return (len(self.queue) == 0)

        # return the size of the queue

    def size(self):
        return (len(self.queue))

    def __str__(self):
        return str(self.queue)


# Input: a is a list of strings that have either lower case
#        letters or digits
# Output: returns a sorted list of strings
def radix_sort(a):
    # set the max num of digits
    m = 0

    # this will compare each item to m (max) and if it's greater than m it
    # will update the m (max)
    for item in a:
        m = max(len(item), m)

    # This will pad the items on the RIGHT in the list according to m (size of largest item)
    # print("main num_digits:", m)
    # print(m)
    count = 0
    for digit in range(len(a)):

        # this will pad (L -> R) items so they are all equal length
        if len(a[digit]) < m:  # if it is less

            # pad to the R with '#'
            a[digit] = a[digit].ljust(m, '#')

            count += 1  # inc counter
    # print('A list:', a)

    queue_list = []

    # creating the Queues 0-9 and a-z plus 1 for padding character = 36
    for i in range(38):
        Q = Queue()
        queue_list.append(Q)

    # used to dump the contents of all other queues
    QLast = Queue()

    # populated with the contents of a
    for word in a:
        QLast.enqueue(word)

    # print(QLast)

    # passes dependent upon the word with max length
    for pass_num in range(m):
        # print('Pass:', pass_num)

        i = -1 * (pass_num + 1)
        # for traversing strings backwards
        while QLast.size() != 0:
            word = QLast.dequeue()

            # check if the character is the special one we padded our strings with
            if word[i] == '#':
                queue_list[0].enqueue(word)
                # print('Queue num:', str(len(queue_list)) + str(queue_list[-1]))

            # check if character is numeric
            elif word[i].isnumeric():
                queue_list[int(word[i])].enqueue(word)
                # print(queue_list[int(word[i])])
                # print('Queue num,', word[i], ':', queue_list[int(word[i])])

            # check if the character is a letter
            if word[i].isalpha():
                queue_list[ord(word[i]) - 87].enqueue(word)
                # print('Queue num,', str(ord(word[i])- 87),
                # ':', str(queue_list[ord(word[i])- 87]))
        for bucket in queue_list:
            while bucket.size() != 0:
                QLast.enqueue(bucket.dequeue())
                # print('QLast:'+ str(QLast))
    qlast_list = []
    while QLast.size() != 0:
        qlast_list.append(QLast.dequeue())

    return qlast_list


# look at the rightmost character in each string from the list of strings

def main():
    # read the number of words in file
    line = sys.stdin.readline()
    line = line.strip()
    num_words = int(line)

    # create a word list
    word_list = []
    for i in range(num_words):
        line = sys.stdin.readline()
        word = line.strip()
        word_list.append(word)

    # print(word_list)

    # use radix sort to sort the word_list
    sorted_list = radix_sort(word_list)

    for item in range(len(sorted_list)):
        sorted_list[item] = sorted_list[item].rstrip('#')

    # for item in sorted_list:
    #     print(item)
    print(sorted_list)


if __name__ == "__main__":
    main()