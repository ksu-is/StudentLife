# studentlife.py
# A simple productivity feature for the StudentLife app

class Task:
    """A class to represent a task."""
    
    def __init__(self, task_name, due_date, priority="Normal"):
        self.task_name = task_name
        self.due_date = due_date
        self.priority = priority
        self.completed = False

    def mark_completed(self):
        """Mark the task as completed."""
        self.completed = True

    def __str__(self):
        """Return a string representation of the task."""
        return f"Task: {self.task_name}, Due: {self.due_date}, Priority: {self.priority}, Completed: {self.completed}"

def schedule_task(task_name, due_date, priority="Normal"):
    """Schedule a new task with a name, due date, and priority."""
    task = Task(task_name, due_date, priority)
    return task

def display_task(task):
    """Display task details."""
    print(task)

if __name__ == "__main__":
    # User input to create a task
    print("Welcome to StudentLife!")
    
    task_name = input("Enter the task name: ")
    due_date = input("Enter the due date (YYYY-MM-DD): ")
    priority = input("Enter the priority (High, Medium, Normal): ")

    # Create and display the task
    task = schedule_task(task_name, due_date, priority)
    print("\nTask created:")
    display_task(task)

    # Option to mark task as completed
    mark_complete = input("Do you want to mark this task as completed? (yes/no): ").strip().lower()
    if mark_complete == "yes":
        task.mark_completed()
        print("\nTask updated:")
        display_task(task)
    else:
        print("\nTask remains as scheduled.")
