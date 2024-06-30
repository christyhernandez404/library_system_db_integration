from db_connection import connect_db, Error

def return_book():
    conn = connect_db()
    if conn is not None:
        try:
            with conn.cursor() as cursor:
                user_id = input("What is your library id?")

                # get user id from DB
                cursor.execute("SELECT id FROM users WHERE id = %s", (user_id,))
                user_result = cursor.fetchone()
                if not user_result:
                    print("Library ID/user not found")
                    return

                # get book name and see if it exists in the library
                title = input("Enter the title of the book you'd like to return: ").title()
                cursor.execute("SELECT * FROM books WHERE title = %s", (title,))
                book_result = cursor.fetchone()
                if not book_result:
                    print("Book not found")
                    return

                # get book_id
                book_id = book_result[0]

                # check if book is borrowed
                cursor.execute("SELECT * FROM borrowed_books WHERE book_id = %s", (book_id,))
                borrowed_book = cursor.fetchone()
                if not borrowed_book:
                    print("This book has not been borrowed.")
                    return

                # update book availability back to True
                cursor.execute("UPDATE books SET availability = True WHERE id = %s", (book_id,))
                cursor.execute("DELETE FROM borrowed_books WHERE id = %s", (book_id,))

                conn.commit()  # fully commits the changes
                print(f"{title} has been successfully returned!")

        except Error as e:
            print(f"Error: {e}")

        finally:
            conn.close()
