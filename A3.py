#  File: Cipher.py 100/100

#  Description: Rotate list and encrypt/decrypt

#  Student Name: Mauricio Benitez

#  Course Name: CS 313E

#  Date Created: February 6, 2021

#  Date Last Modified: February 8, 2021

import sys
import math


def encrypt(p_string):
    L = len(p_string)
    M = math.sqrt(L)

    # This will give us the dimension of the grid (K) and checks if it's a square(int)
    if M.is_integer() == True:
        K = int(math.sqrt(M)) ** 2
    else:
        M = (math.ceil(M)) ** 2
        K = int(math.sqrt(M))
        num_asterisks = M - L
        p_string = p_string + ("*" * num_asterisks)  # pads for encryption

    i = 0
    e_table = []

    cols = K
    rows = K

    e_table = [[0 for i in range(cols)] for j in range(rows)]  #

    for row in range(rows):
        for col in range(cols):
            e_table[row][col] = p_string[i]
            i = i + 1

            # This will rotate and encrypt
    transposed_grid = []
    transposed_grid = [[row[i] for row in e_table] for i in range(len(e_table[0]))]
    for row in range(len(transposed_grid[0])):
        transposed_grid[row] = transposed_grid[row][::-1]

    # This will remove the * and return the final encypted string
    list2str = sum(transposed_grid, [])
    strfromlist = ''.join(list2str)
    strfromlist = strfromlist.replace('*', '')
    return strfromlist


def decrypt(q_string):
    L = len(q_string)
    M = math.sqrt(L)

    temp_string = "#" * L

    if M.is_integer() == True:
        K = int(math.sqrt(M)) ** 2

    else:
        M = (math.ceil(M)) ** 2
        K = int(math.sqrt(M))
        num_asterisks = M - L
        temp_string = temp_string + ("*" * num_asterisks)  # pads for encryption
        q_string = q_string + ("*" * num_asterisks)  # pads for encryption

    i = 0
    e_table = []

    cols = K
    rows = K

    e_table = [[1 for i in range(cols)] for j in range(rows)]  # creates and populates

    # This will put the string into the e_table
    for row in range(rows):
        for col in range(cols):
            e_table[row][col] = q_string[i]
            i = i + 1
    # This will rotate 3 times and decrypt
    transposed_grid = e_table
    for x in range(3):
        transposed_grid = [[row[i] for row in transposed_grid] for i in range(len(transposed_grid[0]))]
        for row in range(len(transposed_grid[0])):
            transposed_grid[row] = transposed_grid[row][::-1]

    # This will remove the * and return the final decrypted string
    list2str = sum(transposed_grid, [])
    strfromlist = ''.join(list2str)
    strfromlist = strfromlist.replace('*', '')
    return strfromlist


def main():
    # read the two strings P and Q from standard imput
    p_string = sys.stdin.readline().strip()
    q_string = sys.stdin.readline().strip()

    encrypt_final = encrypt(p_string)  # encrypt the string P

    decrypt_final = decrypt(q_string)  # decrypt the string Q
    print(encrypt_final)
    print(decrypt_final)


if __name__ == "__main__":
    main()