import os
import json

class Task:
    def __init__(self, task_id, description):
        self.task_id = task_id
        self.description = description
        self.is_done = False

    def __repr__(self):
        status = "Done" if self.is_done else "Not Done"
        return f"{self.task_id}. {self.description} - {status}"

class ToDoList:
    def __init__(self, filename='todo_list.json'):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                tasks = json.load(file)
                return [Task(**task) for task in tasks]
        return []

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump([task.__dict__ for task in self.tasks], file)

    def add_task(self, description):
        task_id = len(self.tasks) + 1
        new_task = Task(task_id, description)
        self.tasks.append(new_task)
        self.save_tasks()

    def update_task(self, task_id, description):
        for task in self.tasks:
            if task.task_id == task_id:
                task.description = description
                self.save_tasks()
                return True
        return False

    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task.task_id != task_id]
        self.reassign_ids()
        self.save_tasks()

    def reassign_ids(self):
        for index, task in enumerate(self.tasks):
            task.task_id = index + 1

    def mark_done(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                task.is_done = True
                self.save_tasks()
                return True
        return False

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        for task in self.tasks:
            print(task)

def display_menu():
    print("============================================================================")
    print("><><><><><><><><><><><><><><>| K-Task_Lister |<><><><><><><><><><><><><><><>")
    print("============================================================================")
    print("============================================================================")
    print("\nTo-Do List Application")
    print("\nMenu.")
    print("1. Add Task.")
    print("2. Update Task.")
    print("3. Delete Task.")
    print("4. Mark Task as Done.")
    print("5. View Tasks.")
    print("6. Exit")

def main():
    todo_list = ToDoList()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            description = input("Enter task description: ")
            todo_list.add_task(description)
        elif choice == '2':
            task_id = int(input("Enter task ID to update: "))
            description = input("Enter new task description: ")
            if not todo_list.update_task(task_id, description):
                print("Task not found.")
        elif choice == '3':
            task_id = int(input("Enter task ID to delete: "))
            todo_list.delete_task(task_id)
        elif choice == '4':
            task_id = int(input("Enter task ID to mark as done: "))
            if not todo_list.mark_done(task_id):
                print("Task not found.")
        elif choice == '5':
            todo_list.view_tasks()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
