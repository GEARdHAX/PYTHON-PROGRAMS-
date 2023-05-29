import mysql.connector
# Replace 'host', 'database', 'user', and 'password' with your database credentials
try:
    conn = mysql.connector.connect(
    host='localhost',
    database='world',
    user='root',
    password='1234'
)
    try:
        if conn.is_connected():
            print('\nSuccessfully connected to Database\n')
    finally:
        cursor = conn.cursor()

        n = int(input("Enter the number of values to insert: "))

        for i in range(n):
            name = input("Enter name: ")
            phnum = input("Enter phone number: ")
            city = input("Enter city: ")
            income = float(input("Enter income: "))

            # SQL query to insert values into the 'users' table
            query = "INSERT INTO users (name, phnum, city, income) VALUES (%s, %s, %s, %s)"
            values = (name, phnum, city, income)

            # Execute the query
            cursor.execute(query, values)

            # Commit the changes to the database
            conn.commit()

    print("Record inserted successfully.")

    query2 = "SELECT * FROM users"
    
    cursor.execute(query2)
    rows = cursor.fetchall()
    for i in rows:
        print(i)
    # Close the cursor and the connection
    cursor.close()
    conn.close()
except Exception:
    print("Connection not established!")
