# Worksheet: Designing Classes with Inheritance (Base & Subclasses)

## 0. Why inheritance?

In your repo you've seen two versions of cars and motorcycles:

- One version where **Car** and **Motorcycle** each have their own `position` and `move()` (duplicate code).
- A second version where they both **inherit** from a common **Vehicle** class.

Inheritance lets us:

- Put **shared data & behaviour** in a **base class**.
- Put **differences** in subclasses that override or extend the base.

You will now design your own small hierarchy.

---

## 1. Step 1 – Find the "parent + children" pattern

We look for:

- One **generic concept** → base class
- Several **specific kinds of it** → subclasses

Examples:

- `Vehicle` → `Car`, `Bus`, `Motorcycle`, `Bicycle`
- `Person` → `Student`, `Teacher`, `Admin`
- `Animal` → `Dog`, `Cat`, `Cow`, `Goat`
- `Account` → `BasicAccount`, `PremiumAccount`

**Task 1.1 – Choose a hierarchy**

Pick one of the patterns below (or design your own):

1. `Vehicle` → `Car`, `Bus`, `Motorcycle`
2. `Person` → `Student`, `Instructor`, `Staff`
3. `Animal` → `Dog`, `Cat`, `Cow`
4. My own idea:
   Base: `______________`
   Subclasses: `______________`, `______________`, `______________`

Write your choice here:

> **Base class:** `____________________________`
> **Subclass 1:** `____________________________`
> **Subclass 2:** `____________________________`
> **Subclass 3 (optional):** `___________________`

---

## 2. Step 2 – Design the base class (shared stuff)

The base class should contain everything that is **common**:

- Shared **attributes** (data)
- Shared **methods** (behaviour)

Example for `Vehicle`:

- attributes: `position`, `speed`
- methods: `move()`, maybe `stop()`

**Task 2.1 – List shared attributes**

What properties do **all** your subclasses have?

1. `________________` (e.g. `name`, `id`, `position`)
2. `________________` (e.g. `speed`, `age`, `email`)
3. *(optional)* `________________`

**Task 2.2 – List shared methods**

What can **all** of them do?

1. `________________()` (e.g. `describe`, `move`, `work`)
2. *(optional)* `________________()` (e.g. `reset`, `print_status`)

**Task 2.3 – Write the base class**

Use this template and adapt:

```python
class BaseName:
    def __init__(self, attr1, attr2):
        self.attr1 = attr1
        self.attr2 = attr2

    def common_method(self):
        print("Common behaviour here")
```

Now write your own base class definition:

```python
class ______________________________:
    def __init__(self, ____________________, ____________________):
        self.____________________ = ____________________
        self.____________________ = ____________________

    def ____________________(self):
        # TODO: use the shared attributes somehow
        print("TODO: common behaviour for ALL subclasses")
```

✅ Goal: Base class captures what all the subclasses share.

## 3. Step 3 – Design the subclasses (differences)

Now define subclasses that:

- inherit from the base: class Car(Vehicle):
- may add extra attributes
- may override methods (polymorphism)

### 3.1 Subclass 1

**Task 3.1 – Decide extra/unique parts**

For subclass 1 (____________):

Extra attributes (not in base):

________________

*(optional)* ________________

Special behaviour (methods only this subclass has or overrides):

________________()

*(optional)* ________________()

**Task 3.2 – Implement subclass 1**

Template:

```python
class SubClassName(BaseName):
    def __init__(self, attr1, attr2, extra_attr):
        super().__init__(attr1, attr2)
        self.extra_attr = extra_attr

    def common_method(self):
        # override base method
        print("Specific version for this subclass")
```

Your version:

```python
class ____________________(____________________):
    def __init__(self, ____________________, ____________________, ____________________):
        super().__init__(____________________, ____________________)
        self.____________________ = ____________________

    def ____________________(self):
        # TODO: override or extend base method
        print("TODO: subclass-specific behaviour here")
```

