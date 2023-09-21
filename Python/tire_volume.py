"""
The size of a car tire in the United States is represented with three numbers like this: 205/60R15. 
The first number is the width of the tire in millimeters. 
The second number is the aspect ratio. 
The third number is the diameter in inches of the wheel that the tire fits.

V = (π*w^2*a(w*a+2540*d))/10000000000

v is the volume in liters,
π is the constant PI, which is the ratio of the circumference of a circle divided by its diameter (use math.pi),
w is the width of the tire in millimeters,
a is the aspect ratio of the tire, and
d is the diameter of the wheel in inches.
"""
# width of the tire in millimeters
tire_size_mm = float(input('Enter the width of the tire in mm (ex 205):'))
# aspect ratio 
aspect_ratio = float(input('Enter the aspect ratio of the tire (ex 60):'))
# diameter in inches of the wheel that the tire fits
diameter_wheel = float(input('Enter the diameter of the wheel in inches (ex 15):')) 
import math
# Calculate volume of space inside a tire
volume_of_space = (math.pi*tire_size_mm**2*aspect_ratio*(tire_size_mm*aspect_ratio+2540*diameter_wheel))/10000000000
print(f'The approximate volume is {volume_of_space:.2f} liters')

