import numpy as np

a = np.array([(1, 2, 3), (4, 5, 6)])
print(a)
print('---------------------------------')
print(f'Dimension of array is {a.ndim}')

print(f'Byte size of each elements is {a.itemsize}')

print(f'Datatype of element is {a.dtype}')

print(f'The total length of an array is {a.size}')

print(f'Rows and columns of an array is {a.shape}')
print('---------------------------------')
#a = a.reshape(3, 2)
#print(f'Reshape of array is: \n {a}')
print('---------------------------------')
print(a[0:, 1])      #0th list and 1st index element of all list
print('---------------------------------')
b = np.linspace(1, 20, 5)      #Divide into 5 equal half from 1 to 20 excluding 20
print(b)
print('---------------------------------')
print(f'The maximum value of array a is: {a.max()}')
print(f'The minimum value of array a is: {a.min()}')
print('---------------------------------')
print(f'Sum of Columns is : {a.sum(axis=0)}')
print(f'Sum of Rows is : {a.sum(axis=1)}')
print('---------------------------------')
print(f'Square root of each element is: \n {np.sqrt(a)}')
print()
print(f'Standard Deviation of an array is: {np.std(a)}')




