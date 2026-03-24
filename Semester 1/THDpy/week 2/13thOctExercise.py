#Exercise sheet for 2025.10.13 - Basics

# Exercise 1: (made by Okuma Chigozie)
print("Exercise 1: ")
def seconds_to_minutes(seconds):
    minutes = seconds // 60
    remaining_seconds = seconds % 60
    return minutes, remaining_seconds
seconds = int(input("Enter number of seconds: "))
minutes, remaining_seconds = seconds_to_minutes(seconds)
print(f"{seconds} seconds is equal to {minutes} minutes and {remaining_seconds} seconds.")

# Exercise 2: (made by Ant Maung Maung)
print("Exercise 2:")
num = int(input("Enter two digits number: "))
ones_num = num % 10
tens_num = num // 10
reversed_number = (ones_num * 10) + tens_num
print(reversed_number)

#Exercise 3: (made by Manthan Amol Patki)
print("Exercise 3:")
x,y,z = int(input("Enter x:")), int(input("Enter y:")), int(input("Enter z:"))
evaluated_expression = (8*x) + (7*x*y*z) + (3*z)
print(evaluated_expression)

#Exercise 4: (made by Manthan Amol Patki)
print("Exercise 4:")
print("Please enter the decimal temperature of the following days:")
mon,tue,wed,thu, fri, sat, sun = (float(input("Monday:")),
                                  float(input("Tuesday:")),
                                  float(input("Wednesday:")),
                                  float(input("Thursday:")),
                                  float(input("Friday:")),
                                  float(input("Saturday:")),
                                  float(input("Sunday:")))
average_temperature = (mon+tue+wed+thu+fri+sat+sun)/7
print(average_temperature)