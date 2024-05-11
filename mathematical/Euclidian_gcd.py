"""
Euclid’s algorithm (or Euclidean algorithm) is a method for efficiently finding the greatest common divisor (GCD) of two numbers. The GCD of two integers, X and Y, is the largest number that divides both X and Y without leaving a remainder.

The Euclidean algorithm is based on the principle that the greatest common divisor of two numbers does not change if the larger number is replaced by its difference with the smaller number.

"""

# Function to return gcd of a and b
# Time Complexity: O(Log min(a, b)) 
def gcd_basic(a:int, b:int):
    if a == 0 :
        print("{0:<15}:  {1:<3}".format("gcd_basic",b)) 
        return b
    return gcd_basic(b%a, a)

def gcd_recursive(a:int, b:int):
    while a!=0 and b!=0:
        temp=a
        a=b%a
        b=temp
    if a == 0:
        ans=b
    else:
        ans=a
    
    print("{0:<15}:  {1:<3}".format("gcd_recursive",ans)) 

gcd_basic(15,10)
gcd_recursive(15,10)