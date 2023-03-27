import sqlite3

# Define DBOperation class to manage all data into the database. 
# Give a name of your choice to the database

class DBOperations:
# Creating table for the first time.
    sql_create_table_firsttime = """CREATE TABLE IF NOT EXISTS Employees
                                    (employeeID INTEGER UNIQUE PRIMARY KEY,
                                    title VARCHAR(10),
                                    forename VARCHAR(25),
                                    surname VARCHAR(25),
                                    nationality VARCHAR(25),
                                    age INTEGER,
                                    email VARCHAR(25),
                                    telephone INTEGER,
                                    salary INTEGER,
                                    startdate INTEGER,
                                    enddate INTEGER)"""

    sql_create_table = """CREATE TABLE Employees
                                    (employeeID INTEGER UNIQUE PRIMARY KEY,
                                    title VARCHAR(10),
                                    forename VARCHAR(25),
                                    surname VARCHAR(25),
                                    nationality VARCHAR(25),
                                    age INTEGER,
                                    email VARCHAR(25),
                                    telephone INTEGER,
                                    salary INTEGER,
                                    startdate INTEGER,
                                    enddate INTEGER)"""



# Inserting data of all the employees
    # inserting question mark (?) at values so we can substitute with parameters later
    sql_insert = """INSERT INTO Employees (employeeID, title, forename, surname, nationality, age, email, telephone, salary, startdate, enddate)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""



# Displaying Employees Data
    # Displaying record based on EmployeeID in ascending order
    sql_select_all = """SELECT *
                        FROM Employees
                        ORDER BY employeeID ASC"""

    # Displaying record where employees is currently working in ABC company and order by working experience. Note that There's no enddate for current employees.
    sql_select_current = """SELECT employeeID, title, forename, surname, nationality, age, email, telephone, salary, startdate, enddate
                        FROM Employees
                        WHERE enddate = 'NULL'
                        ORDER BY startdate ASC"""

    # Displaying record where employees has left ABC company
    sql_select_resign = """SELECT employeeID, title, forename, surname, nationality, age, email, telephone, salary, startdate, enddate
                           FROM Employees
                           WHERE enddate != 'NULL'"""

    # Displaying total salary of current employees in ABC company
    sql_total_salary = """SELECT ROUND(sum(salary),2) AS 'Total Salary'
                          FROM Employees
                          WHERE enddate = 'NULL'"""

    # Displaying average salary of current employees in ABC company
    sql_avg_salary = """SELECT ROUND(avg(salary),2) AS 'Average Salary'
                          FROM Employees
                          WHERE enddate = 'NULL'"""
    


# Searching data of employees (information to be distinct)
    # Search by employees ID
    sql_search_all = """SELECT *
                    FROM Employees
                    WHERE employeeID = ?"""

    # Search by Employees email
    sql_search_email = """SELECT *
                        FROM Employees
                        WHERE email = ?"""



## Updating data of employees
    # Update all information of employees
    sql_update_all = """UPDATE Employees
                        SET title = ?, forename = ?, surname = ?, nationality = ?,age = ?, email = ?, telephone = ?, salary = ?, startdate = ?, enddate = ?
                        WHERE employeeID = ?"""

    # Update title of Employees
    sql_update_newID = """UPDATE Employees
                          SET employeeID = ?
                          WHERE employeeID = ?"""

    # Update title of Employees
    sql_update_title = """UPDATE Employees
                        SET title = ?
                        WHERE employeeID = ?"""

    # Update forename of Employees
    sql_update_forename = """UPDATE Employees
                        SET forename =?
                        WHERE employeeID = ?"""
                        
    # Update surname of Employees
    sql_update_surname = """UPDATE Employees
                        SET surname = ?
                        WHERE employeeID = ?"""

    # Update nationality of Employees
    sql_update_nationality = """UPDATE Employees
                            SET nationality = ?
                            WHERE employeeID = ?"""

    # Update age of Employees
    sql_update_age = """UPDATE Employees
                        SET age = ?
                        WHERE employeeID = ?"""

    # Update email of employees
    sql_update_email = """UPDATE Employees
                        SET email = ?
                        WHERE employeeID = ?"""

    # Update telephone number of employees
    sql_update_telephone = """UPDATE Employees
                        SET telephone = ?
                        WHERE employeeID = ?"""

    # Update salary of employees
    sql_update_salary = """UPDATE Employees
                        SET salary = ?
                        WHERE employeeID = ?"""

    # Update employees start working date in ABC company
    sql_update_startdate = """UPDATE Employees
                                SET startdate = ?, enddate = ?
                                WHERE employeeID = ?"""

    # Update date of employees leaving ABC company
    sql_update_enddate = """UPDATE Employees
                                SET enddate = ?
                                WHERE employeeID = ?"""


# Delete employees data from ABC company
    sql_delete_data = """DELETE FROM Employees
                         WHERE employeeID = ?"""
  
 
# Create table for the first time
    def __init__(self):
        try:
            self.conn = sqlite3.connect("Employees.db")
            self.cur = self.conn.cursor()
            self.cur.execute(self.sql_create_table_firsttime)
            self.conn.commit()
        except Exception as e:
            print(e)
        finally:
            self.conn.close()

    def get_connection(self):
        self.conn = sqlite3.connect("Employees.db")
        self.cur = self.conn.cursor()

# Create table
    def create_table(self):
        try:
            self.get_connection()
            self.cur.execute(self.sql_create_table)
            self.conn.commit()
            print("Table created successfully! Returning to Main Menu.")
        except Exception as e:
            print(e)
        finally:
            self.conn.close()


# Inserting data for company ABC
    def insert_data(self):
        try:
            self.get_connection()
            print("\nINSERTING NEW DATA:")
            print("*******************")

            emp = Employee() # Define Emp as employee

            emp.set_employee_id(int(input("Enter Employee ID: "))) # Input employee id and set as integer
            emp.set_employee_title(input("Enter Title: ")) # Input employee title
            emp.set_employee_forename(input("Enter Forename: ")) # Input forename
            emp.set_employee_surname(input("Enter Surname: ")) # Input surname
            emp.set_employee_nationality(input("Enter Nationality : ")) # Input nationality
            emp.set_employee_age(int(input("Enter Age: "))) # Input age
            emp.set_employee_email(input("Enter Email: ")) # Input email
            emp.set_employee_telephone(int(input("Enter Telephone No.: "))) # Input telephone number.
            emp.set_employee_salary(float(input("Enter Salary: "))) # Input salary with decimal
            emp.set_employee_startdate(input("Enter Start Date as Employee (DD/MM/YYYY): ")) # Input starting date as employee
            emp.set_employee_enddate(input("Enter End Date as Employee (DD/MM/YYYY): "))
            
            self.cur.execute(self.sql_insert,tuple(str(emp).split("\n")))
            self.conn.commit()
            print("Inserted data successfully! Returning to Main Menu.")
            # print("Total number of rows created:", conn.total_changes)
        except Exception as e:
            print(e)
        finally:
            self.conn.close()

# Selecting all data from the database for company ABC
    def select_all(self):
        try:
            self.get_connection()
            self.cur.execute(self.sql_select_all)
            results = self.cur.fetchall()
            if len(results) ==0:
                print ("No data available. Please input Employees data!")
        # Retriving data from the table created earlier.
            else:
                for row in results:
                    print("\n""Employee ID = ", row[0])
                    print("Title = ", row[1])
                    print("Forename = ", row[2])
                    print("Surname = ", row[3])
                    print("Nationality = ", row[4])
                    print("Age = ", row[5])
                    print("Email = ", row[6])
                    print("Telephone No. =", row[7])
                    print("Salary = ", row[8])
                    print("Start_Date = ", row[9])
                    print("End_Date = ", row [10])                   
        except Exception as e:
            print(e)
        finally:
            self.conn.close()

# Selecting all data of current employee from the database for company ABC
    def select_current(self):
        try:
            self.get_connection()
            self.cur.execute(self.sql_select_current)
            results = self.cur.fetchall()
            if len(results) ==0:
                print ("No data available. Please input Employees data!")
        # Retriving data from the table created earlier.
            else:
                for row in results:
                    print("\n""Employee ID = ", row[0])
                    print("Title = ", row[1])
                    print("Forename = ", row[2])
                    print("Surname = ", row[3])
                    print("Nationality = ", row[4])
                    print("Age = ", row[5])
                    print("Email = ", row[6])
                    print("Telephone No. =", row[7])
                    print("Salary = ", row[8])
                    print("Start_Date = ", row[9])
                    print("End_Date = ", row [10])
        except Exception as e:
            print(e)
        finally:
            self.conn.close()

# Selecting all data of employee who has left company ABC from the database
    def select_resign(self):
        try:
            self.get_connection()
            self.cur.execute(self.sql_select_resign)
            results = self.cur.fetchall()
            if len(results) ==0:
                print ("No data available. Please input Employees data!")
        # Retriving data from the table created earlier.
            else:
                for row in results:
                    print("\n""Employee ID = ", row[0])
                    print("Title = ", row[1])
                    print("Forename = ", row[2])
                    print("Surname = ", row[3])
                    print("Nationality = ", row[4])
                    print("Age = ", row[5])
                    print("Email = ", row[6])
                    print("Telephone No. =", row[7])
                    print("Salary = ", row[8])
                    print("Start_Date = ", row[9])
                    print("End_Date = ", row [10])
        except Exception as e:
            print(e)
        finally:
            self.conn.close()

# Displaying total compensation of current employee for company ABC
    def total_salary(self):
        try:
            self.get_connection()
            self.cur.execute(self.sql_total_salary)
            results = self.cur.fetchall()
            if len(results) ==0:
                print ("No data available. Please input Employees data!")
        # Retriving data from the table created earlier.
            else:
                for row in results:
                    print("\n""Total compensation = ", row[0])
        except Exception as e:
            print(e)
        finally:
            self.conn.close()

# Displaying average salary of current employee in company ABC
    def avg_salary(self):
        try:
            self.get_connection()
            self.cur.execute(self.sql_avg_salary)
            results = self.cur.fetchall()
            if len(results) ==0:
                print ("No data available. Please input Employees data!")
        # Retriving data from the table created earlier.
            else:
                for row in results:
                    print("\n""Average salary of current employee  = ", row[0])
        except Exception as e:
            print(e)
        finally:
            self.conn.close()

# Searching Employee information from the database
    def search_data(self):
        try:
            self.get_connection()

            # Provide a list of data/field for searching
            print("\n SEARCH MENU:")
            print("**************")
            print("Please search based on information/ field that you have")
            print("1. Employee ID")
            print("2. Email")
            print("3. Return to Main Menu")
            
            selection = input("\nPlease enter your selection: ")
            if selection == "1":
                employeeID = int(input("Enter Employee ID: "))
                self.cur.execute(self.sql_search_all,[str(employeeID)])
                result = self.cur.fetchone()
                if type(result) == type(tuple()):
                    for index, detail in enumerate(result):
                        if index == 0:
                            print("\nEmployee ID: " + str(detail))
                        elif index == 1:
                            print("Employee Title: " + detail)
                        elif index == 2:
                            print("Employee Forename: " + detail)
                        elif index == 3:
                            print("Employee Surname: " + detail)
                        elif index == 4:
                            print("Employee Nationality:" + detail)
                        elif index == 5:
                            print("Employee Age: " + str(detail))
                        elif index == 6:
                            print("Employee Email: " + detail)
                        elif index == 7:
                            print("Employee Telephone No.: " + str(detail))
                        elif index == 8:
                            print("Employee Salary: " + str(detail))
                        elif index == 9:
                            print("Employee Start Date: " + str(detail))
                        else:
                            print("Employee End Date: "+ str(detail))
                else:
                    print ("No Record. Please reselect Employee ID.""\n")
                    return db_ops.search_data()
                self.conn.commit()

            elif selection == "2":
                email = (input("Enter Email: "))
                self.cur.execute(self.sql_search_email, [email])
                result = self.cur.fetchone()
                if type(result) == type(tuple()):
                    for index, detail in enumerate(result):
                        if index == 0:
                            print("\nEmployee ID: " + str(detail))
                        elif index == 1:
                            print("Employee Title: " + detail)
                        elif index == 2:
                            print("Employee Forename: " + detail)
                        elif index == 3:
                            print("Employee Surname: " + detail)
                        elif index == 4:
                            print("Employee Nationality:" + detail)
                        elif index == 5:
                            print("Employee Age: " + str(detail))
                        elif index == 6:
                            print("Employee Email: " + detail)
                        elif index == 7:
                            print("Employee Telephone No.: " + str(detail))
                        elif index == 8:
                            print("Employee Salary: " + str(detail))
                        elif index == 9:
                            print("Employee Start Date: " + str(detail))
                        else:
                            print("Employee End Date: "+ str(detail))
                else:
                    print ("No Record. Please reselect Email Address. ""\n")
                    return db_ops.search_data()
                self.conn.commit() 
            elif selection == "3":
                return
            else:
                print("Invalid Input. Please reselect either 1 or 2!""\n")
                return db_ops.search_data()
        except Exception as e:
            print(e)
        finally:
            self.conn.close()

# Updating data of employee into database
    def update_data(self):
        try:
            self.get_connection()
            print("\n UPDATE MENU:")
            print("**************")
            # Provide a list of data/field for user/admin to update
            print("Please select the information/field that you wish to update for the employee")
            print("1. Employee ID")
            print("2. Title")
            print("3. Forename")
            print("4. Surname")
            print("5. Nationality")
            print("6. Age")
            print("7. Email")
            print("8. Telephone No.")
            print("9. Salary")
            print("10. Start Date")
            print("11. End Date")
            print("12. Return to Main Menu","\n")

            selection = input("Please enter your selection: ")
            # Updating Employee ID
            if selection == "1":
                employeeID_cur = input("Please enter Existing Employee ID: ")
                employeeID_new = input("Please enter New Employee ID: ")
                info = employeeID_new, employeeID_cur
                result = self.cur.execute(self.sql_update_newID, info)
                self.conn.commit()

            # Updating Employee Title
            elif selection == "2":
                employeeID_cur = input("Please enter Existing Employee ID: ")
                employee_title = input("Please enter New Title: ")
                info = employee_title, employeeID_cur
                result = self.cur.execute(self.sql_update_title, info)
                self.conn.commit()       

            # Updating Employee Forename
            elif selection == "3":
                employeeID_cur = input("Please enter Existing Employee ID: ")
                employee_forename = input("Please enter New Forename: ")
                info = employee_forename, employeeID_cur
                result = self.cur.execute(self.sql_update__forename,info)
                self.conn.commit()

            # Updating Employee Surname
            elif selection == "4":
                employeeID_cur = input("Please enter Existing Employee ID: ")
                employee_surname = input("Please enter New Surname: ")
                info = employee_surname, employeeID_cur
                result = self.cur.execute(self.sql_update_surname, info)
                self.conn.commit()

            # Updating Employee Nationality
            elif selection == "5":
                employeeID_cur = input("Please enter Existing Employee ID: ")
                employee_nationality = input("Please enter New Nationality: ")
                info = employee_nationality, employeeID_cur
                result = self.cur.execute(self.sql_update_nationality, info)
                self.conn.commit()

            # Updating Employee Age
            elif selection == "6":
                employeeID_cur = input("Please enter Existing Employee ID: ")
                employee_age = input("Please enter New age: ")
                info = employee_age, employeeID_cur
                result = self.cur.execute(self.sql_update_age, info)
                self.conn.commit()

            # Updating Employee Email
            elif selection == "7":
                employeeID_cur = input("Please enter Existing Employee ID: ")
                employee_email = input("Please enter New Email: ")
                info = employee_email, employeeID_cur
                result = self.cur.execute(self.sql_update_email, info)
                self.conn.commit()
            
            # Updating Employee Telephone No.
            elif selection == "8":
                employeeID_cur = input("Please enter Existing Employee ID: ")
                employee_telephone = input("Please enter New Telephone No.: ")
                info = employee_telephone, employeeID_cur
                result = self.cur.execute(self.sql_update_telephone, info)
                self.conn.commit()

            # Updating Employee Salary
            elif selection == "9":
                employeeID_cur = input("Please enter Existing Employee ID: ")
                employee_salary = input("Please enter New salary: ")
                info = employee_salary, employeeID_cur
                result = self.cur.execute(self.sql_update_salary, info)
                self.conn.commit()      

            # Updating Employee Starting Date of Working in ABC company
            elif selection == "10":
                employeeID_cur = input("Please enter Existing Employee ID: ")
                employee_startdate = input("Please enter Start Date: ")
                info = employee_startdate, employeeID_cur
                result = self.cur.execute(self.sql_updat_startdate, info)
                self.conn.commit()  

            # Updating Employee Last Day of Working in ABC Company
            elif selection == "11":
                employeeID_cur = input("Please enter Existing Employee ID: ")
                employee_enddate = input("Please enter End date: ")
                info = employee_enddate, employeeID_cur
                result = self.cur.execute(self.sql_update_enddate, info)
                self.conn.commit()
            
            # Returning to Main Menu
            elif selection == "12":
                print("Returning to Main Menu...")
                return
            # Any input number that is not in range 1-11 will deem as invalid input.
            # User will have to retype the number
            else:
                print("Invalid Input. Please reselect any number from 1 to 12!")
                return db_ops.update_data()
        
            if result.rowcount != 0:
                print ("\n" + str(result.rowcount)+ "Row(s) affected.")
                print ("Infomation Updated! Returning to Main Menu.")
            else:
                print ("Cannot find this record in the database. Returning to Main Menu.")

        except Exception as e:
            print(e)
        finally:
            self.conn.close()

# Define Delete_data method to delete data from the table. The user will need to input the employee id to delete the corrosponding record. 
    def delete_data(self):
        try:
            self.get_connection()
            print("\n DELETE MENU:")
            print("**************")
            print("WARNING - Deleted data cannot be recovered.")
            selection = input("\nType 'Y' to proceed or any other letter to cancelled: ")
            if selection == "Y" or selection == "y":
                employeeID = int(input("\nEnter Employee ID: "))
                result = self.cur.execute(self.sql_delete_data,[str(employeeID)])
                self.conn.commit()
            else:
                print("\nCancelled. Returning to Main Menu...")
                return
                    
            if result.rowcount != 0:
                print ("\n" + str(result.rowcount)+ "Row(s) affected.")
                print ("Employee's record with ID = " + str(employeeID) + " deleted!" + "\n")
                print ("Please refer to remaining database:")
                db_ops.select_all()

            else:
                print ("\nCannot find this record in the database. Return to Delete Menu.")
                return db_ops.delete_data()

        except Exception as e:
            print(e)
        finally: 
            self.conn.close()

        
class Employee:
    def __init__(self):
        self.employeeID = 0
        self.title = ''
        self.forename = ''
        self.surname = ''
        self.nationality = ''
        self.age = 0
        self.email = ''
        self.telephone = 0
        self.salary = 0.00
        self.startdate = ''
        self.enddate = ''

    def set_employee_id(self, employeeID):
        self.employeeID = employeeID

    def set_employee_title(self, title):
        self.title = title

    def set_employee_forename(self, forename):
        self.forename = forename
  
    def set_employee_surname(self, surname):
        self.surname = surname

    def set_employee_nationality(self, nationality):
        self.nationality = nationality

    def set_employee_age(self, age):
        self.age = age
  
    def set_employee_email(self, email):
        self.email = email
  
    def set_employee_telephone(self, telephone):
        self.telephone = telephone

    def set_employee_salary(self, salary):
        self.salary = salary
    
    def set_employee_startdate(self, startdate):
        self.startdate = startdate

    def set_employee_enddate(self, enddate):
        self.enddate = enddate

    def get_employee_id(self):
        return self.employeeId

    def get_employee_title(self):
        return self.title
  
    def get_employee_forename(self):
        return self.forename
  
    def get_employee_surname(self):
        return self.surname

    def get_emplyee_nationality(self):
        return self.nationality

    def get_employee_age(self):
        return self.age
  
    def get_employee_email(self):
        return self.email
  
    def get_employee_telephone(self):
        return self.telephone

    def get_employee_salary(self):
        return self.salary

    def get_employee_stardate(self):
        return self.startdate
    
    def get_employee_enddate(self):
        return self.enddate

    def __str__(self):
        return str(self.employeeID)+"\n"+self.title+"\n"+ self.forename+"\n"+self.surname+"\n"+self.nationality+"\n"+str(self.age)+"\n"+self.email+"\n"+str(self.telephone)+"\n"+str(self.salary)+"\n"+str(self.startdate)+"\n"+str(self.enddate)


# The main function will parse arguments. 
# These argument will be definded by the users on the console.
# The user will select a choice from the menu to interact with the database.
  
while True:
    print ("\n MAIN MENU:")
    print ("*************")
    print (" 1. Create table Employees for ABC Company")
    print (" 2. Insert data into Employees database for ABC Company")
    print (" 3. Select all data in Employees database for ABC Company")
    print (" 4. Search an employee")
    print (" 5. Update data (to update a record)")
    print (" 6. Delete data (to delete a record)")
    print (" 7. Select all data of current employees in ABC Company")
    print (" 8. Select all data of former employees in ABC Company")
    print (" 9. Total compensation of current employees in ABC Company ")
    print (" 10. Average Salary of current employees in ABC Company")
    print (" 11. Exit\n")

    __choose_menu = input("Enter your choice: ")
    db_ops = DBOperations()
    if __choose_menu == "1":
        db_ops.create_table()
    elif __choose_menu == "2":
        db_ops.insert_data()
    elif __choose_menu == "3":
        db_ops.select_all()
    elif __choose_menu == "4":
        db_ops.search_data()
    elif __choose_menu == "5":
        db_ops.update_data()
    elif __choose_menu == "6":
        db_ops.delete_data()
    elif __choose_menu == "7":
        db_ops.select_current()
    elif __choose_menu == "8":
        db_ops.select_resign()
    elif __choose_menu == "9":
        db_ops.total_salary()
    elif __choose_menu == "10":
        db_ops.avg_salary()
    elif __choose_menu == "11":
        exit(0)
    else:
        print ("Invalid Choice. Please re-enter your choice from 1 to 11")



