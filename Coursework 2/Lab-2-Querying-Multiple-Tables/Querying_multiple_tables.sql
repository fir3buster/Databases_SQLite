CREATE TABLE Item (

ItemName VARCHAR (30) NOT NULL,
ItemType CHAR(1) NOT NULL,
ItemColour VARCHAR(10),

PRIMARY KEY (ItemName));

CREATE TABLE Employee (

EmployeeNumber SMALLINT UNSIGNED NOT NULL ,
EmployeeName VARCHAR(10) NOT NULL ,
EmployeeSalary INTEGER UNSIGNED NOT NULL ,
DepartmentName VARCHAR(10) NOT NULL REFERENCES Department,
BossNumber SMALLINT UNSIGNED NOT NULL REFERENCES Employee,

PRIMARY KEY (EmployeeNumber));

CREATE TABLE Department (

DepartmentName VARCHAR(10) NOT NULL,
DepartmentFloor SMALLINT UNSIGNED NOT NULL,
DepartmentPhone SMALLINT UNSIGNED NOT NULL,
EmployeeNumber SMALLINT UNSIGNED NOT NULL REFERENCES
Employee,

PRIMARY KEY (DepartmentName));

CREATE TABLE Sale (

SaleNumber INTEGER UNSIGNED NOT NULL,
SaleQuantity SMALLINT UNSIGNED NOT NULL DEFAULT 1,
ItemName VARCHAR(30) NOT NULL REFERENCES Item,
DepartmentName VARCHAR(10) NOT NULL REFERENCES Department,

PRIMARY KEY (SaleNumber));

CREATE TABLE Supplier (

SupplierNumber INTEGER UNSIGNED NOT NULL,
SupplierName VARCHAR(30) NOT NULL,

PRIMARY KEY (SupplierNumber));

CREATE TABLE Delivery (

DeliveryNumber INTEGER UNSIGNED NOT NULL,
DeliveryQuantity SMALLINT UNSIGNED NOT NULL DEFAULT 1,
ItemName VARCHAR(30) NOT NULL REFERENCES Item,
DepartmentName VARCHAR(10) NOT NULL REFERENCES Department,
SupplierNumber INTEGER UNSIGNED NOT NULL REFERENCES
Supplier,

PRIMARY KEY (DeliveryNumber));


.mode column
.headers on
.mode tabs
.separator "\t"

.import delivery.txt Delivery
.import department.txt Department
.import employee.txt Employee
.import item.txt Item
.import sale.txt Sale
.import supplier.txt Supplier


SELECT *
FROM Delivery;
.print

SELECT *
FROM Department;
.print

SELECT *
FROM Employee;
.print

SELECT *
FROM Item;
.print

SELECT *
FROM Sale;
.print

SELECT *
FROM Supplier;


.print
.print "1. What are the names of employees in the Marketing Department?"
.print

SELECT EmployeeName
FROM Employee
WHERE DepartmentName = 'Marketing'
ORDER BY EmployeeName;

.print
.print "2. Find the average salary of the employees in the Clothes department."
.print

SELECT AVG(EmployeeSalary) AS 'Average Salary'
FROM Employee
WHERE DepartmentName = 'Clothes';

.print
.print "3. List the items delivered by exactly one supplier (i.e. the items always delivered by the same supplier)"
.print

SELECT ItemName, SupplierNumber
FROM Delivery
GROUP BY ItemName 
HAVING COUNT (DISTINCT SupplierNumber) = 1;

.print
.print "4. List the departments for which each item delivered to the department is delivered to some other department as well."
.print

SELECT DISTINCT DepartmentName
FROM Delivery
WHERE DepartmentName NOT IN
    (SELECT DepartmentName
    FROM Delivery
    GROUP BY ItemName
    HAVING COUNT (DISTINCT DepartmentName) = 1);


.print
.print "5. Among all the departments with a total salary greater than £25000, find the departments that sell Stetsons. "
.print

SELECT DISTINCT Employee.DepartmentName
FROM (Delivery NATURAL JOIN Employee)
GROUP BY Employee.EmployeeSalary HAVING SUM(Employee.EmployeeSalary) > 25000 AND Employee.DepartmentName IN
    (SELECT Delivery.DepartmentName
    FROM Delivery
    WHERE ItemName = 'Stetsons');

.print
.print "6. Find the suppliers that deliver compasses and at least three other kinds of item."
.print

SELECT DISTINCT Delivery.SupplierNumber, Supplier.SupplierName 
FROM (Supplier NATURAL JOIN Delivery)
WHERE ItemName = 'Compass' AND SupplierNumber IN 
    (SELECT SupplierNumber
    FROM Delivery
    WHERE ItemName <> 'Compass'
    GROUP BY Delivery.SupplierNumber
    HAVING COUNT (DISTINCT ItemName) >= 3)
ORDER BY SupplierNumber;



