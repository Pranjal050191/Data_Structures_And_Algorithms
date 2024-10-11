def memoizedAddTo80():
    cache = {}  # This cache will persist due to closure
    print('I am only called once to initialize the environment.')
    # Inner function that accepts `n` as an argument
    def add_to_80(n):
        if n in cache:
            return cache[n]
        else:
            print('long time')
            cache[n] = n + 80
            return cache[n]
    
    # Return the inner function (closure)
    return add_to_80

# Create a reference to the inner function, `memo_add` is now the inner function `add_to_80`
memo_add = memoizedAddTo80()

# Now `memo_add` is the same as calling `add_to_80`, so it accepts `n` as argument
print(memo_add(5))  # First time, prints 'long time', calculates 85
print(memo_add(5))  # Second time, cached result, returns 85 without recalculating
print(memo_add(5))
print(memo_add(5))
print(memo_add(5))
print(memo_add(6))
print(memo_add(6))
print(memo_add(6))