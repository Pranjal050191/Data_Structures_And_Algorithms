# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters 
# and removing all non-alphanumeric characters, it reads the same forward and backward. 
# Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.
import re
def isPalindrome(s: str) -> bool:
    s1 = re.sub(r'[^a-zA-Z0-9]','',s)
    s2 = s1.lower()
    idx1 = 0
    idx2 = len(s2)-1
    while(idx1 <= idx2):
        if(s2[idx1] == s2[idx2]):
            idx1 = idx1 + 1
            idx2 = idx2 - 1
        else:
            return False
    return True

s = " "
print(isPalindrome(s))

