import numpy as np

a = np.array([(1, 2, 3), (4, 5, 6)])
b = np.array([(7, 8, 9), (2, 4, 8)])

print(f'Sum of array a and b is: {np.sum(a+b)}')
print('----------------')
print(f'Difference of array "a" and "b" is: {np.sum(a-b)}')
print('----------------')
print(f'Multiply of array "a" and "b" is: {np.sum(a*b)}')
print('----------------')
print(f'Divide of array "a" and "b" is: {np.sum(a/b)}')

print('Concatenation of arrays that are vertical stacking and horizontal stacking')
print(f'Vertical stacking is: \n {np.vstack((a,b))}')
print('----------------')
print(f'Horizontal stacking is: \n {np.hstack((a,b))}')
print()
print(f'Convert array  "a" into single row: \n {a.ravel()}')


