"""
app/cli_mune.py: logic for loading the menu and accepting user inputs in the terminal
"""

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
    print("testing")

def list_tasks():
    """
    Displays all tasks from the database with filtering: due date, priority, status
    """
    print("testing")

def update_task():
    """
    Update tasks details
    """
    print("testing")

def complete_task():
    """
    Marks tasks as completed
    """
    print("test")

def delete_task():
    """
    Delete tasks by task ID
    """
    print("testing")

    