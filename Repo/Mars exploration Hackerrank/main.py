#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def marsExploration(s):
    # Write your code here
    letters_changed = 0
    for letter in range(0, len(s), 3):
        if s[letter] != 'S':
            letters_changed += 1
        if s[letter + 1] != 'O':
            letters_changed += 1
        if s[letter + 2] != 'S':
            letters_changed += 1
    return letters_changed


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
