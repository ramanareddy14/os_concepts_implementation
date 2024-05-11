"""
We are given a number N. Find the number of ways of expressing N as a sum 1, 3, and 4.

Example:
– N = 5
– Number of ways = 6
– Explanation: There are 6 ways to express N. {4,1}, {1,4}, {1,3,1}, {3,1,1}, {1,1,3}, {1,1,1,1,1}


"""

#Function to solve Number Factor Problem using top down (memoization) approach
def numberFactor(n, tempDict):
    if n in (0,1,2):
        return 1
    elif n == 3:
        return 2
    else:
        subPart1 = numberFactor(n-1, tempDict)
        subPart2 = numberFactor(n-3, tempDict)
        subPart3 = numberFactor(n-4, tempDict)
        tempDict[n] = subPart1+subPart2+subPart3
        return tempDict[n]


#Function to solve Number Factor Problem using Botton up (Tabulation ) approach
# First few solutions are filled in the array and next solutions is calculated using previous solutions
def numberFactor_1(n):
   tempArr = [1,1,1,2]
   for i in range(4, n+1):
       tempArr.append(tempArr[i-1]+tempArr[i-3]+tempArr[i-4])
   return tempArr[n]

#print("Number factor using DP.Memoization: ",numberFactor(5, {}))
#print("Number factor using DP.Tabulation: ",numberFactor_1(5))


"""
House Robber
We are given N number of houses along a street, each having some amount of money. 
A thief can not steal from adjacent houses. Find the maximum amount that can be stolen.

topdown -- max of firsthouse, skipfirst house
Bottomup -- initialize temparray of zeros, take two lenghts extra zeros
            iterate over the houses in reverse 
                array[i] = max(house[i] + arr[i+2], arr[i+1])
"""
def houseRobber(houses,i,topdown):
    # validation and initial values
    if i >= len(houses):
        return 0
    else:
        firsthouse = houses[i] + houseRobber(houses, i+2, topdown)
        skipfirsthouse = houseRobber(houses, i+1, topdown)
        topdown[i] = max(firsthouse, skipfirsthouse)
    return topdown[i]

def houseRobber_1(houses,i):
    tempArr = [0] * (len(houses)+2)
    
    for i in range((len(houses)-1),-1, -1):
        # current max = max of this robbing this house / skipping this house 
        tempArr[i] = max(houses[i] + tempArr[i+2], tempArr[i+1])
    return tempArr[0]
    


houses = [6,7,1,30,8,2,4]
#print("House Robber DP.Memoization: ",houseRobber(houses, 0, {}))
#print("House Robber DP.Tabulation : ",houseRobber_1(houses, 0))


"""
We are given two strings S1 and S2. Convert S2 to S1 using delete, insert or replace operations. Find the minimum number of edit operations

Example:
– S1 = “table”
– S2 = “tbres”
– Output = 3
– Explanation: Insert “a” to second position, replace “r” with “l”, and delete “s”.

Memoization - 
https://pythonwife.com/dynamic-programming-in-python/#:~:text=Dynamic%20Programming(DP)%20is%20an,optimal%20solution%20to%20the%20subproblems.
"""

