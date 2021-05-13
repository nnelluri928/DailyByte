#!/usr/bin/env python3
import re

def valid_palindrome(s):

	return s == s[::-1]
s = 'level'
assert valid_palindrome(s) == True
s1 = "algorithm"
assert valid_palindrome(s1) == False

def valid_palindrome1(s):
	new_s = "".join(re.split("[,.:\s]",s))
	return new_s.lower() == new_s.lower()[::-1]

s = "A man, a plan, a canal: Panama."
assert valid_palindrome1(s) == True
