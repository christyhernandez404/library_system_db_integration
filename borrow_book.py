from db_connection import connect_db, Error

def borrow_book():
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()
            
            user_id = input("What is your library id?")

            #get user id from DB
            cursor.execute("SELECT id FROM users WHERE id = %s",(user_id,))
            user_result = cursor.fetchone()
            if not user_result:
                print("Library ID/user not found")
                return
    

            title = input("Enter the title of the book you'd like to borrow: ").title()
            #get book id
            cursor.execute("SELECT * FROM books WHERE title = %s AND availability = True", (title,))
            book_result = cursor.fetchone()
            #print book details
            print(f"Book result: {book_result}. 1 = Available, 0 = Unavailable")
            if not book_result:
                print("Book not found or is not available")
                return
            book_id = book_result[0]
           
            #update book availlibity to false
            cursor.execute( "UPDATE books SET availability = False WHERE id = %s", (book_id,))
            cursor.execute("INSERT INTO borrowed_books (user_id, book_id, borrow_date, return_date) VALUES (%s, %s, CURRENT_DATE, DATE_ADD(CURRENT_DATE, INTERVAL 3 WEEK))",(user_id, book_id))



            conn.commit() #fully commits the changes we are trying to make
            print(f"{title} has been succesfully borrowed!")

        except Error as e:
            print(f"Error: {e}")

        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()
