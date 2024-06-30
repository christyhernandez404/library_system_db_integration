import time
import os
from classes import User, Book
from add_book import add_book
from add_user import add_user
from borrow_book import borrow_book
from fetch_book import fetch_book,fetch_all_books
from fetch_user import fetch_user,fetch_all_users
from return_book import return_book


def clear():
    os.system('cls')

def main():
    while True:
        ans = input(""""
Welcome to the Library Management System!
                    
    Main Menu:
    1. Book Operations
    2. User Operations
    3. Quit           
                    
Enter the corresponding number for the action you'd like to take here: """)
        if ans == '1':
            book_ops()
            time.sleep(6)
            clear()
        elif ans == '2':
            user_ops()
            time.sleep(6)
            clear()
        elif ans == '4':
            print("Thanks for using the Library Management System!")
            break
        else:
            print("Invalid data entry. Try again")

def book_ops():
    while True:
        ans = input(""""
Welcome to the Library Management System!
                    
Book Operations:
    1. Add a new book
    2. Borrow a book
    3. Return a book
    4. Search for a book
    5. Display all books
    6. Main Menu
                    
Enter the corresponding number for the action you'd like to take here: """)
        if ans == '1':
            add_book()
            time.sleep(8)
            clear()
        elif ans == '2':
            borrow_book()
            time.sleep(6)
        elif ans == '3':
            return_book()
            time.sleep(6)
        elif ans == '4':
            fetch_book()
            time.sleep(6)
            clear()
        elif ans == '5':
            fetch_all_books()
            time.sleep(6)
            clear()
        elif ans == '6':
            main()
            time.sleep(6)
            clear()
        else:
            print("Invalid data entry. Try again")


def user_ops():
    while True:
        ans = input(""""
Welcome to the Library Management System!
                    
User Operations:
    1. Add a new user
    2. View user details
    3. Display all users
    4. Main Menu         
                    
Enter the corresponding number for the action you'd like to take here: """)

        if ans == '1':
            add_user()
            time.sleep(6)
            clear()
        elif ans == '2':
            fetch_user()           
            time.sleep(6)
            clear()
        elif ans == '3':
            fetch_all_users()
            time.sleep(6)
            clear()
        elif ans == '4':
            main()
            time.sleep(6)
            clear()
        else:
            print("Invalid data entry. Try again")



main()
