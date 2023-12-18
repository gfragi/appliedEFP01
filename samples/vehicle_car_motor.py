class Vehicle:
    def __init__(self):
        self.position = 0

    def move(self):
        self.position += 1

    def print_position(self):
        pass  # This will be implemented in the subclasses

class Car(Vehicle):
    def print_position(self):
        print(f"Car's position: {'*' * self.position}")

class Motorcycle(Vehicle):
    def print_position(self):
        print(f"Motorcycle's position: {'.' * self.position}")

# Create instances of Car and Motorcycle
my_car = Car()
my_motorcycle = Motorcycle()

# Print initial positions
my_car.print_position()
my_motorcycle.print_position()

# Move and print positions 10 times
for i in range(1, 11):
    my_car.move()
    my_motorcycle.move()
    my_car.print_position()
    my_motorcycle.print_position()