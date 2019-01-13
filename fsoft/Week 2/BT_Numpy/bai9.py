import numpy as np 
import math
#B1
lengths = np.array([1,4,6,9,11,10])
widths = np.array([2,3,7,4,8,12])

rectange = lengths * widths
print(rectange)

#B2
A = np.array([34, 56, 32, 87, 65, 29])
B = np.array([26, 78, 45, 38, 85, 92])
C = A >B
print(C)

#B3
radius = np.array([12, 24.5, 23.5, 26.7, 30, 19.4, 25.6])
result = radius[radius> 25]
circle_areas = math.pi*result**2
print(circle_areas)
