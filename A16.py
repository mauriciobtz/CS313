#  File: Poly.py 100/100

#  Description: Will take in two polynomials as linked lists and output the arithmetic (sum & product)

#  Student Name: Mauricio Benitez

#  Course Name: CS 313E

#  Date Created: April 14, 2021

#  Date Last Modified: April 16, 2021

import sys


class Link(object):
    def __init__(self, coeff=1, exp=1, next=None):
        self.coeff = coeff
        self.exp = exp
        self.next = next

    def __str__(self):
        return '(' + str(self.coeff) + ', ' + str(self.exp) + ')'


class LinkedList(object):
    def __init__(self):
        self.first = None
    #Helper function to insert at the beginning (reused from A15)
    def insert_first(self, coeff, exp):
        new_link = Link(coeff, exp)

        new_link.next = self.first
        self.first = new_link

    # Helper function to insert at the end (reused from A15)
    def insert_last(self, coeff, exp):
        new_link = Link(coeff, exp)

        current = self.first

        if (current == None):
            self.first = new_link
            return

        while (current.next != None):
            current = current.next

        current.next = new_link

    # keep Links in descending order of exponents
    def insert_in_order(self, coeff, exp):

        new_link = Link(coeff, exp)
        current = self.first
        previous = self.first

        if (new_link.coeff == 0):
            return
        if (current == None):  # if the linklist is empty
            self.insert_first(coeff, exp)
            return

        # comparing exponents
        # if the current exp we are looking at is less than the
        # exponent passed as an argument, insert the argument one first
        if (current.exp < exp):
            self.insert_first(coeff, exp)
        # if the current exponent we are looking at is greater than
        # the argument
        elif (current.exp >= exp):
            newLink = Link(coeff, exp)

            while (current.exp >= exp):
                # if the exponent are the same then add the coeff together
                if (current.exp == exp):
                    new_coeff = current.coeff + coeff
                    new_coeff_link = Link(new_coeff, exp)
                    #print("NEW COEFF ADDITION:",new_coeff_link)
                    if new_coeff_link.coeff == 0:
                        previous.next = current.next #this isolates the node and it "dies"
                        return
                    if current == self.first: #if combining the two nodes would make it the first node
                        new_coeff_link.next = self.first.next
                        self.first = new_coeff_link
                        return
                    # update the pointers
                    previous.next = new_coeff_link
                    new_coeff_link.next = current.next
                    return

                if (current.next == None):  # this means we reached the end of the list
                    self.insert_last(coeff, exp)
                    return
                else:  # this is where it'll add if it is in the middle of linkedlist (will increment the pointers)
                    previous = current
                    current = current.next

            # create a new pointer
            previous.next = newLink
            newLink.next = current

    # add polynomial p to this polynomial and return the sum
    def add(self, p):
        sum_list = LinkedList() #instantiate the list

        current = self.first
        current2 = p.first
        #This while loop will check how the exponents relate
        while (current != None) and (current2 != None):
            if current.exp > current2.exp: #if it is grater then it will insert current
                #print('wtv')
                sum_list.insert_in_order(current.coeff, current.exp)
                current = current.next
            #if it is less than it will insert the current2
            elif current.exp < current2.exp:
                #print('elif executed')
                sum_list.insert_in_order(current2.coeff, current2.exp)
                current2 = current2.next
            #if they are equal it will add them
            elif current.exp == current2.exp:
                #print('equals')
                new_coeff = current.coeff + current2.coeff
                sum_list.insert_in_order(new_coeff, current.exp)

                current = current.next
                current2 = current2.next
        #This conditional will determine if a list is exhausted so it will insert the remaining nodes
        if current == None:
            while current2 != None:
                sum_list.insert_in_order(current2.coeff, current2.exp)
                current2 = current2.next

        elif current2 == None:
            while current != None:
                sum_list.insert_in_order(current.coeff, current.exp)
                current = current.next

        # sum_list.combine_like_terms()

        return sum_list

    # multiply polynomial p to this polynomial and return the product
    def mult(self, p):
        mult_list = LinkedList()

        # the function will have two loops
        # one will iterate through the first poly, while the other will
        # multiply it to the other poly terms
        current = self.first
        current2 = p.first

        while (current != None):
            while (current2 != None):
                new_coeff = current.coeff * current2.coeff #mult the coeff

                new_exp = current.exp + current2.exp #add the exp

                mult_list.insert_in_order(new_coeff, new_exp) #insert this in order so it is appended to mult list

                current2 = current2.next
            #update the pointers
            current2 = p.first
            current = current.next

            mult_list.combine_like_terms() #run the updated multlist into combine so that it collects like terms

        return mult_list

    #This will combine like terms after the multiplication fcn
    def combine_like_terms(self):

        if self.first != None:
            current = self.first
            #this while loop will traverse through the list if it is not empty
            while current != None:
                temp = current.next
                #compares the previous to the next and if they are the same exp it executes
                while temp != None and temp.exp == current.exp:
                    current.coeff += temp.coeff
                    current.next = temp.next
                    temp = temp.next

                current = current.next

    # create a string representation of the polynomial
    def __str__(self):
        current = self.first

        polystr = ''

        while current != None:
            polystr += str(current) + ' + '
            current = current.next

        return polystr[:-3]


def main():
    # read data from file poly.in from stdin
    num_poly_p = int(sys.stdin.readline().strip())

    # for appending input and then transferring to a link
    p_list = LinkedList()

    # create polynomial p
    for i in range(num_poly_p):
        temp_list = []
        temp_list = sys.stdin.readline().split()
        temp_list[0] = int(temp_list[0])
        temp_list[1] = int(temp_list[1])

        p_list.insert_in_order(temp_list[0], temp_list[1])

    blank_line = sys.stdin.readline()

    # create polynomial q

    num_poly_q = int(sys.stdin.readline().strip())

    # for appending input and then transferring to a link
    q_list = LinkedList()

    # create polynomial p and insert the values
    for i in range(num_poly_q):
        temp_list = []
        temp_list = sys.stdin.readline().split()
        temp_list[0] = int(temp_list[0])
        temp_list[1] = int(temp_list[1])

        q_list.insert_in_order(temp_list[0], temp_list[1])


    # get sum of p and q and print sum
    print(p_list.add(q_list))

    # get product of p and q and print product
    print(p_list.mult(q_list))


if __name__ == "__main__":
    main()