import re

text = "Hello World World Hello"
result = re.search(r"World", text)  # Searches the entire string
print(result)  # Output: <re.Match object; span=(6, 11), match='World'>

# text = "Hello World"
index = text.find("World")  # Searches for 'World' in the string
print(index)  # Output: 6 (The starting index of 'World')

result = re.match(r"Hello", text)  # Matches at the beginning of the string
print(result)  # Output: <re.Match object; span=(0, 5), match='Hello'>

result = re.findall(r"Hello", text)  # Finds all sequences of digits
print(result)  # Output: ['Hello', 'Hello']