### 3.2 Subclass 2 (similar steps)

Repeat the same process for subclass 2.

```python
class ____________________(____________________):
    def __init__(self, ____________________, ____________________, ____________________):
        super().__init__(____________________, ____________________)
        self.____________________ = ____________________

    def ____________________(self):
        print("TODO: behaviour specific to subclass 2")
```

*(Optional)* Do the same for subclass 3.

## 4. Step 4 – Use them together (polymorphism)

Now we write a script that:

- Creates different subclasses.
- Puts them in one list of base type.
- Calls a method with the same name on each object.

Example pattern (for vehicles):

```python
vehicles = [
    Car("Toyota", 0),
    Bus("Volvo", 0),
    Motorcycle("Honda", 0),
]

for v in vehicles:
    v.move()            # same method name
    v.print_position()  # different implementation per class
```

**Task 4.1 – Create a file use_inheritance.py**

Assume your classes are in models.py:

```python
# use_inheritance.py

from models import ____________________, ____________________, ____________________

objects = [
    ____________________("...", ...),
    ____________________("...", ...),
    ____________________("...", ...),
]

for obj in objects:
    # Call at least one method that exists in the base class
    obj.____________________()

    # Optionally call a subclass-specific method
    # (use hasattr to be safe)
    if hasattr(obj, "____________________"):
        obj.____________________()
```

Run it:

```bash
python use_inheritance.py
```

✅ Goal: See that the same method call behaves differently depending on the subclass → polymorphism.

## 5. Step 5 – Refactor from "duplicate classes" to inheritance

This mirrors the idea of going from the simple car_motor.py (duplicate code) to vehicle_car_motor.py (with a Vehicle base class).

**Task 5.1 – Start from procedural or duplicated code**

Write (or reuse) a version where you have two separate classes with repeated code.

Example:

```python
class Car:
    def __init__(self):
        self.position = 0

    def move(self):
        self.position += 1

    def print_position(self):
        print(f"Car: {self.position}")


class Motorcycle:
    def __init__(self):
        self.position = 0

    def move(self):
        self.position += 1

    def print_position(self):
        print(f"Motorcycle: {self.position}")
```

**Task 5.2 – Refactor to use inheritance**

Create a base class with the common code.

Make Car and Motorcycle inherit from it.

Keep only the differences in the subclasses.

Sketch:

```python
class Vehicle:
    def __init__(self):
        self.position = 0

    def move(self):
        self.position += 1

    def print_position(self):
        # (optional) generic implementation or just pass
        print(f"Vehicle at position {self.position}")


class Car(Vehicle):
    def print_position(self):
        print(f"Car at position {self.position}")


class Motorcycle(Vehicle):
    def print_position(self):
        print(f"Motorcycle at position {self.position}")
```

Now update your own custom pair of classes the same way.

## 6. Bonus: Where would this live in a real system?

Answer briefly:

If this inheritance tree were part of the attendance system, what could it represent?

Example: Person → Student, Instructor, Admin.

________________________________________________________________

Which base class attributes would be stored in the database for all subclasses?

________________________________________________________________

Which subclass-only attributes or methods can you imagine being used in the web interface or API?

________________________________________________________________

## 7. Mini checklist: "Did I use inheritance well?"

- [ ] I chose a base class that represents a clear generic concept.
- [ ] Each subclass is a specific kind of that base class.
- [ ] Common attributes and methods live in the base.
- [ ] Subclasses only contain differences or extra behaviour.
- [ ] I can create a list of base-type objects (list[BaseType]) that actually holds different subclasses.
- [ ] I can loop over that list and call the same method name, and it does the right thing for each object (polymorphism).
- [ ] Compared to the "no inheritance" version, I now have less duplicated code and it is easier to add a new subclass.

If you checked most of these, you're successfully using inheritance like in real applications. 🚀
