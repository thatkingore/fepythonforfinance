# Using NumPy

import numpy as np


# Example

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
