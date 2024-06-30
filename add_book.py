from db_connection import connect_db, Error

def add_book():
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()
            
            title = input("Enter book title: ").title()
            availability = True
            new_book = (title, availability)
            
            query = "INSERT INTO books (title, availability) VALUES (%s, %s)"

            cursor.execute(query, new_book)

            conn.commit() #fully commits the changes we are trying to make
            print(f"{title} has been succesfully added!")

        except Error as e:
            print(f"Error: {e}")

        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()

