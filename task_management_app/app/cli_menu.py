"""
app/cli_mune.py: logic for loading the menu and accepting user inputs in the terminal
"""

from services.task_manager import TaskManager
from database_provider.task_repo import TaskRepo


repo = TaskRepo()
tm = TaskManager(repo)


def menu():
    """
    Main menu. Display user choices and redirections
    """
    print("\n==========================================\n")
    print("\nCHOOSE AN OPTION BELOW:")
    print("[1] Add a New Task")
    print("[2] List all Tasks")
    print("[3] Update a Task's Details")
    print("[4] Mark a Task as Completed")
    print("[5] Delete a Task")
    print("[0] Exit App")
    print("\n==========================================\n")

    choice = input("Enter a choice: ").strip()

    # choices and function calls
    if choice == "1":
        add_task()
    elif choice == "2":
        list_tasks()
    elif choice == "3":
        update_task()
    elif choice == "4":
        complete_task()
    elif choice == "5":
        delete_task()
    elif choice == "0":
        print("Goodbye!!!")
        exit()
    else:
        print("Please enter a valid choice")

"""
Function declarations and Entry point of each menu choice
"""
def add_task():
    """
    collects user inputs and add a new task to the database
    """
    try:
        title = input("Title: ").strip()
        task_desc = input("Description (optional): ").strip()

        due_date = input("Due date (YYYY-MM-DD) [optional]: ").strip()
        if due_date == "":
            due_date = None

        task_priority = input("Priority (Low/Medium/High) [Low]: ").strip()
        if task_priority == "":
            task_priority = "Low"

        task_status = input("Status (Pending/In progress/Completed) [Pending]: ").strip()
        if task_status == "":
            task_status = "Pending"

        t = tm.add_task(title, task_desc, due_date, task_priority, task_status)
        print("\nTask added:")
        print(t)
    except Exception as e:
        print("\nError:", e)

def list_tasks():
    """
    Displays all tasks from the database with filtering: due date, priority, status
    """
    try:
        print("\n--- Filters (press Enter to skip) ---")
        status = input("Status (Pending/In progress/Completed): ").strip() or None
        priority = input("Priority (Low/Medium/High): ").strip() or None
        due_date = input("Due date (YYYY-MM-DD): ").strip() or None

        print("\n--- Sorting (press Enter to skip) ---")
        print("Sort by: due_date / priority / status / created_at")
        sort_by = input("Sort by: ").strip() or None

        tasks = tm.list_tasks(status=status, priority=priority, due_date=due_date, sort_by=sort_by)

        if not tasks:
            print("\nNo tasks found.")
            return

        print("\n--- TASKS ---")
        for t in tasks:
            print(t)

    except Exception as e:
        print("\nError:", e)

def update_task():
    """
    Update tasks details
    """
    try:
        task_id = int(input("Task ID to update: ").strip())

        print("Press Enter to skip updating a field.")
        title = input("New title: ").strip()
        task_desc = input("New description: ").strip()
        due_date = input("New due date (YYYY-MM-DD) (blank clears): ").strip()
        task_priority = input("New priority (Low/Medium/High): ").strip()
        task_status = input("New status (Pending/In progress/Completed): ").strip()

        title = title if title != "" else None
        task_desc = task_desc if task_desc != "" else None

        if due_date == "":
            due_date = None  #clear due
        task_priority = task_priority if task_priority != "" else None
        task_status = task_status if task_status != "" else None

        t = tm.update_task(
            task_id,
            title=title,
            task_desc=task_desc,
            due_date=due_date,
            task_priority=task_priority,
            task_status=task_status
        )

        if not t:
            print("\nTask not found.")
        else:
            print("\nTask updated:")
            print(t)

    except ValueError:
        print("\nTask ID must be a number.")
    except Exception as e:
        print("\nError:", e)

def complete_task():
    """
    Marks tasks as completed
    """
    try:
        task_id = int(input("Task ID to mark as completed: ").strip())
        t = tm.complete_task(task_id)

        if not t:
            print("\nTask not found.")
        else:
            print("\nTask completed:")
            print(t)

    except ValueError:
        print("\ Task ID must be a number.")
    except Exception as e:
        print("\n Error:", e)

def delete_task():
    """
    Delete tasks by task ID
    """
    try:
        task_id = int(input("Task ID to delete: ").strip())
        ok = tm.delete_task(task_id)

        if ok:
            print(f"\nTask {task_id} deleted.")
        else:
            print("\nTask not found.")

    except ValueError:
        print("\nTask ID must be a number.")
    except Exception as e:
        print("\nError:", e)