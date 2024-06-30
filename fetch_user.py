from db_connection import connect_db, Error

def fetch_all_users():
    conn = connect_db()

    if conn is not None:
        try:
            cursor = conn.cursor() #cursor is our messager to travel back and forth from Python file to SQL. when we have a query, we use the cursor as the messenger. 

            #select all from customer table
            query = 'SELECT * FROM users'

            #execute our query
            cursor.execute(query)

            for id, name, email in cursor.fetchall():
                print(f" ID: {id}, Title: {name}, Availability: {email}")

        except Error as e:
            print(f"Error: {e}")

        finally:
            cursor.close()
            conn.close()


def fetch_user():
    conn = connect_db()

    if conn is not None:
        try:
            user_name = input("What is the name of the user you are looking for?").title()

            cursor = conn.cursor()

            query = "SELECT * FROM users WHERE name = %s" #the marker is %s

            cursor.execute(query, (user_name,))

            row = cursor.fetchall()
            for id, name, email in row:
                print(f" ID: {id}, Title: {name}, Availability: {email}")

        except Error as e:
            print(f"Error: {e}")
        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()

