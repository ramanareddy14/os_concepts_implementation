"""
Stack basic problems

patenthesis check
for every character in the string
    if open character push it into stack(list)
    if close character 
        if stack is empty return false
        if last character in stack matches curent character pop 
return True if stack is empty or else return false
"""


def parenthesis(string):
    left   = "({["
    right  = ")}]"
    
    if string is None:
        return True
    stack = []
    
    for char in string:
        print("char - {} :".format(char),end='',flush = True)
        if char not in left and char not in right:
            print("non bracket character-:{}:-stack-{}".format(char,stack))
            continue
        elif char in left:
            stack.append(char)
            print("appended character-:{}:-stack-{}".format(char,stack))
        elif char in right:
            if len(stack) == 0:
                print("stack lenght is zero-stack:{}".format(stack))
                return False
            # it right matches doesn't correct opening parenthesis return true
            if right.index(char) != left.index(stack.pop()):
                return False
            else:
                print("popped character-:{}:".format(stack))
    
    # by now all the right characters should be matched
    # if the stack is still empty then it a failure
    if len(stack) > 0 :
        return False
    return True

str1 = "( )(( )){([( )])}"
str2 = "((( )(( )){([( )])}))"
str3 =  ")(( )){([( )])}"
str4 =  "({[ ])}"
str5 =  "("
                
print("\n parenthesis : {}.".format(parenthesis(str2)))