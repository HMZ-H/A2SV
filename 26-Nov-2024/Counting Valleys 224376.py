# Problem: Counting Valleys - https://www.hackerrank.com/challenges/counting-valleys/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    
    stack=[]
    valley = 0
    for step in path:
        if stack and (step == "U" and stack[-1] == "D" or step == "D" and stack[-1] == "U"):
            stack.pop()
            continue
        stack.append(step)
        if len(stack) == 1 and stack[-1] == "D":
            valley += 1
    return valley

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
