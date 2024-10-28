# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack
# , or -1 if needle is not part of haystack.
def strStr(haystack: str, needle: str) -> int:
    l = len(needle)
    for i in range(len(haystack)):
        print(f'{haystack[i]} and {needle[0]}')
        print(f'{haystack[i:i+l]}')
        if(haystack[i] == needle[0]):
            print(f'In first if condition {i} ,{haystack[i:l]} and {needle}')
            if(haystack[i:i+l] == needle):
                return i
    return -1

haystack = "hello"
needle = "ll"
print(strStr(haystack,needle))
 