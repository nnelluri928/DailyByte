'''
This question is asked by Google. You are given two strings, s and t which only consist of lowercase letters. i
t is generated by shuffling the letters in s as well as potentially adding an additional random character. 
Return the letter that was randomly added to t if it exists, otherwise, return ’ ‘.
Note: You may assume that at most one additional character can be added to t.

Ex: Given the following strings...

s = "foobar", t = "barfoot", return 't'
s = "ide", t = "idea", return 'a'
s = "coding", t "ingcod", return ''
'''
from collections import Counter
def differnce(s,t):
    if len(s) == 1:
        return s
    count = Counter(s)
    for char in t:
        if char in count:
            count[char] -=1
        else:
            count[char] = 1
    for key,val in count.items():
        if val > 0 or val < 0:
            return key
    return ''
s = "foobar";  t = "barfoot"
print(differnce(s,t))
s = "ide"; t = "idea"
print(differnce(s,t))
s = "coding"; t= "ingcod"
print(differnce(s,t))
s = 'a'; t = 'aa'
print(differnce(s,t))