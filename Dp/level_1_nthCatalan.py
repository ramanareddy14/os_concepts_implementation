# -*- coding: utf-8 -*-
"""
Given a number N. Find the minimum number of operations required to reach N starting from 0. 
You have 2 operations available:

Double the number
Add one to the number
"""
class Solution:
    def minOperation(self, n):
        # code here 
        '''
        MINIMUM OPERATIONS IS 
        '''
        operations = 0
        while n > 0:
            if n % 2 == 1:
                # if number is odd it can be rached by adding a number
                operations +=1
                n -= 1
            
            else:
                operations +=1
                n /= 2
                
        return operations

'''
Given string s containing characters as integers only, the task is to delete all characters of this string
in a minimum number of steps wherein one step you can delete the substring which is a palindrome. 
After deleting a substring remaining parts are concatenated.

Input: s = "2553432"
Output: 2
Explanation: In first step remove "55", 
then string becomes "23432" which is a 
palindrome.


'''


'''
Given an infinite supply of each denomination of Indian currency 
{ 1, 2, 5, 10, 20, 50, 100, 200, 500, 2000 } and a target value N.
Find the minimum number of coins and/or notes needed to make the change for Rs N.


Example 1:

Input: N = 43
Output: 20 20 2 1
Explaination: 
Minimum number of coins and notes needed 
to make 43. 

For a real life situation we can give out the maximum denominations possible 


For programaticak situations with unrealistic currency denominations we can build up a DP matrix 
and for each row we can fill up with least currency possible
'''
class Solution:
    def minPartition(self, N):
        currency_denominations = [1, 2, 5, 10, 20, 50, 100, 200, 500, 2000 ]
        
        idx = len(currency_denominations) -1
        toreturn = []
        
        while N > 0 and idx >=0:
            if currency_denominations[idx] <= N:
                count = (N//currency_denominations[idx]  ) # 43//20 gives 2 20's
                N %= currency_denominations[idx]   # 43 % 20 gives 3
                for i in range(count):
                    toreturn.append(currency_denominations[idx])
                
            idx -=1
                
        print(toreturn)
        return toreturn
                
sol = Solution()
sol.minPartition( 43)


'''
A frog jumps either 1, 2, or 3 steps to go to the top. 
In how many ways can it reach the top. As the answer will be large find the answer modulo 1000000007.

Solution 1 : recursion Fun(n) = Fun(n-1) + Fun(n-2) + Fun(n-3) 
        time : O(2^N) and same stack space

Solution 2: using tabulation method
            arr[0] = 1  # to reach step 1
            arr[1] = 2 # to reach step 2
            arr[2] = 4 # to reach step 3
            
            and fill up the array from here after filling the base conditions

'''