"""
main.py: THIS IS THE ENTRY POINT OF THE TASK MANAGEMENT APP
usage: python3 main.py
"""

from app.cli_menu import menu #import the main menu 

def main():
    """
    Execute the main menu loop until the user exits or clicks 0
    """
    print()
    print("*******************************************")
    print("*                                         *")
    print("*   WELCOME TO THE TASK MANAGEMENT APP!   *")
    print("*                                         *")
    print("*******************************************")
    
    while True:
        menu()

if __name__ == "__main__":
    main()