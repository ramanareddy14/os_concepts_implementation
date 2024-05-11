def printarray(array, end, init, mid):  
    print('\n')
    for i in array:
        print('{:>10}'.format(i), end='')
    print('')    
    w1 = 10*(init +1)
    w2 = 10*(init-end)-1
    w3 = 10*(mid+1)
    print('{init:>{w1}}{end:>{w2}}'.format(init=init,end=end, w1 = w1, w2 = w2))
    print('{:>{w3}}'.format(array[mid], w3 = w3), '\n')


def searchInSortedMatrix(matrix, target):
    """
    This matrix appears to me like a plane of heights with the top left at a lower height
    and bottom right element as the highest peak of the plane

    Navigate the first row and find the element less or equal to the target
    then navigate the column and find the less or equal element 
    ...
    """


    row = 0
    col =0
    # binary search in this row
    init = 0
    end = len(matrix[0])-1
    
    row_init = 0
    row_end = len(matrix)-1

    while init <= end:
            mid = (init + end)//2
            printarray(matrix[row], end, init, mid)
            if matrix[row][mid] == target:
                #return [row,mid]
                print("bingo {}, {}".format(row,mid))
                break

            if matrix[row][mid] < target:
                # search in the right part of the column
                # but before checking the right element if 
                # index is valid and the next element is more than the target we need to 
                # stop searching in the row and move forward to search in the col
                print(matrix[row][mid], target, "in secondary flow control")
                if matrix[row][mid+1] > target:
                    print('-----')
                    row +=1
                    col = mid
                    init = col
                    break
                # else just search in the right part of the array
                init = mid+1 
            else :
                # search in the left part of the column
                print(matrix[row][mid], target, "in third flow control")
                end = mid -1
            
    print("\t\t row and column",row, col)
    
    row_init = row
    
    while row_init <= row_end:
            mid = (row_init + row_end)//2
            #printarray(matrix[row], row_end, row_init, mid)
            if matrix[mid][col] == target:
                #return [row,mid]
                print("bingo {}, {}".format(row,mid))
                break

            if matrix[mid][col] < target:
                # search in the right part of the column
                # but before checking the right element if 
                # index is valid and the next element is more than the target we need to 
                # stop searching in the row and move forward to search in the col
                print(matrix[mid][col], target, "in secondary flow control")
                if matrix[mid+1][col] > target:
                    print('-----')
                    row = mid
                    col += 1
                    row_init = col
                    break
                # else just search in the right part of the array
                row_init = mid+1 
            else :
                # search in the left part of the column
                print(matrix[mid][col], target, "in third flow control")
                row_end = mid -1
            
    print(row, col)

    



matrix =  [
    [1, 4, 7, 12, 15, 1000],
    [2, 5, 19, 31, 32, 1001],
    [3, 8, 24, 33, 35, 1002],
    [40, 41, 42, 44, 45, 1003],
    [99, 100, 103, 106, 128, 1004]
  ]
 
target = 31

print(searchInSortedMatrix(matrix, target))
