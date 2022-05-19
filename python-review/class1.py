# The any() function returns True if any item in an iterable are true, otherwise it returns False
some_list = [None, 0, False]
print(any(some_list))  # False
some_list = [0, 0, None, '', False, 1]
print(any(some_list))  # True

# In line for
x = [1, 2, 3, 4, 5]
y = [i**2 for i in x]
#print(y)

# Matrix for in line
matrix = [[j for j in range(0,2)] for i in range(0,2)]
print(matrix)
