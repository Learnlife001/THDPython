print('______________________________________________________________________________________________________________________')
print("The following problems of Exercise 3 are done by Ant Maung Maung.")

"""
1) Write a Python program that creates a list of 5 integers and performs the following tasks:
a) Prints the first and last element
b) Adds a new number to the list
c) Removes the second element
"""
print("problem 1)")
l1 = [0, 1, 2, 3, 4]
print(l1[0], l1[-1])
l1.append(5)
del l1[1]
print(l1)


"""
2) Create a tuple colors = (“red”, “green”, “blue”). Print the second element. Try to change “green” to “yellow”, What happens?
"""
print("problem 2)")
colors = ("red", "green", "blue")
print(colors[1])
# If we try to change green to yellow using colors[1] = "yellow", we get typeError.


"""
3) Given person = (“Alice”, “25”, “Berlin” ) , unpack the tuple into separate variables and print them in a sentence:
“Alice is 25 years old and lives in Berlin”
"""
print("problem 3)")
person = ("Alice", "25", "Berlin")
name = person[0]
age = person[1]
place = person[2]
print(name, "is", age, "years old and lives in", place)


"""
4) Write a program that creates 2 sets: A = {1,2,3,4} and B ={3,4,5,6}. Find and print:
Union of A and B, Intersection of A and B and the Set Difference of A and B
"""
print("problem 4)")
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print(A | B)
print(A & B)
print(A - B)


"""
5) Create a set with duplicate values. Print the set, What do you notice?
"""
print("problem 5)")
s = {0, 1, 2, 4, 2, 1}
print(s)
# The duplicate values are gone in print result

"""
6) Create a dictionary with student names as keys and their scores as values. Print a
person’s score using their key. Add a new student “David” : 92 and update a random
score of anyone to 88
"""
print("problem 6)")
scores = {"John": 81, "Sarah": 82, "Kevin": 90}
scores["David"] = 92
scores["John"] = 88
print(scores)


"""
7) Given the Dictionary capitals = {"Germany": "Berlin", "France": "Paris", "Italy":
"Rome"}, write a program that prints each country and its capital in the format : “The
capital of Germany is Berlin”
"""
print("problem 7)")
capitals = {"Germany": "Berlin", "France": "Paris", "Italy": "Rome"}
l1 = list(capitals.keys())
l2 = list(capitals.values())
print(l2[0], "is the capital of", l1[0])
print(l2[1], "is the capital of", l1[1])
print(l2[2], "is the capital of", l1[2])


"""
9) Write a Python program that stores a list of dictionaries representing students:
students = [
{"name": "Alice", "age": 20},
{"name": "Bob", "age": 22}
]
Print the names of all the students in the list
"""
print("problem 9)")
students = [
    {"name": "Alice", "age": 20},
    {"name": "Bob", "age": 22}
]
print(students[0]["name"])
print(students[1]["name"])


"""
10) Write a Python program that:
• Stores a sentence in a string.
• Splits it into words (list).
• Converts the list into a set to remove duplicates.
• Stores each unique word as a key in a dictionary, with the value being the word length.
"""
print("problem 10)")


def task10(sentence):
    line = str(sentence)
    ls = line.split()
    st = set(ls)
    result = {}
    for word in st:
        result[word] = len(word)
    return result


print(task10("Mary had a little lamb"))


"""
11) Given a list of numbers numbers = [10,20,30,40,50], write a script that prints
each element using a loop, Calculate the sum of all elements without using sum()
"""
print("problem 11)")
numbers = [10, 20, 30, 40, 50]
n0 = 0
for n in numbers:
    print(n)
    n0 = n0 + n
print(n0)

print('______________________________________________________________________________________________________________________')
print('\nThe following programs from the collections exercise were done by Manthan Amol Patki')

# program 1 :
print('program 1:')
numbers_list = [1, 2, 3, 4, 5]
print(f'List of {len(numbers_list)} elements created: {numbers_list}')
# part a
print(
    f'Part a: Printing the first and last element of the list: first -> {numbers_list[0]}, last ->{numbers_list[-1]}')
numbers_list.append(6)
# part b
print(
    f'Part b: Adding a new element to the list, which becomes {numbers_list} with {numbers_list[-1]} added')
del numbers_list[1]
# part c
print(
    f'Part c: Removing the second element of the list, and now the list becomes {numbers_list}')


# program 2:
print("\nprogram 2:")
colors = ("red", "green", "blue")
print(f'Tuple named colors created: {colors}')
# first part of the question
print(f'Printing the second element -> {colors[1]}')
# colors[1] = "yellow"
# second part of the question
print(
    f'After attempting to change the second element with the commented line above (colors[1] = "yellow"), the following error arises: <TypeError: \'tuple\' object does not support item assignment>')

# program 3:
print('\nprogram 3:')
person = ('Alice', '25', 'Berlin')
name, age, place = person  # unpacking the tuple
# printing the sentence with the upacked variables
print(f'{name} is {age} years old and lives in {place}')

# program 4:
print('\nprogram 4:')
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print(f'The two sets are A: {A} and B: {B}')
print(f'Union of A and B is: {A | B}')
print(f'Intersection of A and B is: {A & B}')
print(f'Set Difference of A and B is: {A-B}')

# program 5:
print('\nprogram 5:')
my_set = {1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2}
print(
    f'The set named my_set is defined as {1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2} but its value is actually stored as: {my_set} since duplicate values are removed in python')

# program 6:
print('\nprogram 6:')
student_grades = {'Mark': 82, 'Chris': 43,
                  'Steven': 76, 'Parker': 17, 'Philip': 96}
