'''
This question is asked by Google. 
Given a string only containing the 
following characters (, ), {, }, [, and ] return 
whether or not the opening and closing characters are in a valid order.

Ex: Given the following strings...

"(){}[]", return true
"(({[]}))", return true
"{(})", return false
'''

def isValid(s):
    stack = []
    lib = {")":"(","}":"{","]":"["}
    
    for char in s:
        if char in lib:
            if stack and stack[-1] == lib[char]:
                stack.pop()
            else:
                return False
        else:
            stack.append(char)
    
    return True if not stack else False
s = "(){}[]"
print(isValid(s))
s = "(({[]}))"
print(isValid(s))
s = "{(})"
print(isValid(s))