import math


# method to calculate  volume of hemisphere
def vol_of_hemisphere(radius):
    result = (math.pi * radius * radius * radius)*(2 / 3)
    return result


# method to calculate  volume of cone
def vol_of_cone(radius, height):
    result = (math.pi * radius * radius * height) / 3
    return result


# method to calculate  volume of cylinder
def vol_of_cylinder(radius, height):
    result = math.pi * radius * radius * height
    return result


# method to calculate  volume of cuboid
def vol_of_cuboid(length, width, height):
    result = length * width * height
    return result
