#  File: Josephus.py 91/100

#  Description: This uses circular linked list to remove values using a start and a step

#  Student Name: Mauricio Benitez

#  Course Name: CS 313E

#  Date Created: April 10, 2021

#  Date Last Modified: April 12, 2021


import sys


class Link(object):

    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next


class CircularList(object):
    # Constructor
    def __init__(self):
        self.first = None

    # Insert an element (value) in the list
    def insert(self, data):
        if not self.first:
            self.first = Link(data)
            self.first.next = self.first

        else:
            new_link = Link(data)
            current = self.first

            while current.next != self.first:
                current = current.next

            current.next = new_link
            new_link.next = self.first

    # Find the Link with the given data (value)
    # or return None if the data is not there
    def find(self, data):
        current = self.first

        if current == None:
            return None

        while current.data != data:
            if current == self.first:
                return None
                break
            else:
                current = current.next

        return current

    # Delete a Link with a given data (value) and return the Link
    # or return None if the data is not there
    def delete(self, data):

        if self.first == None:
            return None

        # if we are deleting the head of the list
        elif self.first.data == data:
            current = self.first

            # look for the tail of the list to re-point it
            while current.next != self.first:
                # point the tail to the link AFTER the head
                current = current.next
            # if self.first.next == current:
            #     self.first.next = None
            current.next = self.first.next
            # assign a new head link
            self.first = current

        else:
            current = self.first
            previous = None

            # as long as we're not at the tail
            while current.next != self.first:
                previous = current
                current = current.next

                if current.data == data:
                    previous.next = current.next
                    return current
            return None

    # Delete the nth Link starting from the Link start
    # Return the data of the deleted Link AND return the
    # next Link after the deleted Link in that order
    def delete_after(self, start, n):
        current = self.first
        # print('current is:', current.data)
        # print('current.next is:', current.next.data)


        #this will check if it is only 1 item
        if current.next == current:
            # print(self.first.data)
            return current.data, current

        # print('start is:', start)
        #get to the starting point (node)
        while (current.data != start):
            current = current.next
            #print(current.data)



        #find the nth value
        i = 1
        while (i < n):
            current = current.next
            i += 1

        deleted_data = current.data
        self.delete(current.data) #use the delete function to remove the value from the list
        # print('current is:', current.data)
        # print('current.next is:', current.next.data)
        return deleted_data, current.next

    # Return a string representation of a Circular List
    # The format of the string will be the same as the __str__
    # format for normal Python lists
    def __str__(self):
        current = self.first


        string_rep = '['
        while current != None:
            string_rep += str(current.data) + ', '
            current = current.next

            if current == self.first:
                break
        if len(string_rep) ==1:
            return string_rep + ']'
        else:
            return string_rep[:-2] + ']'


def main():
    # read number of soldiers
    line = sys.stdin.readline()
    line = line.strip()
    num_soldiers = int(line)

    # read the starting number
    line = sys.stdin.readline()
    line = line.strip()
    start_count = int(line)
    start_count = Link(start_count)

    # read the elimination number
    line = sys.stdin.readline()
    line = line.strip()
    elim_num = int(line)


    CL = CircularList()

    for i in range(1, num_soldiers +1):
        CL.insert(i)

    for i in range(num_soldiers):
        if start_count != None:
            x, start_count  = CL.delete_after(start_count.data, elim_num)
            print(x)
    # print(CL)

# 1 2 3 4 5

if __name__ == "__main__":
    main()