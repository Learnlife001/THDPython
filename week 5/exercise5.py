# exercise 1 greet_user
def greet(first_name, last_name=""):
    if last_name == "":
        print(f"Hello, {first_name}! Welcome back!")
    else:
        print(f"Hello, {first_name} {last_name}! Welcome back!")


greet("Bob", "Ross")
greet("Bob")

# exercise 2 find_max


def find_max(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


result = find_max(2, 4, 6)
print("The largest number is:", result)

# exercise 3 average


def average(numbers):
    if len(numbers) == 0:
        return 0
    total = 0
    for n in numbers:
        total = total + n
        average = total / len(numbers)
    return average


result = average([2, 3, 5, 6, 8])
print("Average:", result)


# exercise 4 filter_ever
def filter_even(numbers):
    even_numbers = []
    for n in numbers:
        if n % 2 == 0:
            even_numbers.append(n)
    return even_numbers


result = filter_even([1, 2, 3, 6, 5])
print("Even numbers:", result)


# exercise 5 factorial
def factorial(n):
    if n < 0:
        return "Invalid Input"
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


result = factorial(-1)
print("Factorial is:", result)


# exercise 6 write_lines
def write_lines(filename, lines):
    with open(filename, "w") as f:
        for line in lines:
            f.write(line + "\n")


lines = ["Hello", "up is good", "that is all"]
write_lines("my.txt", lines)
print("Lines in file")


# exercise 7 count_words
def count_words(filename):
    with open(filename, "r") as f:
        content = f.read()
        words = content.split()
        print("Number of words:", len(words))


count_words("my.txt")


# exercise 8 longest_length
def longest_length(filename):
    with open(filename, "r") as f:
        longest_line = ""
        for line in f:
            if len(line) > len(longest_line):
                longest_line = line
        print("Longest line:")
        print(longest_line)


longest_length("my.txt")


# exercise 9 reverse_file
def reverse_file(input_file, output_file):
    with open(input_file, "r") as f:
        lines = f.readlines()
    print("Lines reversed:", len(lines))
    reversed_lines = []
    index = len(lines) - 1
    while index >= 0:
        reversed_lines.append(lines[index])
        index = index - 1
    with open(output_file, "w") as f:
        for line in reversed_lines:
            f.write(line)


reverse_file("my.txt", "reversed_my.txt")


# exercise 10 word_frequency
def word_frequency(filename):
    with open(filename, "r") as f:
        content = f.read()
        content = content.lower()
        words = content.split()
        frequency = {}

        for word in words:
            if word in frequency:
                frequency[word] = frequency[word] + 1
            else:
                frequency[word] = 1

        print("Word frequency:")
        for word in frequency:
            print(word, ":", frequency[word])


word_frequency("my.txt")
