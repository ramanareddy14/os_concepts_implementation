# -*- coding: utf-8 -*-
"""
Strings in python from geeksforgeeks
"""

'''
find minimum character removal to make two strings anagram
'''

from collections import Counter
import sys

count = len(sys.path)
modules_count = len(sys.modules)



print("system path count is : ",count,"\n")
for i in range(0,count):
    print(sys.path[i])
    
    
print(sys.getrefcount(count))