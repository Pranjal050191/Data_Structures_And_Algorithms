# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".
def longestCommonPrefix(strs: list[str]) -> str:
   strs_sort = sorted(strs)
   l = len(strs_sort)
   i = 0
   while(i < len(strs_sort[0]) and i < len(strs_sort[l-1]) and strs_sort[0][i] == strs_sort[l-1][i]):
      i=i+1
   return strs_sort[0][:i]


strs = ["dog","racecar","car"]
print(longestCommonPrefix(strs))
        

       
