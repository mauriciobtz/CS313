#  File: ExpressionTree.py 100/100

#  Description: Using expression trees to evaluate infix notation convert infix to postfix and prefix

#  Student Name: Mauricio Benitez

#  Course Name: CS 313E

#  Date Created: April 17, 2021

#  Date Last Modified: April 19, 2021

import sys

operators = ['+', '-', '*', '/', '//', '%', '**']  # the operators we will reference later in evaluate


class Stack(object):
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if (not self.is_empty()):
            return self.stack.pop()
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0


class Node(object):
    def __init__(self, data=None, lChild=None, rChild=None):
        self.data = data
        self.lChild = lChild
        self.rChild = rChild


class Tree(object):
    def __init__(self):
        self.root = None

    # this function takes in the input string expr and
    # creates the expression tree
    def create_tree(self, expr):

        # splitting by spaces to be able to search fro '.'
        # in the operands
        expr_list = expr.split()

        # creating a node because that constructor doesn't have it
        self.root = Node()

        # creating a stack
        treeStack = Stack()

        current = self.root

        for character in expr_list:

            # If the current token is a left parenthesis add a new node as the left child of the current node.
            if character == '(':
                current.lChild = Node()
                treeStack.push(current)
                current = current.lChild  # Push current node on the stack and make current node equal to the left child.

            # If the current token is an operator set the current node's data value to the operator.
            elif character in operators:

                current.data = character

                # Push current node on the stack.
                treeStack.push(current)

                # Add a new node as the right child of the current node and make the current node equal to the right child.
                current.rChild = Node()
                current = current.rChild

            # If the current token is an operand, set the current node's data value to the operand and
            #  make the current node equal to the parent by popping the stack.
            elif character.isnumeric() or '.' in character:
                current.data = (character)
                current = treeStack.pop()

            # If the current token is a right parenthesis make the current node equal to the parent node by popping the stack if it is not empty.
            elif character == ")":
                if not treeStack.is_empty():
                    current = treeStack.pop()

    # this function should evaluate the tree's expression
    # returns the value of the expression after being calculated
    def evaluate(self, aNode):
        # this will evaluate the expressions referencing the operators before
        if aNode.data in operators:
            # this will add the childs
            if aNode.data == '+':
                return self.evaluate(aNode.lChild) + self.evaluate(aNode.rChild)
            # this will subtract the childs
            elif aNode.data == '-':
                return self.evaluate(aNode.lChild) - self.evaluate(aNode.rChild)
            # this will multiply the childs
            elif aNode.data == '*':
                return self.evaluate(aNode.lChild) * self.evaluate(aNode.rChild)
            # this will divide the childs
            elif aNode.data == '/':
                return self.evaluate(aNode.lChild) / self.evaluate(aNode.rChild)
            # this will give truncate the childs
            elif aNode.data == '//':
                return self.evaluate(aNode.lChild) // self.evaluate(aNode.rChild)
            # this will give the remainder of the childs
            elif aNode.data == '%':
                return self.evaluate(aNode.lChild) % self.evaluate(aNode.rChild)
            # this will give the exponent
            elif aNode.data == '**':
                return self.evaluate(aNode.lChild) ** self.evaluate(aNode.rChild)
        # this will return if it doesnt go into the if statement
        else:
            return float(aNode.data)

    # this function should generate the preorder notation of
    # the tree's expression
    # returns a string of the expression written in preorder notation
    def pre_order(self, aNode):
        pre_ord = ''  # create an empty string
        # for pre we will append it first
        if not aNode == None:
            pre_ord += str(aNode.data) + ' '
            pre_ord += self.pre_order(aNode.lChild)
            pre_ord += self.pre_order(aNode.rChild)
        return pre_ord

        # this function should generate the postorder notation of

    # the tree's expression
    # returns a string of the expression written in postorder notation
    def post_order(self, aNode):
        post_ord = ''  # create an empty string
        # for pre we will append it last
        if not aNode == None:
            post_ord += self.post_order(aNode.lChild)
            post_ord += self.post_order(aNode.rChild)
            post_ord += str(aNode.data) + ' '
        return post_ord

    # you should NOT need to touch main, everything should be handled for you


def main():
    # read infix expression
    line = sys.stdin.readline()
    expr = line.strip()

    tree = Tree()
    tree.create_tree(expr)

    # evaluate the expression and print the result
    print(expr, "=", str(tree.evaluate(tree.root)))

    # get the prefix version of the expression and print
    print("Prefix Expression:", tree.pre_order(tree.root).strip())

    # get the postfix version of the expression and print
    print("Postfix Expression:", tree.post_order(tree.root).strip())


if __name__ == "__main__":
    main()