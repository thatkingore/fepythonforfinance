# Using NumPy

import numpy as np


# Example with Lists

SP500_Monday = np.array([105.6, 1206.4, 137.6])
print(SP500_Monday)

SP500_Tuesday = np.array([(105.6, 1206.4, 137.6), (106.4, 1208.4, 139.9)], dtype = float)
print(SP500_Tuesday)

list = [1045.5, 111.5, 1024.7, 105.9, 126.7]
array_list = np.array(list)
print(array_list)


# Using Tuples

price_tuple = (1056.7, 1057.9, 2j)
print(price_tuple)

price_tuple_array = np.array(price_tuple)
print(price_tuple_array)

# Why use a tuple

print(price_tuple * 10)
print(price_tuple_array * 10)


# Creating Arrays

print(np.zeros((3, 4), dtype = np.int16))
print(np.ones((2, 3), dtype = np.int16))
print(np.linspace(0, 2, 9))

# Inspecting Arrays

a = np.array([1, 2, 3])

print(a.shape)
print(len(a))
print(a.ndim)
print(a.size)
print(a.dtype)

del a

# Aggregate Functions

a = np.array([105.4, 205.6, 307.5, 1406.5, 1508.7])
print(a)

print(a.sum())
print(a.mean())
print(a.min())
print(a.max())
