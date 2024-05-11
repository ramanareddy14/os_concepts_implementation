"""
Geek is in a maze of size N * M. Each cell in the maze is made of either ‘.’ or ‘#’. 
An empty cell is represented by ‘.’ and an obstacle is represented by ‘#’. 
The task is to find out how many different empty cells he can pass through If Geek starts at cell (R, C) 
and avoids the obstacles and he can move in any of the four directions but he can move up at most U times 
and he can move down at most D times. 


#Given N*M , current position R,C, limits U,D

counter =0
if current pos is . counter++
else if currenr pos is # or R>=N or R<0 or C >= M or C <0 or U<0 or D<0
    return counter

 return max(move left, move right, move up , move down)

"""

def solution(mat, N,M, R,C, U,D, counter=0):
    
    # if current step is either a block or if stepping out of matrix return 0
    if R>=N or R<0 or C >= M or C <0 or U<0 or D<0 or mat[R][C] == '#':
        return counter
    
    # for current valid step increase counter by 1 and mark as visited
    mat[R][C] = '#'
    counter += 1
    print(R,C, counter," U:{},D{}".format(U,D))
    # return max of down, up, left, right 
    return max(solution(mat, N, M, R+1, C, U, D-1, counter), solution(mat, N, M, R-1, C, U-1, D,counter), solution(mat, N, M, R, C-1, U, D,counter), solution(mat, N, M, R, C+1, U, D, counter))

    


arr = [['.','.','.'],['.','#','.'],['.','.','.'],['#','.','.']]

print(solution(arr,4,3,0,1,1,2))


    
    
    






