#!/usr/bin/env python3


def longestCommonPrefix(strs):
    
    if len(strs) ==0:
        return ("")
    if len(strs) == 1:
        return strs[0]
    
    pref = strs[0]
    plen = len(pref)
    for word in strs[1:]:
        
        while pref != word[0:plen]:
            pref = pref[0:(plen-1)]
            plen -=1
            if plen == 0:
                return ("")
    
    return pref

assert(longestCommonPrefix(["colorado", "color", "cold"])) == "col"
assert(longestCommonPrefix(["a", "b", "c"])) == ""
assert(longestCommonPrefix(["spot", "spotty", "spotted"])) == "spot"
