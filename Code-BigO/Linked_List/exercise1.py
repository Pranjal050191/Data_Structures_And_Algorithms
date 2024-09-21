obj1 = {'a': 'true'}
obj2 = obj1
obj1['a'] = 'booya'
del(obj1)
obj2 = 'hello'
# print(f'1. {obj1}')
print(f'2. {obj2}')
