#  File: Work.py 100/100

#  Description: Uses both Linear and Binary search to find the the minimum allowable value of v for a given productivity factor that will allow him to write at least n lines of code

#  Student Name: Mauricio Benitez

#  Course Name: CS 313E

#  Date Created: March 4, 2021

#  Date Last Modified: March 7, 2021

import sys
import time


# Input: v an integer representing the minimum lines of code and, k an integer representing the productivity factor
# Output: computes the sum of the series (v + v // k + v // k**2 + ...)
#         returns the sum of the series
def sum_series (v, k):
    sum = 0
    p = 0 #the productivity he writes is inversely proportional to the amount of code he writes
    while (v//k**p) > 0:
        sum += v//(k**p)
        p += 1 #inc bc productivity decreases
    return sum

#Input: n an integer representing the total number of lines of code, k an integer representing the productivity factor
# Output: returns v the minimum lines of code to write using linear search
def linear_search (n, k):
    for l in range(1,n+1): #increase the range to n+1 since this isn't a list and it usually stops at n-1
        if sum_series(l, k) >= n: #just passes it through sum_series and returns the best
            return l



# Input: n an integer representing the total number of lines of code
#        k an integer representing the productivity factor
# Output: returns v the minimum lines of code to write using binary search
def binary_search (n, k):
    lo = 0 #set the low to 0
    hi = n #set the high to the n which would be like the highest index if it were a list except no len(list)-1
    while (lo <= hi):
        mid = (lo + hi) // 2 #finds the middle value
        x = sum_series(mid, k) #this passes it through sum_series
        if x == n:
            return mid
        elif x < n:
            lo = mid + 1 # if x is less than n, that means that the mid must increase by 1 and check the "sublist"
        else:
            hi = mid - 1 # if x is greater than n, that means that the mid must dec by 1 and check the "sublist" or else there won't be a stopping point
    return mid #if it gets here then it will return mid

# Input: no input
# Output: a string denoting all test cases have passed
def test_cases():
  # write your own test cases

  return "all test cases passed"

def main():
  # read number of cases
  line = sys.stdin.readline()
  line = line.strip()
  num_cases = int (line)

  for i in range (num_cases):
    line = sys.stdin.readline()
    line = line.strip()
    inp =  line.split()
    n = int(inp[0])
    k = int(inp[1])

    start = time.time()
    print("Binary Search: " + str(binary_search(n, k)))
    finish = time.time()
    print("Time: " + str(finish - start))

    print()

    start = time.time()
    print("Linear Search: " + str(linear_search(n, k)))
    finish = time.time()
    print("Time: " + str(finish - start))

    print()
    print()

if __name__ == "__main__":
  main()