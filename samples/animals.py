from pets import *

class Goat(Pet, ):
    """A simple attempt to model a goat."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        super().__init__(name, age)

    def bleat(self):
        """Simulate a goat bleating in response to being milked."""
        print(f"{self.name} says, 'Bleat!'")

    def milk(self):
        """Simulate milking a goat."""
        print(f"{self.name} is being milked.")

    def kick(self):
        """Simulate a goat kicking."""
        print(f"{self.name} is kicking.")

class Cow:
    """A simple attempt to model a cow."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def moo(self):
        """Simulate a cow mooing in response to being milked."""
        print(f"{self.name} says, 'Moo!'")

    def milk(self):
        """Simulate milking a cow."""
        print(f"{self.name} is being milked.")

    def kick(self):
        """Simulate a cow kicking."""
        print(f"{self.name} is kicking.")