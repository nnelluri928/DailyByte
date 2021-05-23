'''
This question is asked by Microsoft. Given a string, return the index of its first unique character. If a unique character does not exist, return -1.

Ex: Given the following strings...

"abcabd", return 2
"thedailybyte", return 1
"developer", return 0
'''
def unique(s):
    lib = {}
    for char in s:
        if char not in lib:
            lib[char] =1
        else:
            lib[char] += 1
    for k,v in lib.items():
        if v == 1:
            return s.index(k)
    return -1
s = "abcabd"
print(unique(s))
s = "thedailybyte"
print(unique(s))
s = "developer"
print(unique(s))
