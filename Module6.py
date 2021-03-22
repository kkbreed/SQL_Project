import mysql.connector
#This imports the MYSQL library for the connector to establish a connector with MYSQL (Boronczyk, 2015)
#This was installed via PIP
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="admin",
  database="classicmodels"
)
#The code above is used to connect to the MYSQL database
#using the user, passwd, and host credentials.

def show_data(mycursor):
    # Get the cursor to process rows in result set
    mycursor.execute("SELECT * FROM payments WHERE MONTH(paymentDate) = 12")
    # Obtains the record used for the payment
    myresult = mycursor.fetchall()
    # We use the fetch command to retrieve all rows in the table (Boronczyk, 2015)
    print("%-20s %-20s %-20s %-10s" %("Customer Number","Check Number", "Payment Date", "Amount"))
    for x in myresult:
      print("%-20d %-20s %-20s %-8.2f" %(x[0], x[1], x[2], x[3]))


mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM payments WHERE MONTH(paymentDate) = 12")
myresult = mycursor.fetchall()
print("Before Rebate")
#Displays results before the rebate
print()
show_data(mycursor)
sql = "UPDATE payments SET amount = amount*0.99 WHERE MONTH(paymentDate) = 12"
mycursor.execute(sql)
mydb.commit()
#Commit the changes made
print()
print("After Rebate")
#Displays the results after the rebate
print()
show_data(mycursor)
