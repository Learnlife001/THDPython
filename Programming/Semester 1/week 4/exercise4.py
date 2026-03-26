# 1. Add odd numbers up to N
N = int(input("Value for N: "))
total = 0
for number in range(1, N + 1):
    if number % 2 != 0:
        total += number
print("Sum of odd numbers up to3", N, "is:", total)

# 2. Find the lowest number
numbers_list = [1, 3, 5, 7, 9, 11]
lowest = numbers_list[0]
for number in numbers_list:
    if number < lowest:
        lowest = number
print("Lowest number is:", lowest)

# 3. Fibonacci series (first 20 elements)
a = 0
b = 1
fib_series = []
for i in range(20):
    fib_series.append(a)
    temp = a
    a = b
    b = temp + b
print("The first 20 Fibonacci numbers are:", fib_series)

# 4. First ten Mersenne numbers
mersenne_numbers = []
for n in range(1, 11):
    mersenne_numbers.append((2 ** n) - 1)
print("First ten Mersenne numbers are:", mersenne_numbers)

# 5. Star pattern
rows = 4
for i in range(1, rows + 1):
    print('*' * i)

# 6. Leap year check
year = int(input("Enter a year: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(year, "is a leap year.")
        else:
            print(year, "is not a leap year.")
    else:
        print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")

# 7. Triangle sides check
a = float(input("Side 1: "))
b = float(input("Side 2: "))
c = float(input("Side 3: "))
if (a + b > c) and (b + c > a) and (c + a > b):
    print("The sides can form a triangle.")
else:
    print("The sides cannot form a triangle.")

# 8. Digit to word
digit_words = {
    '0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four',
    '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'
}
digit = input("Enter a single digit (0-9): ")
if digit in digit_words:
    print("The word is:", digit_words[digit])
else:
    print("Invalid input. Please enter a digit between 0 and 9.")

# 9. Palindrome checker
text = input("Enter a string or number: ")
cleaned = ''.join(text.split()).lower()
if cleaned == cleaned[::-1]:
    print(text, "is a palindrome.")
else:
    print(text, "is not a palindrome.")

# 10. Temperature converter
temp = float(input("Enter the temperature: "))
unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

if unit.upper() == 'C':
    converted = (9 / 5) * temp + 32
    print(temp, "°C is", converted, "°F.")
elif unit.upper() == 'F':
    converted = (5 / 9) * (temp - 32)
    print(temp, "°F is", converted, "°C.")
else:
    print("Invalid unit entered.")
