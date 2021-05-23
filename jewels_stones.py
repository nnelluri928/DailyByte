
'''
This question is asked by Amazon. Given a string representing 
your stones and another string representing a list of jewels, 
return the number of stones that you have that are also jewels.

Ex: Given the following jewels and stones...

jewels = "abc", stones = "ac", return 2
jewels = "Af", stones = "AaaddfFf", return 3
jewels = "AYOPD", stones = "ayopd", return 0
'''

def stones_jewels(jewels,stones):    
        count = {}
        ans = 0
        for s in jewels:
            if s not in count:
                count[s] = 1
            else:
                count[s] +=1
        
        for j in stones:
            if j in count:
                ans += 1
        return ans
jewels = "abc" ; stones = "ac"
assert stones_jewels(jewels,stones) == 2
jewels = "Af" ; stones = "AaaddfFf"
assert stones_jewels(jewels,stones) == 3
jewels = "AYOPD"; stones = "ayopd"
assert stones_jewels(jewels,stones) == 0