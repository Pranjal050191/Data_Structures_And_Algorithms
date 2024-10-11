# Given two strings s and t, return true if t is an 
# anagram
#  of s, and false otherwise.

def isAnagram(s: str, t: str) -> bool:
        s1 = {}
        for i in range(len(s)):
            if s[i] in s1:
                s1[s[i]] = s1[s[i]] + 1
            else:
                s1[s[i]] = 1
        s2 = {}
        for i in range(len(t)):
            if t[i] in s2:
                s2[t[i]] = s2[t[i]] + 1
            else:
                s2[t[i]] = 1
        for key in s1:
            if not(key in s2) or not(s1[key] == s2[key]):
                print(f'{key} not in s2 or s1[{key}] not equal to s1[{key}]')
                return False
        for key in s2:
            print(f'Comparing values: {s2[key]} with s1[key]')
            if not(key in s1) or not(s1[key] == s2[key]):
                return False
        return True

s="anagram"
t="nagaram"
print(isAnagram(s,t))