# Calculates volume of the Piston 

'''
    Volume of the Cylinder = PI * r^2 * h
'''

import math

# Car 1
piston_diameter = 74.50
piston_count = 4
engine_type = "Inline"
stroke_length = 80

total_volume = ((piston_diameter / 2) ** 2) * stroke_length * 3.1415

def calculate_piston_volume(diameter, stroke_lenth):
    radius = diameter / 2
    stroke_area = math.pi * (radius**2)
    return stroke_area * stroke_length

total_cylinder_volume = calculate_piston_volume(piston_diameter, stroke_length) * piston_count

#print(total_cylinder_volume)

# Control Flow 

total_volume = 1600

if total_volume > 1500:
    category = "large"
elif total_volume > 1000:
    category = "medium"
else:
    category = "small"


print(f"The engine category is {category}.")