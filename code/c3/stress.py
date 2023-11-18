def calculate_stress(force, area = 500):
    '''
        Takes in a force and area and returns stress.
    '''
    stress = force / area
    return stress

# We can pass a default value to the parameter

# Positional Arguements
print(calculate_stress(50))
print(calculate_stress(50, 1000))

# Keyword Arguments
print(calculate_stress(area=100, force=50))

# Variables number of arguments

def calculate_total_force(*pressures, area = 500):
    total_force = sum(pressures) * area
    return total_force

#print(calculate_total_force(10, 20, 30, area = 2000))

# Lambda Functions (aka anonymous functions) - Used for small and temporary purposes

square = lambda x,y: x**y

print(f"{square(5,2)}")