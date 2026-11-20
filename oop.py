from abc import ABC, abstractmethod
import math


class Person:
    def __init__(self):
        self._age = 0

    def set_age(self, age):
        if age < 0:
            print("Age cannot be negative")
        self._age = age

    def get_age(self):
        return (f"age: {self._age}")

p = Person()
p.set_age(25)
print(p.get_age())
p.set_age(-5)
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return "I am  an animal "
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
    def speak(self):
        return "Woof"
class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
    def speak(self):
        return "Meow"
dog = Dog("Buddy")
cat = Cat("Kitty")

print(dog.name, dog.speak())  # Вывод: Buddy Woof
print(cat.name, cat.speak())  # Вывод: Kitty Meow
