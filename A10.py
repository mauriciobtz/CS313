#  File: Boxes.py 100/100

#  Description: This program uses recursion to find the largest amount of nesting boxes that fit in a sequence

#  Student Name: Mauricio Benitez

#  Course Name: CS 313E

#  Date Created: March 22, 2021

#  Date Last Modified: March 26, 2021


import sys

# generates all subsets of boxes and stores them in all_box_subsets
# box_list is a list of boxes that have already been sorted
# sub_set is a list that is the current subset of boxes
# idx is an index in the list box_list
# all_box_subsets is a 3-D list that has all the subset of boxes
def sub_sets_boxes (box_list, sub_set, idx, all_box_subsets):
  if (idx >= len(box_list)):
    all_box_subsets.append(sub_set)
    return
    # len(all_box_subsets) == 2**len(box_list) #this formula is for testing
  else:
    temp_list = sub_set[:]
    sub_set.append(box_list[idx])
    sub_sets_boxes(box_list, temp_list, idx + 1, all_box_subsets)
    sub_sets_boxes(box_list, sub_set, idx + 1, all_box_subsets)

# goes through all the subset of boxes and only stores the
# largest subsets that nest in the 3-D list all_nesting_boxes
# largest_size keeps track what the largest subset is
def largest_nesting_subsets(all_box_subsets):
  largest_size = 0
  largest = []
  #We have to use a nested for loop since the array is 3D
  for subset in all_box_subsets:
    for box in range(len(subset) - 1):
      # if j <= len(subset)-2:
      # nesting = does_fit(subset[box], subset[box + 1])
      if does_fit(subset[box], subset[box + 1]) == False: #This stops it before it proceeds if it doesn't fit
        break
      elif does_fit(subset[box], subset[box + 1]) == True and box == len(subset) - 2:
        currSize = len(subset) #This sets the current length and will be used to compare largest_size
        if currSize > largest_size:  # if it is larger, then it will clear the list and append
          largest_size = currSize
          largest = [] #clear list if it's larger and append the rest
          largest.append(subset)
        elif currSize == largest_size:  # if it is the same size, it will just append to the list
          largest.append(subset)

      elif does_fit(subset[box], subset[box + 1]) == True:
        continue

  return largest

# returns True if box1 fits inside box2
def does_fit (box1, box2):
  return (box1[0] < box2[0] and box1[1] < box2[1] and box1[2] < box2[2])

def main():
  # read the number of boxes
  line = sys.stdin.readline()
  line = line.strip()
  num_boxes = int (line)

  # create an empty list for the boxes
  box_list = []

  # read the boxes from the file
  for i in range (num_boxes):
    line = sys.stdin.readline()
    line = line.strip()
    box = line.split()
    for j in range (len(box)):
      box[j] = int (box[j])
    box.sort()
    box_list.append(box)

  '''
  # print to make sure that the input was read in correctly
  print (box_list)
  print()
  '''

  # sort the box list
  box_list.sort()

  '''
  # print the box_list to see if it has been sorted.
  print (box_list)
  print()
  '''

  # create an empty list to hold all subset of boxes
  all_box_subsets = []
  #print(all_box_subsets)

  # create a list to hold a single subset of boxes
  sub_set = []

  # generate all subsets of boxes and store them in all_box_subsets
  sub_sets_boxes (box_list, sub_set, 0, all_box_subsets)
  #print(len(all_box_subsets))


  # all_box_subsets should have a length of 2^n where n is the number
  # of boxes
  #print(len(all_box_subsets) == 2 ** len(box_list))

  # go through all the subset of boxes and only store the
  # largest subsets that nest in all_nesting_boxes
  all_nesting_boxes = largest_nesting_subsets (all_box_subsets)

  # print the largest number of boxes that fit
  print(len(all_nesting_boxes[0]))


  # print the number of sets of such boxes
  print(len(all_nesting_boxes))

if __name__ == "__main__":
  main()