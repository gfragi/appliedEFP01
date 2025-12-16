# Worksheet: Designing Your Own Classes in Python (Step by Step)

## 0. Why are we doing this?

In a real application (like the attendance app you're using), the world is modeled with **classes**:

- `User`, `Course`, `Session`, `Attendance`
- each with **data** (attributes) and **behaviour** (methods).

In this worksheet you'll practice how to design *your own* classes from scratch, not just copy `Dog` or `Car` examples.

We'll follow the same simple recipe every time.

---

## 1. Step 1 – Pick a *domain* and find the nouns

Think of a small "world" you care about:

- 📚 Library
- 🚌 Transport
- 🎮 Video game
- 🐾 Pets
- 🧑‍🎓 University / classes
- 🍕 Food delivery

**Task 1.1**

1. Choose *one* domain:
   - **My domain:** `__________________________`
2. Write down at least **3 important things (nouns)** in that world.
   These will become classes.

Examples:

- For a library: `Book`, `Member`, `Loan`
- For a transport system: `Passenger`, `Ticket`, `Route`
- For pets: `Dog`, `Cat`, `Owner`

**My nouns (candidate classes):**

- `Class 1:` `__________________________`
- `Class 2:` `__________________________`
- `Class 3:` `__________________________`

Pick **one** of them for the rest of the worksheet:

> I will design a class called: **`__________________________`**

---

## 2. Step 2 – Decide the attributes (data)

Now think:
> "What information do I need to store about one such object?"

Examples:

- A `Dog` might need: `name`, `age`, `breed`
- A `Ticket` might need: `ticket_id`, `route`, `price`, `is_valid`
- A `Student` might need: `name`, `email`, `attendance_count`

**Task 2.1 – Brainstorm attributes**

For your class `____________` list at least **3 attributes**:

1. `________________` (e.g. name)
2. `________________` (e.g. email, id)
3. `________________` (e.g. age, count, price)
4. *(optional)* `________________`
5. *(optional)* `________________`

**Task 2.2 – Write the `__init__` method**

Use this template and fill in your own class name + attributes.

```python
class CLASSNAME:
    def __init__(self, attr1, attr2, attr3):
        self.attr1 = attr1
        self.attr2 = attr2
        self.attr3 = attr3
```

Now rewrite with your own names and types:

```python
class ____________________:
    def __init__(self, ____________________, ____________________, ____________________):
        self.____________________ = ____________________
        self.____________________ = ____________________
        self.____________________ = ____________________
```

✅ Goal: your class can now store information about one object.

## 3. Step 3 – Decide the methods (behaviour)

Now ask:

"What can this object do? What can we do with it?"

Examples:

- Dog: `bark()`, `sit()`, `have_birthday()`
- Ticket: `invalidate()`, `print_info()`
- Student: `check_in()`, `print_summary()`

**Task 3.1 – List 2–3 actions (verbs)**

For your class ____________, what makes sense?

____________________() (e.g. print_info, check_in)

____________________() (e.g. invalidate, have_birthday)

*(optional)* ____________________()

**Task 3.2 – Implement at least 2 methods**

Use this template:

```python
class CLASSNAME:
    def __init__(self, ...):
        ...

    def method1(self):
        # use self.attribute here
        print("TODO: implement method1")

    def method2(self):
        # update some attribute
        print("TODO: implement method2")
```

Now, write the real code for your class:

```python
class ____________________:
    def __init__(self, ____________________, ____________________, ____________________):
        self.____________________ = ____________________
        self.____________________ = ____________________
        self.____________________ = ____________________

    def ____________________(self):
        # TODO: use one or more attributes
        print("TODO: describe what this object does here")

    def ____________________(self):
        # TODO: maybe change (update) one attribute
        print("TODO: describe another behaviour here")
```

✅ Goal: your class now has both data and behaviour.

## 4. Step 4 – Use your class from another file

In the repo, you have examples like my_dog.py and our_dogs.py where a class is imported from another file and used.

You'll do the same with your own class.

**Task 4.1 – Create the module for your class**

Create a file named, for example, my_class.py.

Paste your class definition in it.

```python
# my_class.py

class ____________________:
    def __init__(self, ...):
        ...
    def ____________________(self):
        ...
    def ____________________(self):
        ...
```

**Task 4.2 – Create a "user" file that imports and uses it**

Create another file, e.g. use_my_class.py:

```python
# use_my_class.py

from my_class import ____________________

# create an object (instance)
obj = ____________________("...", "...", ...)

# call methods
obj.____________________()
obj.____________________()
```

Run it:

```bash
python use_my_class.py
```

If it runs and prints what you expect → 🎉 you've built your own mini "model" just like in real applications.

## 5. Bonus: Add a helper function that uses the class

Methods are one way to add behaviour. Another way is to write functions that take your object as a parameter.

Example pattern:

```python
def describe_dog(dog: Dog) -> None:
    print(f"{dog.name} is {dog.age} years old.")
```

**Task 5.1 – Write one helper function**

In use_my_class.py, add a function that takes your object as argument:

```python
def describe(obj: ____________________) -> None:
    """Print some information about this object."""
    print("TODO: print a nice description here")

# After creating your object:
describe(obj)
```

✅ Goal: see the difference between what belongs inside the class (methods), and what can be a separate utility function.

## 6. Reflection: connect to real systems

Answer briefly (can be bullet points):

- If your class were part of a real application (like the attendance app), what larger system could it belong to?

  ________________________________________________________________

- Which attributes might be stored in a database?

  ________________________________________________________________

- Which methods/functions might be used when handling a web request (e.g. "user clicks a button" / "sends a form" / "scans a QR code")?

  ________________________________________________________________

## 7. Mini checklist: "Did I design a good class?"

Use this to self-check your work:

- [ ] My class represents one clear concept (one main noun).
- [ ] I have at least 3 attributes that make sense for that concept.
- [ ] I have at least 2 methods that:
  - use or modify the attributes
  - have meaningful names (verbs)
- [ ] I can create multiple objects of this class with different data.
- [ ] I can import the class from another file and use it.
- [ ] I wrote at least one helper function that accepts my object.

If you checked most of these: you're thinking like a software engineer 🧠.


