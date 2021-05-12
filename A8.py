#  File: Palindrome.py 100/100

#  Description: output the shortest palindrome by adding letters to the beginning of the string

#  Student Name: Mauricio Benitez

#  Course Name: CS 313E

#  Date Created: March 6, 2021

#  Date Last Modified: March 8, 2021

import sys

def smallest_palindrome(pal):
    # check if it's not already a palindrome
    string1 = pal
    string2 = string1[::-1]

    if string1 == string2: #checks if the line is already a palindrome by comparing the reverse
        return string1
    else: #this will check if removing the last character of the string becomes a palindrome
        for i in range(1, len(string1)):
            string3 = string1[:-i] #assigning string3 to the truncated reversal ; "removing" letters from the end of the string

            if string3 == string3[::-1]:  # checking the "stripped" string against its own reverse
                reversed = string1[-i:-1]
                rere = reversed[::-1] #this reverses the reversal to go from "center" to left
                return (string1[-1] + rere + string1) # concatenate the original string with the "removed" letters




# Output: a string denoting all test cases have passed
# def test_cases():
# write your own test cases

# return "all test cases passed"

def main():
    # run your test cases
    '''
    print (test_cases())
    '''
    #read the data
    pal = sys.stdin.readline().strip()
    while pal != '':
        print(smallest_palindrome(pal))
        pal = sys.stdin.readline().strip()

if __name__ == "__main__":
    main()