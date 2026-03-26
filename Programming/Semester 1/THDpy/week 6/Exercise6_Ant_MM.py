print("____________________________________")

print("The following exercises are done by Ant Maung Maung.")
print("exercise 1")

class Person:
    def greet(self):
        print("Hello!")

p = Person()
p.greet()

print("____________")

print("exercise 2")
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name :", self.name)
        print("Age :", self.age)

john = Person("John", 36)
john.display()

print("____________")

print("exercise 3")
class Person:
    def __init__(self, name, age = 18):
        self.name = name
        self.age = age

    def display(self):
        print("Name :", self.name)
        print("Age :", self.age)

jim = Person("Jim")
jim.display()

print("____________")
print("exercise 4")
class employees(Person):
    def __init__(self, name, age, job_role):
        super().__init__(name, age)
        self.job_role = job_role

    def display(self):
        super().display()
        print("Job Role :", self.job_role)

james = employees("James",32, "Manager")
james.display()

print("____________")
print("exercise 5")
class Address:
    def __init__(self, fname, lname,email):
        self.fname = fname
        self.lname = lname
        self.email = email

Max_Munstermann = Address("Max", "Munstermann", "<max.mstrm@gmail.comm>")
print(Max_Munstermann.fname)

print("____________")
print("exercise 6")
class Addressbook:
    def __init__(self):
        self.address = []

    def add(self, address):
        self.address.extend(address)

    def find(self, ADDRESS):
        address = ADDRESS.lower()
        for the_address in self.address:
            if the_address == address:
                print("Address found :" + the_address)
                return the_address
        print("Address not found")
        return None

houses = Addressbook()
houses.add(["house1", "house2", "house6"])
houses.find("HOUSE2")
houses.find("HOUSE7")

print("____________")
print("exercise 7")
class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

customer = BankAccount()
customer.deposit(100)
print(customer.balance)
customer.withdraw(15)
print(customer.balance)

print("____________")
print("exercise 8")
class Car:
    def __init__(self,wheel = 4):
        self.wheel = wheel

SUV = Car()
COUPE = Car()
print(SUV.wheel)
print(COUPE.wheel)

print("____________")
print("exercise 9")
class Vehicle:
    def start(self):
        print("Vroom Vroom")

class Bike(Vehicle):
    def start(self):
        print("Brap Brap Brap")

kawasaki = Bike()
kawasaki.start()

print("____________")
print("exercise 10")
class Bike(Vehicle):
    def start(self):
        super().start()
        print("The Bike is starting")

Honda = Bike()
Honda.start()

print("____________")
print("exercise 11")

class Student():
    def __init__(self, name, initial_grade = None):
        self.name = name
        self._grade = initial_grade

    def set_grade(self, grade):
        self._grade = grade

    def get_grade(self):
        return self._grade

alice = Student("Alice")
alice.set_grade(100)
print(alice.get_grade())

print("____________")
print("exercise 12")
class Dog():

    def sound(self):
        print("Woof")

class Cat():
    def sound(self):
        print("Meow")

pets = [Dog(), Cat(), Dog(), Cat()]
for pet in pets:
    pet.sound()

print("____________")
print("exercise 13")
class Note():
    def __init__(self, filename):
        self.filename = str(filename)

    def write_note(self, note):
        with open(self.filename, "a") as file:
            file.write(note+ "\n")

    def read_note(self):
        with open(self.filename, "r") as file:
            print(file.read())

example_note = Note("exercise 13")
example_note.write_note("example text")
example_note.read_note()

print("____________")
print("exercise 14")

from abc import ABC, abstractmethod
class Vehicle(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def start(self):
        print(self.name +": Engine starts, ready to drive.")

    def stop(self):
        print(self.name+": Brakes engaged, car is parked.")

class Bicycle(Vehicle):
    def start(self):
        print(self.name+": Rider begins pedaling.")

    def stop(self):
        print(self.name+": Rider comes to a stop and dismounts.")

my_car = Car("Sedan")
my_bike = Bicycle("Mountain Bike")

my_car.start()
my_car.stop()

my_bike.start()
my_bike.stop()

print("____________________________________")