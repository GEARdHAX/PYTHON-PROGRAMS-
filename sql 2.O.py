import mysql.connector as database

connection = database.connect(
 host="localhost",
 user="root",
 password="1234",
 database="mydb"
)

if connection.is_connected():
  print("\nConnection established ✅\n")
   
  cursor = connection.cursor()
  decision = input("What You want to do? : ")
  
  # <============= Create New Database ===============>
  def create():
   records = int(input("How many Records to create : "))
   for i in range(records):
    name = input("Enter Name : ")
    id = int(input("Enter ID : "))
    salary = int(input("Enter Salary : "))
    insert_query = "INSERT INTO employee (name, id, salary) VALUES (%s, %s, %s)"
    cursor.execute(insert_query, (name, id, salary))
    connection.commit()
    print("\nRecord inserted successfully\n")
   
   # <========== Check All the Inserted Records===========>
  def check():
   cursor.execute("SELECT * FROM employee")
   decision = input("Particular ID (1) / All ID (2) : ")
   if decision=='1':
    row = cursor.fetchall()
    id = int(input("Enter ID You Want to Search : "))
    for i in range(0, len(row)-1):
     for record in row:
      if record[i] == id:
       print(record)
       break
      else:
        print("Record not found")

   elif decision=='2':      
        row = cursor.fetchall()
        if len(row)==0:
          print("Records Not Found")
        else:     
         for i in range(0,len(row)):
          print(row[i]) 
    # <============= Delete Particular Records ===============>
  def delete():
    records = (input("How many Records to delete : "))
    if records.lower() == 'all':
          delete_query = "DELETE FROM employee"
          cursor.execute(delete_query)
          connection.commit()
          print("All records deleted successfully.")
    else:
     records = int(records)
     for i in range(records):
      id = int(input("Enter ID : "))
      delete_query = "DELETE FROM employee WHERE id = %s"
      cursor.execute(delete_query, (id,))
      connection.commit()
      print("\nRecord deleted successfully\n")
    
    
  if decision == "create":
   create()
  elif decision == "check":
   check()
  elif decision == "delete":
   delete()
   
else:
  print("Connection Failed ❌")