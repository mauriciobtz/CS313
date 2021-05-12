#  File: BST_Cipher.py 100/100

#  Description: using binary search trees to encrypt / decrypt a string

#  Student Name: Mauricio Benitez

#  Course Name: CS 313E

#  Date Created: April 21, 2021

#  Date Last Modified: April 23, 2021

import sys

# creating node class
# necessary for creating the tree
class Node(object):
    def __init__(self, data=None, lChild=None, rChild=None):
        self.data = data
        self.lChild = lChild
        self.rChild = rChild

    def __str__(self):
        return self.data


class Tree(object):
    # the init() function creates the binary search tree with the
    # encryption string. If the encryption string contains any
    # character other than the characters 'a' through 'z' or the
    # space character drop that character.
    def __init__(self, encrypt_str):
        self.root = None

        temp_str = ''

        # this is where we adjust the key, removing characters
        # that are not a-z or the space character
        for s in encrypt_str:
            if s.isalpha() or s == ' ':
                temp_str += s

        encrypt_str = temp_str

        # create the bst based on the modified key
        for s in encrypt_str:
            self.insert(s)

    # the insert() function adds a node containing a character in
    # the binary search tree. If the character already exists, it
    # does not add that character. There are no duplicate characters
    # in the binary search tree.
    def insert(self, ch):
        newNode = Node(ch)

        # takes into account that the bst is empty
        if (self.root == None):
            self.root = newNode

        else:
            current = self.root

            # until we have reached the end of the tree
            # in this case reaching the end means we have inserted the
            # character
            while (current != None):

                # makes sure there are no duplicates in the tree
                if (ch == current.data):
                    break

                # insert each letter into a binary tree using
                # the ASCII value as a comparative measure

                elif ch < current.data:
                    if current.lChild == None:
                        current.lChild = newNode
                        break
                    current = current.lChild

                elif (ch > current.data):
                    if current.rChild == None:
                        current.rChild = newNode
                        break
                    current = current.rChild

    # the search() function will search for a character in the binary
    # search tree and return a string containing a series of lefts
    # (<) and rights (>) needed to reach that character. It will
    # return a blank string if the character does not exist in the tree.
    # It will return * if the character is the root of the tree.
    def search(self, ch):

        current = self.root

        series = ''

        # editing code from class website

        while ((current != None) and (current.data != ch)):
            if (ch > current.data):
                series += '>'
                current = current.rChild

            elif (ch < current.data):
                series += '<'
                current = current.lChild

        # return blank string if the character does not exist in the tree
        if current == None:
            return ''

        # return * if the character is the root of the tree.
        if current == self.root:
            return '*'

        return series

    # the traverse() function will take string composed of a series of
    # lefts (<) and rights (>) and return the corresponding
    # character in the binary search tree. It will return an empty string
    # if the input parameter does not lead to a valid character in the tree.
    def traverse(self, st):

        # takes care of if there is even a tree to begin with,
        # or if we've traversed the entirety of the tree
        if self.root != None:

            current = self.root

            # keep track of the series of lefts and rights in the bst
            # there is also the option of the *, which corresponds to
            # the root of the tree
            for s in st:
                if s == '>':
                    current = current.rChild

                elif s == '<':
                    current = current.lChild

                elif s == '*':
                    return str(self.root)

                # empty string if the input parameter does not lead to a valid
                # character in the tree
                if current == None:
                    return ''

            return str(current.data)

    # the encrypt() function will take a string as input parameter, convert
    # it to lower case, and return the encrypted string. It will ignore
    # all digits, punctuation marks, and special characters.
    def encrypt(self, st):

        # convert to lower case
        st = st.lower()

        encryption = ''

        for letter in st:
            # ignoiring all digits, punctuation marks, and special characters.
            if letter.isalpha() or letter == ' ':
                encryption += str(self.search(letter)) + '!'  # add delimeter

        return encryption[:-1]

    # the decrypt() function will take a string as input parameter, and
    # return the decrypted string.
    def decrypt(self, st):

        if self.root != None:
            decryption = ''

            # splitting by the delimeter character
            for letter in st.split('!'):
                decryption += str(self.traverse(letter))

        return decryption


def main():
    # read encrypt string
    line = sys.stdin.readline()
    encrypt_str = line.strip()

    # create a Tree object
    the_tree = Tree(encrypt_str)

    # read string to be encrypted
    line = sys.stdin.readline()
    str_to_encode = line.strip()

    # print the encryption
    print(the_tree.encrypt(str_to_encode))

    # read the string to be decrypted
    line = sys.stdin.readline()
    str_to_decode = line.strip()

    # print the decryption
    print(the_tree.decrypt(str_to_decode))


if __name__ == "__main__":
    main()