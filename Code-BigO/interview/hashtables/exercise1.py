class user:
    age = 54
    name = 'Kylie'
    magic = True
    def scream():
        print('ahhhh!!')
print(user.age) # O(1)
user.spell = 'aabra ka dabra' #O(1)
print(user.scream()) #O(1)
print(user.__dict__)
#print(vars(user)) output is same as above