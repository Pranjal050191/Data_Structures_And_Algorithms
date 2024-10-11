# Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.

# For example:

# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28 
def titleToNumber(columnTitle: str) -> int:
    result = 0
    l = len(columnTitle)
    for i in range(l):
        print(f'Pranjal: {ord(columnTitle[i])-ord('A')+1}')
        result = result + ((ord(columnTitle[i])-ord('A')+1)*pow(26,l-i-1))
    return result
        
print(titleToNumber("ZY"))