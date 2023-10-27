import sqlite3

def create_database():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()

    # Create the 'user_info' table if it doesn't exist
    c.execute("CREATE TABLE IF NOT EXISTS user_info (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, username TEXT, full_name TEXT,results INT);")
    conn.commit()
    conn.close()

create_database()

def add_user_info(user_id, username, full_name, results):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()

    # Insert the new user information into the 'user_info' table
    c.execute('''INSERT INTO user_info (user_id, username,full_name,results)
                 VALUES (?, ?, ?,?)''', (user_id, username,full_name,results))

    conn.commit()
    conn.close()
def add_user_info(user_id, username, full_name, results):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()

    # Check if the user's ID is already in the database
    c.execute("SELECT results FROM user_info WHERE user_id = ?", (user_id,))
    existing_results = c.fetchone()

    if existing_results is not None:
        # If the user's ID is in the database, fetch the existing results
        existing_results = existing_results[0]
        # Add the new results to the existing results
        total_results = existing_results + results

        # Update the user's results in the database
        c.execute("UPDATE user_info SET results = ? WHERE user_id = ?", (total_results, user_id))
    else:
        # If the user's ID is not in the database, insert a new record
        c.execute('''INSERT INTO user_info (user_id, username, full_name, results)
                     VALUES (?, ?, ?, ?)''', (user_id, username, full_name, results))

    conn.commit()
    conn.close()


# def selfing():
#     con=sqlite3.connect("data.db")
#     c=con.cursor()
#     c.execute('''INSERT INTO user_info (user_id, username, full_name, results)
#                  VALUES (?, ?, ?, ?)''', (777777, "Sama", "Jamandar","333"))
#
#     con.commit()
#     con.close()
# selfing()