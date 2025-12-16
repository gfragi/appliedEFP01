class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Cat(Pet):
    """A simple attempt to model a cat."""

    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def meow(self):
        """Simulate a cat meowing in response to a command."""
        print(f"{self.name} says, 'Meow!'")


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} is now barking.")

    def sit(self):
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        print(f"{self.name} rolled over!")

    def get_age(self):
        print (f"{self.name} is {self.age} years old.")