print(
    f'Dictionary student_grades has student name as keys and scores as values: {student_grades}')
student_grades['David'] = 92
# adding a new student
print(
    f'After adding a new student \'David\':92 the dictionary becomes: {student_grades}')
student_grades['Philip'] = 88  # updating a random student's score to 88
print(
    f'After updating a randoms core to 88 the dictionary becomes: {student_grades}')

# program 7:
print('\nprogram 7:')
capitals = {"Germany": "Berlin", "France": "Paris", "Italy": "Rome"}
# prints the capital of each country
print(
    f'The capital of {list(capitals.keys())[0]} is: {capitals[list(capitals.keys())[0]]}')
print(
    f'The capital of {list(capitals.keys())[1]} is: {capitals[list(capitals.keys())[1]]}')
print(
    f'The capital of {list(capitals.keys())[2]} is: {capitals[list(capitals.keys())[2]]}')

# program 9, program 8 not mentioned in the document
print('\nprogram 9:')
students = [{"name": "Alice", "age": 20}, {"name": "Bob", "age": 22}]
students_list = []
print(f'First student is {students[0]["name"]}')
# prints the name of both of the students
print(f'Second student is {students[1]["name"]}')

# program 10:
print('\nprogram 10:')
# sentence with repeated words
input_sentence = "Python is my favourite programming language, and this programming program is done in python."
print(f'The sentence is: {input_sentence}')
input_sentence = input_sentence.replace(",", "").replace(
    ".", '')  # removing comma and fullstop for easier processing
list_of_words = input_sentence.split(' ')  # splits sentence into words
print(f'List of words in the sentence: {list_of_words}')
# converts list into set to remove duplicates
set_of_words = set(list_of_words)
print(f'Set of the words in the sentence, without repetition: {set_of_words}')
# converts set back to list to be accessible for the dictionary
list_out_of_set_of_words = list(set_of_words)
dictionary_with_length = {
    list_out_of_set_of_words[0]: len(list_out_of_set_of_words[0]),
    list_out_of_set_of_words[1]: len(list_out_of_set_of_words[1]),
    list_out_of_set_of_words[2]: len(list_out_of_set_of_words[2]),
    list_out_of_set_of_words[3]: len(list_out_of_set_of_words[3]),
    list_out_of_set_of_words[4]: len(list_out_of_set_of_words[4]),
    list_out_of_set_of_words[5]: len(list_out_of_set_of_words[5]),
    list_out_of_set_of_words[6]: len(list_out_of_set_of_words[6]),
    list_out_of_set_of_words[7]: len(list_out_of_set_of_words[7]),
    list_out_of_set_of_words[8]: len(list_out_of_set_of_words[8]),
    list_out_of_set_of_words[9]: len(list_out_of_set_of_words[9]),
    list_out_of_set_of_words[10]: len(list_out_of_set_of_words[10]),
    list_out_of_set_of_words[11]: len(list_out_of_set_of_words[11]),
}
print(f'Dictionary with words and their length: {dictionary_with_length}')

# program 11:
print('\nprogram 11:')
numbers = [10, 20, 30, 40, 50]
sum = 0  # variable to store the sum
for i in range(len(numbers)):
    print(f'{numbers[i]}')  # prints each element using a loop
    sum += numbers[i]
# prints the sum of all elements
print(f'Sum of all the numbers of the list numbers is {sum}')

print('______________________________________________________________________________________________________________________')
print("The following problems of Exercise 3 are done by Okuma Chigozie.")

# 1.
print('Program 1:')
cars = ['toyota', 'ford', 'bmw', 'audi', 'honda']
print(cars[0])
print(cars[-1])
cars.append('mercedes')
print(cars)
cars.remove('ford')
print(cars)

# 2.
print('Program 2:')
colors = ("red", "green", "blue")
print(colors[1])
# colors[1] = "yellow"
# gives a typeerrror because tuples are immutable

# 3.
print('Program 3')
person = ("Alice", "25", "Berlin")
print(person)
print("Alice", "is", "25", "years", "old", "and", "lives", "in", "Berlin.")

# 4.
print('Program 4:')
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print(A | B)
print(A & B)
print(A - B)

# 5.
print('Program 5:')
a = {1, 2, 3, 2, 1}
print(a)
# it prints only the unique values: {1, 2, 3}

# 6.
print('Program 6:')
names = {'Alice': 7, 'Bob': 3, 'Charlie': 5}
print(names)
print(names['Alice'])
names['David'] = 92
print(names)
names['Bob'] = 88
print(names)

# 7.
print('Program 7:')
capitals = {"Germany": "Berlin", "France": "Paris", "Italy": "Rome"}
print("The", "capital", "of", "Germany", "is", capitals["Germany"])
print("The", "capital", "of", "France", "is", capitals["France"])
print("The", "capital", "of", "Italy", "is", capitals["Italy"])

# 8.
print('Program 8:')
S = {20: 'Alice', 22: 'Bob'}
print(S)
{20: 'Alice', 22: 'Bob'}
S.values()

# 9.
print('Program 9:')
sentence = "The capital of Germany is Berlin"
print(sentence)
lst = ["The", "capital", "of", "Germany", "is", "Berlin"]
print(lst[0:6])
sentence = {"The", "capital", "of", "Germany", "is", "Berlin"}
print(sentence)
S = {'The': 3, 'capital': 7, 'of': 2, 'Germany': 7, 'is': 2, 'Berlin': 6}
print(S)

# 10.
print('Program 10:')
numbers = [10, 20, 30, 40, 50]
total = 0
for num in numbers:
    print(num)
    total = total + num
print("Total:", total)
