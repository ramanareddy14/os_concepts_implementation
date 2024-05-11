"""
Find majority element (Boyer–Moore Majority Vote Algorithm)
Given an integer array containing duplicates, return the majority element if present. A majority element appears more than n/2 times, where n is the array size.
We can find the majority element using linear time and constant space using the Boyer–Moore majority vote algorithm.

The algorithm processes each element of the sequence, one at a time. When processing an element x,

If the counter is 0, set the current candidate to x, and set the counter to 1.
If the counter is non-zero, increment or decrement it according to whether x is a current candidate.
At the end of this process, if the sequence has a majority, it will be the element stored by the algorithm. If there is no majority element, the algorithm will not detect that fact and may output the wrong element. In other words, the Boyer–Moore majority vote algorithm produces correct results only when the majority element is present in the input.
"""


