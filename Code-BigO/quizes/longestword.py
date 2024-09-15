import re
def LongestWord(sen):

  # code goes here
  cleaned_string = re.sub(r'[^a-zA-Z\s]', '', sen)
  splitted_string = cleaned_string.split()
  global_length = 0
  current_length = 0
  for item in splitted_string:
    current_length = len(item)
    if(current_length > global_length):
      global_length = current_length
      sen = item
  return sen

# keep this function call here 
print(LongestWord(input()))