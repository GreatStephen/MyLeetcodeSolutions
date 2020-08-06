#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'droppedRequests' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY requestTime as parameter.
#

def droppedRequests(requestTime):
    # Sliding window
    R = requestTime
    l = r = 0
    l60 = r60 = 0
    ans = 0
    count = 0 # count how many duplicates in a second
    while r<len(R):
        if R[r]-R[l]<10 and r-l+1>20:
            ans += 1 # more than 20 in 10 sec, drop
        elif R[r]-R[l]<10 and r-l+1<=20 :
            if r==0 or R[r]==R[r-1]:
                count += 1
            else:
                count = 1
            if count>3: # more than 3 in a sec, drop
                ans += 1
        elif R[r60]-R[l60]<60 and r60-l60+1>60:
            ans += 1


        if R[r]-R[l]>=10: # shrink the 10-sec window
            while l<=r and R[r]-R[l]>=10:
                l += 1      
        
        if R[r60]-R[l60]>=60: # shrink the 60-sec window
            while l60<=r60 and R[r60]-R[l60]>=60:
                l60 += 1
        r += 1
        r60 += 1
    return ans



if __name__ == '__main__':