#  File: Reducible.py 100/100

#  Description: Takes in a list of words and outputs the larget words that are reducible to one letter that is also a word

#  Student Name: Mauricio Benitez

#  Course Name: CS 313E

#  Date Created: April 1, 2021

#  Date Last Modified: April 5, 2021

import sys
import math


# Input: takes as input a positive integer n
# Output: returns True if n is prime and False otherwise
def is_prime(n):
    if (n == 1):
        return False

    limit = int(n ** 0.5) + 1
    div = 2
    while (div < limit):
        if (n % div == 0):
            return False
        div += 1
    return True


# Output: returns the index the string will hash into
def hash_word(s, size):
    hash_idx = 0
    for j in range(len(s)):
        letter = ord(s[j]) - 96
        hash_idx = (hash_idx * 26 + letter) % size
    return hash_idx


# Input: takes as input a string in lower case and the constant
#        for double hashing
# Output: returns the step size for that string
def step_size(s, const):
    return (const - (hash_word(s, const)))


# Input: takes as input a string and a hash table
# Output: no output; the function enters the string in the hash table,
#         it resolves collisions by double hashing
def insert_word(s, hash_table):
    # created variables to limit num of function calls and toll on efficiency
    hash_len = len(hash_table)
    hash_index = hash_word(s, hash_len)

    # linear probing using hashing index
    if hash_table[hash_index] == '':
        hash_table[hash_index] = s

    else:
        rehash_index = step_size(s, 11)

        # else:
        i = 0
        # double hashing as long as there isnt an empty space
        while hash_table[(hash_index + i * rehash_index) % hash_len] != '':
            i += 1

        hash_table[(hash_index + rehash_index * i) % hash_len] = s

    return


# Input: takes as input a string and a hash table
# Output: returns True if the string is in the hash table
#         and False otherwise
def find_word(s, hash_table):
    # this function uses the same logic as insert_word, but for finding a word
    hash_len = len(hash_table)

    hash_index = hash_word(s, hash_len)
    if hash_table[hash_index] == s:
        return True

    elif hash_table[hash_index] != '':
        rehash_index = step_size(s, 11)
        i = 1

        while hash_table[(hash_index + rehash_index * i) % hash_len] != '':
            if hash_table[(hash_index + rehash_index * i) % hash_len] == s:
                return True
            i += 1

    else:
        return False


# Input: string s, a hash table, and a hash_memo
#        recursively finds if the string is reducible
# Output: if the string is reducible it enters it into the hash memo
#         and returns True and False otherwise
def is_reducible(s, hash_table, hash_memo):
    # if a word is reduced to one word and it's not these, it's not reducible
    if len(s) == 1:
        return (s == 'a' or s == 'i' or s == 'o')

    elif find_word(s, hash_memo):
        return True

    else:

        if find_word(s, hash_table):
            # i = 0

            for i in range(len(s)):
                # string slicing to reduce the word
                substring = s[:i] + s[i + 1:]
                if is_reducible(substring, hash_table, hash_memo):
                    insert_word(s, hash_memo)
                    return True
        else:
            return False

    # return


# Output: returns a list of words that have the maximum length
def get_longest_words(string_list):
    max_len_list = []
    max_length = len(string_list[0])

    for i in range(len(string_list)):

        if len(string_list[i]) == max_length:
            max_len_list.append(string_list[i])

        # if a new max length  is found, clear list to start over
        elif len(string_list[i]) > max_length:
            max_len_list.clear()
            max_len_list.append(string_list[i])
            max_length = len(string_list[i])

    return max_len_list


def main():
    # create an empty word_list
    word_list = []
    # read words from words.txt and append to word_list
    for line in sys.stdin:
        line = line.strip()
        word_list.append(line)

    # find length of word_list
    length_word_list = len(word_list)

    # determine prime number N that is greater than twice
    # the length of the word_list
    N = 2 * length_word_list

    # anything times 2 will not be a prime num, so it's safe to assume
    # we need to by default go into the loop
    while is_prime(N) == False:
        N = N + 1

    # create an empty hash_list
    hash_list = []

    # populate the hash_list with N blank strings
    for n in range(N):
        hash_list.append('')

    # hash each word in word_list into hash_list
    # for collisions use double hashing
    for word in word_list:
        insert_word(word, hash_list)

    # create an empty hash_memo of size M
    M = math.ceil(0.2 * length_word_list)
    while is_prime(M) == False:
        M = M + 1

    # populate the hash_memo with M blank strings
    hash_memo = [''] * M

    # create an empty list reducible_words
    reducible_words = []

    # for each word in the word_list recursively determine
    # if it is reducible, if it is, add it to reducible_words
    # as you recursively remove one letter at a time check
    for word in word_list:
        if is_reducible(word, hash_list, hash_memo) == True:
            reducible_words.append(word)

    # find the largest reducible words in reducible_words
    largest_words = get_longest_words(reducible_words)
    largest_words.sort()

    # print the reducible words in alphabetical order
    # one word per line
    for word in largest_words:
        print(word)


if __name__ == "__main__":
    main()
