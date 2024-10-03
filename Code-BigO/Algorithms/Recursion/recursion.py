counter = 0
def inception():
    global counter
    counter = counter + 1
    print(counter)
    if (counter > 3):
        return 'done!!'
    inception()
print(inception())