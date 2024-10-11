def fibonacci():
    cache = {}
    print('I am executed only once')
    def fibonacci_cached(n):
        if (n in cache):
            print('I am in cache')
            return cache[n]
        else:
            print('I am NOT in cache')
            if(n<=1):
                cache[n] = n
            else:
                cache[n] = fibonacci_cached(n-1) + fibonacci_cached(n-2)
            return cache[n]
    return fibonacci_cached

fb = fibonacci()
print(fb(8))
print(fb(10))
print(fb(8))
print(fb(8))
print(fb(9))
print(fb(9))

def fibonacci_loop(n):
    a = 0
    b = 1
    s = 0
    for i in range(n-1):
        s = a+b
        a = b
        b = s
    return s
print(fibonacci_loop(10))