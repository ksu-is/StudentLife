# studentlife.py
# A simple productivity feature for the StudentLife app

from datetime import datetime

class Task:
    """A class to represent a task."""
    
    def __init__(self, task_name, due_date, priority="Normal"):
        self.task_name = task_name
        self.due_date = datetime.strptime(due_date, "%Y-%m-%d")
        self.priority = priority
        self.completed = False

    def mark_completed(self):
        """Mark the task as completed."""
        self.completed = True

    def __str__(self):
        """Return a string representation of the task."""
        return f"Task: {self.task_name}, Due: {self.due_date.strftime('%Y-%m-%d')}, Priority: {self.priority}, Completed: {self.completed}"

def check_conflict(new_task, task_list):
    """Check for scheduling conflicts."""
    for task in task_list:
        if task.due_date == new_task.due_date:
            return task
    return None

def schedule_task(task_list, task_name, due_date, priority="Normal"):
    """Schedule a new task with a name, due date, and priority."""
    new_task = Task(task_name, due_date, priority)
    conflict = check_conflict(new_task, task_list)
    if conflict:
        print(f"Conflict detected! Task '{conflict.task_name}' is already scheduled for {due_date}.")
    task_list.append(new_task)
    return new_task

def display_tasks(task_list):
    """Display all tasks."""
    print("\nScheduled Tasks:")
    if not task_list:
        print("No tasks scheduled.")
    for task in task_list:
        print(task)

if __name__ == "__main__":
    # Welcome message
    print("Welcome to StudentLife!")
    tasks = []  # List to store scheduled tasks

    while True:
        print("\n1. Add a task")
        print("2. View all tasks")
        print("3. Mark a task as completed")
        print("4. Exit")

        choice = input("Choose an option: ").strip()
        
        if choice == "1":
            task_name = input("Enter the task name: ")
            due_date = input("Enter the due date (YYYY-MM-DD): ")
            priority = input("Enter the priority (High, Medium, Normal): ")
            
            try:
                new_task = schedule_task(tasks, task_name, due_date, priority)
                print("\nTask added:")
                print(new_task)
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")
        
        elif choice == "2":
            display_tasks(tasks)
        
        elif choice == "3":
            display_tasks(tasks)
            task_name = input("\nEnter the name of the task to mark as completed: ").strip()
            for task in tasks:
                if task.task_name.lower() == task_name.lower():
                    task.mark_completed()
                    print(f"\nTask '{task.task_name}' marked as completed.")
                    break
            else:
                print("Task not found.")
        
        elif choice == "4":
            print("Goodbye!")
            break
        
        else:
            print("Invalid option. Please try again.")
