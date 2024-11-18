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

# Example usage
if __name__ == "__main__":
    # Create and display a task
    task1 = schedule_task("Finish math assignment", "2024-11-20", "High")
    display_task(task1)

    # Mark task as completed
    task1.mark_completed()
    display_task(task1)
