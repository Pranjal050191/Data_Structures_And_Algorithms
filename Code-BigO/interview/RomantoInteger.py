# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
def romanToInt(s: str) -> int:
    roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    for i in range(len(s)-1):
        if roman_map[s[i]] < roman_map[s[i + 1]]:
        # Subtract the current value
            result = result - roman_map[s[i]]

        else:
        # Add the current value
            result = result + roman_map[s[i]]
    result = result + roman_map[s[len(s)-1]]
    return result

s = "MCMXCIV"
print(romanToInt(s))
