def permute(word, start, end, result):
    if start == end:
        # When a permutation is complete, add it to the result set
        result.add(''.join(word))
    else:
        seen = set()
        for i in range(start, end + 1):
            print(f'Pranjal 1 {word[i]}')
            if word[i] not in seen:
                seen.add(word[i])
                print(f'Pranjal 2 {seen}')
                # Swap characters at position `start` and `i`
                word[start], word[i] = word[i], word[start]
                # Recur with the next position
                permute(word, start + 1, end, result)
                # Backtrack to restore the original order
                word[start], word[i] = word[i], word[start]

def generate_unique_permutations(word):
    result = set()
    word_list = list(word)  # Convert the word to a list of characters
    permute(word_list, 0, len(word_list) - 1, result)
    return sorted(result)  # Sort the result to have a consistent order

# Example usage
word = "aab"
unique_permutations = generate_unique_permutations(word)
print(unique_permutations)
