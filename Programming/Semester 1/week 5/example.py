print("exercise 8")


def longest_length(filename):
    max_length = 0
    with open(filename, "r") as file:
        for line in file:
            current_length = len(line.strip())

            if current_length > max_length:
                max_length = current_length
                longest_sentence = line.strip()

    return longest_sentence


l = longest_length(the_file_name)
print("The longest sentence is: ", l)

print("____________________")
