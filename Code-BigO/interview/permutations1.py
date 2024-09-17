def get_permutations(string, i=0, result=None):
    if result is None:
        result = set()  # To store unique permutations
    
    if i == len(string):
        result.add(''.join(string))  # Store the permutation in the set
    
    for j in range(i, len(string)):
        words = [c for c in string]
        words[i], words[j] = words[j], words[i]  # Swap
        get_permutations(words, i+1, result)  # Recur

    return sorted(result)  # Return sorted list of unique permutations

unique_permutations = get_permutations('Pran')
print(unique_permutations) 
