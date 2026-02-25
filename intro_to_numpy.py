import numpy as np

height = [1.73,1.68,1.92,1.45,1.67]
weight = [55,67,77,102,94]

np_height = np.array(height)
np_weight = np.array(weight)

bmi = np_weight / np_height ** 2

print(bmi)

print(bmi[1])
print(bmi > 23)


np2_d = np.array([[1,1,1,1,1],[2,2,2,2,0]])

print(np2_d.shape) # (2,5) 2 rows and 5 cols
#np_2d[0][2] = np_2d[0,2]
#np_2d[1, :]

import numpy as np

baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

# Create a 2D numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out the type of np_baseball
print(type(np_baseball))

# Print out the shape of np_baseball
print(np_baseball.shape)

#Subsetting 2D NumPy Arrays

#If your 2D numpy array has a regular structure, i.e. each row and column has a fixed number of values, complicated ways of subsetting become very easy. Have a look at the code below where the elements "a" and "c" are extracted from a list of lists.

# numpy
#import numpy as np
#np_x = np.array(x)
#np_x[:, 0]
#The indexes before the comma refer to the rows, while those after the comma refer to the columns. The : is for slicing; in this example, it tells Python to include all rows.

#np_baseball = np.array(baseball)

# Print out addition of np_baseball and updated
#print(np_baseball + updated)

# Create numpy array: conversion
#conversion = np.array([0.0254,0.453592,1])

# Print out product of np_baseball and conversion
#print(np_baseball * conversion)

#Average height = np.mean
#Median= np.median()

#corrcoef()
#np.std()


# import numpy as np

# # Create np_height_in from np_baseball
# np_height_in = np.array(np_baseball[:,0])

# # Print out the mean of np_height_in
# print(np.mean(np_height_in))

# # Print out the median of np_height_in
# print(np.median(np_height_in))


avg = np.mean(np_baseball[:,0])
print("Average: " + str(avg))

# Print median height
med = np.median(np_baseball[:,0])
print("Median: " + str(med))

# Print out the standard deviation on height
stddev = np.std(np_baseball[:,0])
print("Standard Deviation: " + str(stddev))

# Print out correlation between first and second column
corr = np.corrcoef(np_baseball[:,0],np_baseball[:,1])
print("Correlation: " + str(corr))