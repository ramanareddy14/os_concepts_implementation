'''
Power set P(S) of a set S is the set of all subsets of S. 
For example S = {a, b, c} then P(s) = {{}, {a}, {b}, {c}, {a,b}, {a, c}, {b, c}, {a, b, c}}.

If S has n elements in it then P(s) will have 2^n elements
'''

'''
Solution 1:
    For a given set[] S, the power set can be found by generating all binary numbers between 0 and 2^(n-1), where n is the size of the set. 
    For example, for the set S {x, y, z}, generate all binary numbers from 0 to 2^(3-1)
    and for each generated number, the corresponding set can be found by considering set bits in the number.
    
Time Complexity: O(n * 2^n)
Auxiliary Space: O(1)
'''

'''
Solution 2: backtracking
    We can use backtrack here, we have two choices first consider that element then don’t consider that element. 
    
Time Complexity: O(n * 2^n)
Auxiliary Space: O(n)
    
'''
    

#-------------------------------- Recursive solutions ---------------------------------------------------------

'''
Method 1: 
    The idea is to fix a prefix, generate all subsets beginning with the current prefix. 
    After all subsets with a prefix are generated, replace the last character with one of the remaining characters.  

'''

# str : Stores input string
# curr : Stores current subset
# index : Index in current subset, curr
def powerSet(str, index, curr):
    
    # base case
    if index == len(str):
        return
    
    # first print current subset
    print(curr)
    
    # try appending remaining characters to current subset
    for i in range(index + 1, len(str)):
        curr += str[i]
        powerSet(str, i, curr)
        
        # once all subsets beginning with initial 'curr' are printed
        # remove last character to consider a different prefix of subsets
        curr = curr.replace(curr[len(curr) - 1], "")

str = "abc";
powerSet(str, -1, "")
'''
a
ab
abc
ac
b
bc
c
'''
 