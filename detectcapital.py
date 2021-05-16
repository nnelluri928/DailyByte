#!/usr/bin/env python3

def detectCapitalUse(s):

	return s.isupper() or s.islower() or s.istitle() 

print(detectCapitalUse("USA"))
print(detectCapitalUse("Calvin"))
print(detectCapitalUse("compUter"))
print(detectCapitalUse("coding"))

def detectCapitalUse1(s):
	if s.upper() == s:
		return True
	elif s.lower() == s:
		return True
	elif s[0].upper() == s[0] and s[1:].lower() == s[1:]:
		return True
	else:
		return False
print(detectCapitalUse1("USA"))
print(detectCapitalUse1("Calvin"))
print(detectCapitalUse1("compUter"))
print(detectCapitalUse1("coding"))
