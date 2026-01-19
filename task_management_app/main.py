"""
main.py: THIS IS THE ENTRY POINT OF THE TASK MANAGEMENT APP
usage: python3 main.py
"""

from app.cli_menu import menu #import the main menu 
from dotenv import load_dotenv #import the environment variable for database credentials

def main():
    """
    Execute the main menu loop until the user exits or clicks 0
    """
    load_dotenv()
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