#  File: TestBinaryTree.py INCOMPLETE

#  Description: 

#  Student Name: Mauricio Benitez

#  Course Name: CS 313E

#  Date Created: April 21, 2021

#  Date Last Modified: April 23, 2021

import sys

class Node (object):
  ...

class Tree (object):
  # Returns true if two binary trees are similar
  def is_similar (self, pNode):
      pass

  # Returns a list of nodes at a given level from left to right
  def get_level (self, level):
      pass

  # Returns the height of the tree
  def get_height (self):
        pass

  # Returns the number of nodes in the left subtree and
  # the number of nodes in the right subtree and the root
  def num_nodes (self):
      pass

def main():
    # Create three trees - two are the same and the third is different
	line = sys.stdin.readline()
	line = line.strip()
	line = line.split()
	tree1_input = list (map (int, line)) 	# converts elements into ints

	line = sys.stdin.readline()
	line = line.strip()
	line = line.split()
	tree2_input = list (map (int, line)) 	# converts elements into ints

	line = sys.stdin.readline()
	line = line.strip()
	line = line.split()
	tree3_input = list (map (int, line)) 	# converts elements into ints

    # Test your method is_similar()

    # Print the various levels of two of the trees that are different

    # Get the height of the two trees that are different

    # Get the total number of nodes a binary search tree

if __name__ == "__main__":
  main()