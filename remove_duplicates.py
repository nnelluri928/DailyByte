'''
This question is asked by Facebook. Given a string s containing only lowercase letters, continuously remove adjacent characters that are the same and return the result.

Ex: Given the following strings...

s = "abccba", return ""
s = "foobar", return "fbar"
s = "abccbefggfe", return "a"
'''
def compact(s):
    stack = []
    for char in s:
        if stack and char == stack[-1]:
            stack.pop()
        else:
            stack.append(char)
    return ''.join(stack)

s = "aabbcc"
print(compact(s))
s = "foobar"
print(compact(s))
s = "abccbefggfe"
print(compact(s))