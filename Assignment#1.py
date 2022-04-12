"Learned how to get user inputs, mathematical calculations, and printing"

#1. Write a program to convert from LBS (user input) to KG
lbs = (float(input("Enter your weight in lbs:")))
kg = (lbs * 0.45359237)
print("Your weight in kg is:", kg, '\n')


#2. Write a program to convert distance (in feet (user input)) to inches, yards and miles
feet = (float(input("Enter a distance (in feet):")))
inches = (feet * 12)
yards = (feet / 3)
miles = (feet / 5280)
print("Feet conversion to inches:", inches, '\n',"Feet conversion to yards:", yards, '\n',"Feet conversion to miles:", miles, '\n')

#3. Write a program to calculate volume of Cube/Sphere/RectangularPrism
cube_measurement = (float(input("Enter either the length/width/height (make sure to input only one) of the the cube:")))
cube_volume = cube_measurement**3
print("Cube Volume:", cube_volume, '\n')

radius = (float(input("Enter the radius of the sphere:")))
sphere_volume = (4/3*3.141592) * radius**3
print("Sphere Volume:", sphere_volume, '\n')

length = (float(input("Enter the length of the rectangular prism:")))
width = (float(input("Enter the width of the rectangular prism:")))
height = (float(input("Enter the height of the rectangular prism:")))
rectangular_prism_volume = length * width * height
print("Rectangular Prism Volume: ", rectangular_prism_volume)
