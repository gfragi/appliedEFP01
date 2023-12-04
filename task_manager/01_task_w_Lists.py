"""
This script provides a task manager that allows the user to add, display, mark as completed, and remove tasks from a list.
The script defines four functions: add_task, display_tasks, complete_task, and remove_task, which are used to perform the corresponding actions.
The main program loop provides a menu of options for the user to choose from, and the selected action is performed accordingly.
"""
#Initialize an empty task list
task_list = []

# Function to add a task to the list
def add_task(task):
    """
    Adds a task to the task list.

    Args:
        task (str): The task to be added.

    Returns:
        None
    """
    task_list.append(task)
    print("Task added: ", task)

# Function to display the task list
def display_tasks():
    if not task_list:
        print("Task list is empty.")
    else:
        print("Task List:")
        for index, task in enumerate(task_list, start=1):
            print(f"{index}. {task}")

# Function to mark a task as completed
def complete_task(task_index):
    """
    Marks a task as completed by adding the string "(Completed)" to the end of the task description.

    Args:
        task_index (int): The index of the task to mark as completed.

    Returns:
        None
    """
    if 1 <= task_index <= len(task_list):
        task_list[task_index - 1] += " (Completed)"
        print("Task marked as completed.")
    else:
        print("Invalid task index.")

# Function to remove a task
def remove_task(task_index):
    """
    Removes a task from the task list at the specified index.

    Args:
        task_index (int): The index of the task to remove.

    Returns:
        None
    """
    if 1 <= task_index <= len(task_list):
        removed_task = task_list.pop(task_index - 1)
        print(f"Task removed: {removed_task}")
    else:
        print("Invalid task index.")

# Main program loop
while True:
    print("\nOptions:")
    print("1. Add Task")
    print("2. Display Tasks")
    print("3. Mark Task as Completed")
    print("4. Remove Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter the task: ")
        add_task(task)
    elif choice == "2":
        display_tasks()
    elif choice == "3":
        task_index = int(input("Enter the task number to mark as completed: "))
        complete_task(task_index)
    elif choice == "4":
        task_index = int(input("Enter the task number to remove: "))
        remove_task(task_index)
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please choose a valid option.")
