#  File: TestLinkedList.py 100/100

#  Description: This will test our LinkedList using helper methods

#  Student Name: Mauricio Benitez

#  Course Name: CS 313E

#  Date Created: April 7, 2021

#  Date Last Modified: April 9, 2021

class Link(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList(object):
    # create a linked list
    # you may add other attributes
    def __init__(self):
        self.first = None

    # get number of links
    def get_num_links(self):

        current = self.first
        counter = 0

        while current != None:
            counter += 1
            current = current.next

        return counter

    # add an item at the beginning of the list
    def insert_first(self, data):
        new_link = Link(data)

        new_link.next = self.first
        self.first = new_link

        # return

    # add an item at the end of a list
    def insert_last(self, data):
        new_link = Link(data)

        current = self.first
        if (current == None):
            self.first = new_link
            return

        while (current.next != None):
            current = current.next

        current.next = new_link

    # add an item in an ordered list in ascending order
    # assume that the list is already sorted
    def insert_in_order(self, data):

        current = self.first
        previous = self.first

        if (current == None): #if the linklist is empty
            self.insert_first(data)
            return

        if (current.data >= data):
            self.insert_first(data)
        elif (current.data <= data):
            newLink = Link(data)
            while (current.data <= data):
                if (current.next == None): #this means we reached the end of the list
                    self.insert_last(data)
                    return
                else: #this is where it'll add if it is in the middle of linkedlist (will increment the pointers)
                    previous = current
                    current = current.next
            #create a new pointer
            previous.next = newLink
            newLink.next = current

    # search in an unordered list, return None if not found
    def find_unordered(self, data):
        current = self.first

        if (current == None):
            return None

        while (current.data != data):
            if (current.next == None):
                return None
            else:
                current = current.next

        return current

    # Search in an ordered list, return None if not found
    def find_ordered(self, data):
        current = self.first

        if (current == None):
            return None

        while (current.data != data):
            if (current.next == None):
                return None
            else:
                current = current.next
        return current

    # Delete and return the first occurrence of a Link containing data
    # from an unordered list or None if not found
    def delete_link(self, data):

        previous = self.first
        current = self.first

        if (current == None):
            return None

        while (current.data != data):
            if (current.next == None):
                return None
            else:
                previous = current
                current = current.next

        if (current == self.first):
            self.first = self.first.next
        else:
            previous.next = current.next

        return current

    # String representation of data 10 items to a line, 2 spaces between data
    def __str__(self):
        empty_string = ''
        current = self.first

        item_counter = 0

        while current != None:

            if item_counter < 10:
                empty_string += str(current.data) + '  '

                current = current.next
                item_counter += 1

            elif item_counter == 10:
                empty_string = empty_string[:-2]
                empty_string += "\n"
                item_counter = 0

        return empty_string[:-2]

    # Copy the contents of a list and return new list
    # do not change the original list
    def copy_list(self):

        # creating new linked list
        copy = LinkedList()
        current = self.first

        # attaching items from the og to the copy
        while current != None:
            copy.insert_last(current.data)
            current = current.next

        return copy

    # Reverse the contents of a list and return new list
    # do not change the original list
    def reverse_list(self):

        # structure similar to copy, but with the logic of a stack
        reverse = LinkedList()
        current = self.first

        while current != None:
            reverse.insert_first(current.data)
            current = current.next

        return reverse

    # Sort the contents of a list in ascending order and return new list
    # do not change the original list
    def sort_list(self):
        sorted_list = LinkedList()
        current = self.first

        # if you insert items in order, you arrive at a sorted list
        while current != None:
            sorted_list.insert_in_order(current.data)

            if current.next == None:
                break
            else:
                current = current.next

        return sorted_list

    # Return True if a list is sorted in ascending order or False otherwise
    def is_sorted (self):

        current = self.first

        if (self.is_empty() == True or self.get_num_links() == 1):
            return True
        for i in range(self.get_num_links()-1): #-1 to avoid out of bounds error
            if (current.data >= current.next.data):
                return False #because not sorted in ascending order
            current = current.next #increment
        #finished traversing list and checked it is in ascending
        return True

    # Return True if a list is empty or False otherwise
    def is_empty(self):
        return self.first == None

    # Merge two sorted lists and return new list in ascending order
    # do not change the original lists
    def merge_list(self, other):

        mergedList = self.copy_list()

        current = other.first

        while current != None:
            mergedList.insert_in_order(current.data)

            current = current.next

        return mergedList

    # Test if two lists are equal, item by item and return True
    def is_equal(self, other):

        # checking every value in both lists
        current = self.first
        other_current = other.first

        # if either gets to None before the other, they are not equal
        while current != None and other_current != None:
            if current.data != other_current.data:
                return False

            current = current.next
            other_current = other_current.next

        return current == None and other_current == None

    # Return a new list, keeping only the first occurence of an element
    # and removing all duplicates. Do not change the order of the elements.
    # do not change the original list
    def remove_duplicates(self):
        uniques = LinkedList()
        current = self.first

        # kept a record of data that's been seen
        memo = []
        while current != None:

            # if we have already seen the data, we don't add it to the
            # list of unique values
            if current.data in memo:
                pass

            else:

                # if they are unique, append them to the new list
                uniques.insert_last(current.data)
                memo.append(current.data)

            current = current.next

        return uniques


def main():
    # Test methods insert_first() and __str__() by adding more than
    # 10 items to a list and printing it.
    ''' testlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
     linked_list = LinkedList()

     for item in testlist:
         linked_list.insert_last(item)


     otherlist =  [1, 3, 5, 7]
     otherLinked = LinkedList()
     for item in otherlist:
         otherLinked.insert_last(item)

     print(linked_list)'''


if __name__ == "__main__":
    main()