from db_connection import connect_db, Error

def fetch_all_books():
    conn = connect_db()

    if conn is not None:
        try:
            cursor = conn.cursor() #cursor is our messager to travel back and forth from Python file to SQL. when we have a query, we use the cursor as the messenger. 

            #select all from customer table
            query = 'SELECT * FROM books'

            #execute our query
            cursor.execute(query)

            for id, name, availability in cursor.fetchall():
                print(f" ID: {id}, Title: {name}, Availability: {availability}")

        except Error as e:
            print(f"Error: {e}")

        finally:
            cursor.close()
            conn.close()


def fetch_book():
    conn = connect_db()

    if conn is not None:
        try:
            book_name = input("what is the name of the book you are looking for?").title()

            cursor = conn.cursor()

            query = "SELECT * FROM books WHERE title = %s" #the marker is %s

            cursor.execute(query, (book_name,))

            row = cursor.fetchall()
            for id, title, availability in row:
                print(f" ID: {id}, Title: {title}, Availability: {availability}")

        except Error as e:
            print(f"Error: {e}")
        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()
