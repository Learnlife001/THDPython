# reverse a 2 digit number
number = int(input("Enter a 2 digit number: "))
ones = number % 10
reversed_number = ones * 10 + (number // 10)

print(f"Reversed number: {reversed_number}")

