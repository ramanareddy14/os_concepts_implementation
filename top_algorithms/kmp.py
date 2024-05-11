"""
Partial match table:
    
    Partial match table will have same cells as length of string at starting
    If I'm looking at 4th cell I'm interested only in first 4 characters only 
    
    Proper Prefixes : “S”, “Sn”, “Sna”, and “Snap” are all the proper prefixes of “Snape”.
    Proper Sufixes  : “agrid”, “grid”, “rid”, “id”, and “d” are all proper suffixes of “Hagrid”.
    
    The length of the longest proper prefix in the (sub)pattern that matches a proper suffix 
    in the same (sub)pattern.
                chars:  | a | b | a | b | a | b | c | a |
                index:  | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 
                value:  | 0 | 0 | 1 | 2 | 3 | 4 | 0 | 1 |
                
    Some _conclusions:
        1. The first element doesn't have prefixes or suffixes hence 0
        2. 
        
How to use partial match table:
    
"""

def computeLPSarray(pattern):
    """
    

    """
    pmt_value = [0]*len(pattern)
    length = 0 # length of the previous longest prefix suffix
    i = 1
 
    # the loop calculates lps[i] for i = 1 till end of pattern 
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            pmt_value[i] = length
            i += 1
        else:
            # This is tricky. Consider the example.
            # AAACAAAA and i = 7. The idea is similar
            # to search step.
            if length != 0:
                length = pmt_value[length-1]
 
                # Also, note that we do not increment i here
            else:
                pmt_value[i] = 0
                i += 1
    return  pmt_value
              

# Function to implement the KMP algorithm
def KMP(text, pattern):
 
    # base case 1: pattern is empty
    if not pattern:
        print('The pattern occurs with shift 0')
        return
 
    # base case 2: text is empty, or text's length is less than that of pattern's
    if not text or len(pattern) > len(text):
        print('Pattern not found')
        return
 
    
    """
    Step 1: building partial match table
    """
    pmt_value = computeLPSarray(pattern)    
    print(pmt_value)
    print(list(pattern))
    
    
    

# Program to implement the KMP algorithm in Python
if __name__ == '__main__':
 
    text = 'ABCABAABCABAC'
    pattern = 'ABBABA'
 
    KMP(text, pattern)