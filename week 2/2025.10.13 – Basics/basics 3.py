# calculate 8x + 7xyz + 3z
x = float(input("Enter value for x: "))
y = float(input("Enter value for y: "))
z = float(input("Enter value for z: "))

result = 8*x + 7*x*y*z + 3*z

print(f"8({x}) + 7({x})({y})({z}) + 3({z}) = {8*x} + {7*x*y*z} + {3*z} = {result}")