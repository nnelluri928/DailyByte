'''
This question is asked by Amazon. 
Given two strings s and t, which represents a sequence of keystrokes, 
where # denotes a backspace, 
return whether or not the sequences produce the same result.

Ex: Given the following strings...

s = "ABC#", t = "CD##AB", return true
s = "como#pur#ter", t = "computer", return true
s = "cof#dim#ng", t = "code", return false
'''
def backspaceCompare(s, t):
  
    s_stack = []
    t_stack = []
    
    for char in s:
        if char !='#':
            s_stack.append(char)
        if char == '#':
            if not s_stack:
                continue
            s_stack.pop()
    for char in t:
        if char !='#':
            t_stack.append(char)
        if char == '#':
            if not t_stack:
                continue
            t_stack.pop()
            
    return ''.join(s_stack) == ''.join(t_stack)
s = "ABC#"; t = "CD##AB"
print(backspaceCompare(s, t))
s = "como#pur#ter"; t = "computer"
print(backspaceCompare(s, t))
s = "cof#dim#ng"; t = "code"
print(backspaceCompare(s, t))