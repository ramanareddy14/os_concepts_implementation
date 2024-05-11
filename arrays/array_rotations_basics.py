"""
program for array rotations
approach 1 : 
    k = array.index(element) # finding index if an element is given
    new_lis = array[k+1:]+array[0:k+1]
    ---O(n) as we need to iterate through all the elements
    
Cyclically rotate an array by 1 
    new_list = array[1:] + array[0:1]
    
sorted and rotated array: (all the below can be solved efficiently using modified binary search)
    find minimum element
    find the rotation count
    
sorted and rotated array find if there is a pair with given sum
https://www.geeksforgeeks.org/given-a-sorted-and-rotated-array-find-if-there-is-a-pair-with-a-given-sum/
https://www.geeksforgeeks.org/find-maximum-value-of-sum-iarri-with-only-rotations-on-given-array-allowed/
https://www.geeksforgeeks.org/find-rotation-count-rotated-sorted-array/

Find a rotation with maximum hamming distance between both arrays
    approach 1:
        create a new array with douple the size and concatenate with itself
        now iterate in copy array and find hamming distance with each shift of copy array
    approach 2: constant space  O(n*2)
        We will compare elements of the original array sequence with its rotated versions. 
        The rotated versions of the array are achieved using shifted index method 
        where you compare elements at the original index with elements on the shifted index, 
        without requiring any extra space
    approach 3:
        
    

"""

