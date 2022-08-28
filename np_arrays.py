"""
Numpy arrays are great alternatives to Python Lists
It allows for arithmetic operations to be done on arrays
"""

# Import the numpy package as np
import numpy as np

# Create 2 new lists height and weight
height = [1.87,  1.87, 1.82, 1.91, 1.90, 1.85]
weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

# Create 2 numpy arrays from height and weight

np_height = np.array(height)
np_weight = np.array(weight)

print(np_height)

# Calculate bmi
bmi = np_weight / np_height ** 2

# Print the result
print(bmi)

# Print only those observations above 23
print(bmi[bmi > 23])


# Second exercise

weight_kg = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]


# Create a numpy array np_weight_kg from weight_kg

np_weight_kg = np.array(weight_kg)

# Create np_weight_lbs from np_weight_kg 2.2 lbs per kg
np_weight_lbs = np_weight_kg * 2.2

print(np_weight_lbs)
