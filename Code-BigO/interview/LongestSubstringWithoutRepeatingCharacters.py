

# Given a string s, find the length of the longest 
# substring
#  without repeating characters.
def lengthOfLongestSubstring(s: str) -> int:
    if not(s):
        return 0
    elif(len(s) == 1):
            return 1
    se = set()
    l = 0
    max_l = 0
    for j in range (len(s)):
        print(f'j is : {s[j]}')
        if not(s[j] in se):
            se.add(s[j])
            l = l+1
            for i in range(j+1,len(s)):
                print(s[i])
                if not(s[i] in se):
                    se.add(s[i])
                    l = l+1
                    print(f'value of l is {l}')
                else:
                    se = set()
                    max_l = max(max_l,l)
                    print(f'value of max_l is {max_l}')
                    l = 0
                    break
    return max(max_l,l)

s = "jbpnbwwd"
print(lengthOfLongestSubstring(s))