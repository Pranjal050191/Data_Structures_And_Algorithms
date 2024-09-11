from datetime import datetime
const = ['nemo']
everyone = ['sdsd','sdsd','nemo','sdfd','dfdfd x','etgvdb','xvdtra','xfe','cdfcz','sdfe','vdsfew','zxccsdx','zcsc','zccer']
large = ['nemo'] * 100000
def findnemo(array):
     start_time = datetime.now()
     for item in array:
         if (item == 'nemo'):
             print('Found nemo')
             break
     end_time = datetime.now()
     elapsed_time = (end_time - start_time).total_seconds() * 1000
     print(f'Time taken is + {elapsed_time}')           
findnemo(everyone) # O(n)  --> Linear time
boxes = [0,1,2,3,4,5]
def logFirstTwoBoxes(array):
    print(array[0]) # O(1)
    print(array[1]) # O(1)
logFirstTwoBoxes(boxes) #O(2)