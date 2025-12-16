from manolis import Cars

class Battery:
    """ A simple attempt to model a battery for an electric car. """

    def __init__(self, battery_size=75):
        """ Initialize the battery's attributes. """
        self.battery_size = battery_size

    def describe_battery(self):
        """ Print a statement describing the battery size. """
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """ Print a statement about the range this battery provides. """
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        """ Upgrade the battery if possible. """
        if self.battery_size < 100:
            self.battery_size = 100

class ElectricCar(Cars):
    def __init__(self, make, model, year):
        """ Initialize attributes of the parent class. """
        super().__init__(make, model, year)
        self.battery = Battery()