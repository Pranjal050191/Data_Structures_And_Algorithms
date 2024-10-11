# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
def firstUniqChar(s: str) -> int:
    di = {}
    for i in range(len(s)):
        if (s[i] in di):
            di[s[i]] = di[s[i]] + 1
        else:
            di[s[i]] = 1
    for i in range(len(s)):
        if di[s[i]] == 1:
            return i
    return -1

s = "aabb"
print(firstUniqChar(s))
