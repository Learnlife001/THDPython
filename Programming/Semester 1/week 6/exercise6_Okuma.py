# week 6 solutions
from abc import ABC, abstractmethod
print("__________________________________________")
print("exercise 1")


class Person:
    def greet(self):
        print("Hello!")


p = Person()
p.greet()


print("__________________________________________")
print("exercise 2")


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name, self.age)


p = Person("Okuma", 23)
p.display()


print("__________________________________________")
print("exercise 3")


class Person:
    def __init__(self, name, age=23):
        self.name = name
        self.age = age

    def display(self):
        print(self.name, self.age)


p1 = Person("Greg", 25)
p2 = Person("CJ")
p1.display()
p2.display()

print("__________________________________________")
print("exercise 4")


class Person:
    def __init__(self, name, age=18):
        self.name = name
        self.age = age

    def display(self):
        print(self.name, self.age)


class Employee(Person):
    def __init__(self, name, age, job_role):
        super().__init__(name, age)
        self.job_role = job_role

    def display(self):
        print(self.name, self.age, self.job_role)


e = Employee("CJ", 23, "Security")
e.display()

print("__________________________________________")
print("exercise 5")


class Address:
    def __init__(self, fname, lname, email):
        self.fname = fname
        self.lname = lname
        self.email = email

    def display(self):
        print(self.fname, self.lname, self.email)


a = Address("CJ", "Greg", "gregcj06@gmail.com")
a.display()


print("__________________________________________")
print("exercise 6")


class Addressbook:
    def __init__(self):
        self.addresses = []

    def add(self, address):
        self.addresses.append(address)

    def find_by_email(self, email):
        for addr in self.addresses:
            if addr.email == email:
                return addr
        return None


book = Addressbook()
book.add(Address("Okuma", "Greg", "gregcj06@gmail.com"))
found = book.find_by_email("gregcj06@gmail.com")

if found:
    found.display()
else:
    print("Not found")


print("__________________________________________")
print("exercise 7")


class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def display(self):
        print("Balance:", self.balance)


acc = BankAccount(100)
acc.deposit(50)
acc.withdraw(30)
acc.display()

print("__________________________________________")
print("exercise 8")


class Car:
    wheels = 4


car1 = Car()
car2 = Car()

print(car1.wheels)
print(car2.wheels)


print("__________________________________________")
print("exercise 9")


class Vehicle:
    def start(self):
        print("Vehicle is starting")


class Bike(Vehicle):
    def start(self):
        print("Bike specific start")


v = Vehicle()
b = Bike()
v.start()
b.start()


print("__________________________________________")
print("exercise 10")


class Vehicle:
    def start(self):
        print("Vehicle is starting")


class Bike(Vehicle):
    def start(self):
        super().start()
        print("Bike is starting")


b = Bike()
b.start()


print("__________________________________________")
print("exercise 11")


class Student:
    def __init__(self, name):
        self.name = name
        self.__grade = None

    def set_grade(self, grade):
        self.__grade = grade

    def get_grade(self):
        return self.__grade


s = Student("Greg")
s.set_grade(860)
print(s.get_grade())


print("__________________________________________")
print("exercise 12")


class Cat:
    def sound(self):
        print("Meow")


class Dog:
    def sound(self):
        print("Woof")


animals = [Cat(), Dog()]
for a in animals:
    a.sound()


print("__________________________________________")
print("exercise 13")


class Note:
    def __init__(self, filename):
        self.filename = filename

    def write_note(self, text):
        with open(self.filename, "a") as f:
            f.write(text + "\n")

    def read_note(self):
        with open(self.filename, "r") as f:
            content = f.read()
            print(content)


n = Note("note.txt")
n.write_note("I am groot")
n.read_note()


print("__________________________________________")
print("exercise 14")


class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):
    def start(self):
        print("Car starting")

    def stop(self):
        print("Car stopping")


class Bicycle(Vehicle):
    def start(self):
        print("Bicycle starting")

    def stop(self):
        print("Bicycle stopping")


c = Car()
b = Bicycle()
c.start()
c.stop()
b.start()
b.stop()
