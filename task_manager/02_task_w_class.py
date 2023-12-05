class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

class TaskManager:
    def __init__(self):
        self.task_list = []

    def add_task(self, description):
        task = Task(description)
        self.task_list.append(task)
        print("Task added:", description)

    def display_tasks(self):
        if not self.task_list:
            print("Task list is empty.")
        else:
            print("Task List:")
            for index, task in enumerate(self.task_list, start=1):
                status = "Completed" if task.completed else "Not Completed"
                print(f"{index}. Description: {task.description}")
                print(f"   Status: {status}")

    def complete_task(self, task_index):
        if 1 <= task_index <= len(self.task_list):
            task = self.task_list[task_index - 1]
            task.completed = True
            print("Task marked as completed.")
        else:
            print("Invalid task index.")

    def remove_task(self, task_index):
        if 1 <= task_index <= len(self.task_list):
            removed_task = self.task_list.pop(task_index - 1)
            print(f"Task removed: {removed_task.description}")
        else:
            print("Invalid task index.")

    def display_menu(self):
        print("\nOptions:")
        print("1. Add Task")
        print("2. Display Tasks")
        print("3. Mark Task as Completed")
        print("4. Remove Task")
        print("5. Exit")

    def run(self):
        while True:
            self.display_menu()
            
            choice = input("Enter your choice: ")
            
            if choice == "1":
                description = input("Enter the task: ")
                self.add_task(description)
            elif choice == "2":
                self.display_tasks()
            elif choice == "3":
                task_index = int(input("Enter the task number to mark as completed: "))
                self.complete_task(task_index)
            elif choice == "4":
                task_index = int(input("Enter the task number to remove: "))
                self.remove_task(task_index)
            elif choice == "5":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    task_manager = TaskManager()
    task_manager.run()