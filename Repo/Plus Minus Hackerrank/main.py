#!/bin/python3

import math
import os
import random
import re
import sys
from decimal import Decimal


#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    positives = 0
    negatives = 0
    neutral = 0

    for i in range(0, len(arr)):
        if arr[i] > 0:
            positives += 1
        elif arr[i] < 0:
            negatives += 1
        else:
            neutral += 1

    positives_ratio = round(positives / len(arr), 6)
    negatives_ratio = round(negatives / len(arr), 6)
    neutral_ratio = round(neutral / len(arr), 6)

    print(positives_ratio)
    print(negatives_ratio)
    print(neutral_ratio)


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
