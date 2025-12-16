class Dog:
    """Represents a dog in our system."""

    def __init__(self, name: str, age: int):
        """
        Create a new dog.

        :param name: The dog's name
        :param age: The dog's age in years
        """
        self.name = name
        self.age = age

    def bark(self) -> None:
        print(f"{self.name} is now barking.")

    def sit(self) -> None:
        print(f"{self.name} is now sitting.")

    def roll_over(self) -> None:
        print(f"{self.name} rolled over!")

    def get_age(self) -> int:
        return self.age

    def have_birthday(self) -> None:
        self.age += 1
        print(f"Happy birthday, {self.name}! You are now {self.age}.")
