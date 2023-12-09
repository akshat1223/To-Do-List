class TodoList:
    def __init__(self):
        self.tasks = []

    def display_tasks(self):
        print("\nTasks:")
        if not self.tasks:
            print("No tasks found.")
        else:
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task['task']} {'(Completed)' if task['completed'] else ''}")

    def add_task(self, task):
        self.tasks.append({'task': task, 'completed': False})
        print(f"\nTask '{task}' added successfully.")

    def delete_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            deleted_task = self.tasks.pop(task_index - 1)
            print(f"\nTask '{deleted_task['task']}' deleted successfully.")
        else:
            print("\nInvalid task index. No task deleted.")

    def mark_completed(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1]['completed'] = True
            print("\nTask marked as completed.")
        else:
            print("\nInvalid task index. No task marked as completed.")


def main():
    todo_list = TodoList()

    while True:
        print("\nOptions:")
        print("1. Display Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Mark Task as Completed")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            todo_list.display_tasks()
        elif choice == '2':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '3':
            task_index = int(input("Enter the task index to delete: "))
            todo_list.delete_task(task_index)
        elif choice == '4':
            task_index = int(input("Enter the task index to mark as completed: "))
            todo_list.mark_completed(task_index)
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
