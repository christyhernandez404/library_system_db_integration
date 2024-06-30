from db_connection import connect_db, Error
import re

def add_user():
    conn = connect_db()
    if conn is not None:
        try:
            with conn.cursor() as cursor:
                name = input("what is your name?").title()
                email_valid = False
                while not email_valid:
                    email = input("Enter email address: ").lower()
                    if re.fullmatch(r"[\w.-]+@[\w-]+\.[a-z]{2,3}", email):
                        email_valid = True
                        new_user = (name, email)
                        query = "INSERT INTO users (name, email) VALUES (%s, %s)"
                        cursor.execute(query, new_user)
                        conn.commit()  # fully commits the changes we are trying to make (adding data to the customer tables)
                        print(f"{name} has been added successfully!")
                    else:
                        print("Invalid email. Try again")

        except Error as e:
            print(f"Error: {e}")

        finally:
            conn.close()

