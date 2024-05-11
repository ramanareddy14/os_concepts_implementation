"""
Given a matrix, clockwise rotate elements in it.
    
1. Inplace rotate square matrix by 90 in anti-clock wise
    approach1:
        last column becomes first row ...
        first column becomes last row
        
    approach 2:
        rotate the array in form of squares, dividing the matrix into inner squares or cycles.
        
    approach 3:  O(R*C)
        mat[i].reverse()  #reverse every individual row
        
        def transpose(arr):  # Transpose the matrix (rows becomes columns)
        for i in range(R):
            for j in range(i, C):
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]  
            
            
2. Rotate a matrix by 180 degrees 
    approach 1:
        first row becomes last row ans so on 
        
    approach 2:
        only print the view of rotated matrix-- mat[::-1][::]
    
3. Check if rows are circular rotations of each other
    approach 1:
        create a string with first row elements and concatenate with itself
        for each other rows check if the row string is a substirng of above string
        
4. sort the matrix
    approach 1:
        take a temp array arr of n*n and sort and place one by one into the matrix
        
5. find max number of 1's in a 2D boolean sorted matrix
    approach 1:
        for each row find the index of 1 by doing a binary search, so that you can get count
        complexity is O(mLogn)
    approach 2: efficient  O(m+n)
        for first row find the index of first 1
        move down to second row if it is 0 ignore else move to left to find 0-1
        The time complexity is O(m+n) because we can possibly go as far left as we came ahead in the first step.

6. Median in a row-wise sorted matrix
    approach 1:

7. Find distinct elements common to all tows: caution check for dupolicates
    approach : map efficient method
        for each element of first row add to map key-element, value-row number
        for each other row elements if present in map update value(so now duplicates can't effect map val')
        for last row if element is present with val n-2 then print them
        O(m*n) aux space O(m) because we store no more than m elements in map
        
8. print given matrix in rings  form
    approach 1: 
            first outer spiral  0 to n(+=spiral) , 1 to m(+-spiral), n-2 - 0(+-spiral), m-2 to 1(+-spiral)
            where spiral = min(n,m)/2 + min(n,m)%2 // 3 should have 2 and 4 should have 2 spirals
            
9. print the given matrix in spiral form
    approach 1:
        print  0 to n 
    print in counter clockwise spiral form
    
10. maximum sum path in a matrix, only moved one down or one diagonally down
    approach 1: space O(m*n) and complexity O(m*n)

"""