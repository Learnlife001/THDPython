print("The following exercises are done by Ant Maung Maung")

print("Exercise 1")


def greeting(first_name, last_name=""):
    print("Hello, " + first_name + " " + last_name+". Welcome Back.")


greeting("Ant", "Maung Maung")
greeting("Ant")

print("____________________")

print("exercise 2")


def find_max(*number):
    maximum = number[0]
    for number in number:
        if number > maximum:
            maximum = number
    return maximum


max = find_max(1, 2, 3, 4, 5)
print(max)

print("____________________")

print("exercise 3")


def find_average(*number):
    if number:
        average = sum(number) / len(number)
        return average
    else:
        return 0


print(find_average(1, 2, 3, 4, 5))
print(find_average())

print("____________________")

print("exercise 4")


def filter_even(*number):
    even = []
    for n in number:
        if n % 2 == 0:
            even.append(n)
    return even


print(filter_even(0, 1, 2, 3, 4, 5))

print("____________________")

print("exercise 5")


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))

print("____________________")

print("exercise 6")


def write_lines(filename, lines):
    with open(filename, "w") as file:
        for line in lines:
            file.write(line + "\n")


file_name = "AMM_text_file.txt"
lines_to_write = [
    "First line.",
    "Second line.",
    "second line.",
    "Third and final line.",
    "AndOneForTesting.",
    "Repeated line."
]

write_lines(file_name, lines_to_write)

print("____________________")

print("exercise 7")


def count_words(filename):
    the_words = []
    space_newline = " \n"
    current_word = ""
    with open(filename, "r") as file:
        content = file.read()
    for chr in content:
        if chr in space_newline:
            if current_word:
                the_words.append(current_word)
                current_word = ""
        else:
            current_word += chr

    return len(the_words)


print(count_words(file_name))

print("____________________")

print("exercise 8")


def longest_length(filename):
    the_words = []
    space_newline = " \n"
    current_word = ""
    with open(filename, "r") as file:
        content = file.read()
    for chr in content:
        if chr in space_newline:
            if current_word:
                the_words.append(current_word)
                current_word = ""
        else:
            current_word += chr

    longest_word = the_words[0]
    for word in the_words:
        if len(word) > len(longest_word):
            longest_word = word

    return longest_word


print(longest_length(file_name))

print("____________________")

print("exercise 9")


def reverse_file(input_file, output_file):
    with open(input_file, "r") as file:
        content = file.readlines()

    reversed_content = []
    for line in content:
        reversed_content.insert(0, line)

    with open(output_file, "w") as file:
        for line in reversed_content:
            file.write(line)


reverse_file("AMM_text_file.txt", "AMM_reversed_text_file.txt")
print("Please check the output file for result.")

print("____________________")

print("exercise 10")


def word_frequency(filename):
    the_words = []
    space_newline = " \n"
    current_word = ""
    with open(filename, "r") as file:
        content = file.read()
    for chr in content:
        if chr in space_newline:
            if current_word:
                the_words.append(current_word)
                current_word = ""
        else:
            current_word += chr

    case_sensitive_list = []
    for word in the_words:
        case_sensitive_list.append(word.lower())

    frequency = {}

    for word in case_sensitive_list:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency


print(word_frequency(file_name))
