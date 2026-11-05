print("""
SQOOP PRACTICAL – TRANSFER DATA BETWEEN MYSQL AND HADOOP
========================================================

1. CHECK REQUIREMENTS (Ubuntu Terminal)
---------------------------------------
java -version
hadoop version
sqoop version
mysql --version
jps

Hadoop services should be running before import/export.

COMPATIBILITY NOTE:
Sqoop 1.4.7 is old and may be difficult to install with modern Java/Hadoop versions. If the lab already has working Sqoop, use that setup and do not change versions just before the practical.

2. START MYSQL AND LOGIN
------------------------
sudo systemctl start mysql
sudo systemctl status mysql
sudo mysql

SQL commands below are typed at the mysql> prompt.

3. CREATE DATABASE AND EMPLOYEES TABLE
--------------------------------------
CREATE DATABASE company;
USE company;

CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    department VARCHAR(50),
    salary INT
);

INSERT INTO employees VALUES
(1, 'Liston', 'IT', 50000),
(2, 'John', 'HR', 40000),
(3, 'David', 'IT', 60000),
(4, 'Sam', 'Finance', 45000),
(5, 'Alex', 'HR', 55000);

View table:
SELECT * FROM employees;

Exit MySQL:
EXIT;

4. CHECK MYSQL JDBC DRIVER
--------------------------
find /usr/share/java -iname '*mysql*connector*.jar'

Note the JAR path if found. The driver must be accessible to Sqoop, usually through its lib directory or classpath.

Check Sqoop:
sqoop version

5. IMPORT MYSQL TABLE INTO HDFS
-------------------------------
Create HDFS directory:
hdfs dfs -mkdir -p /sqoop

Import complete table:
sqoop import \\
--connect jdbc:mysql://localhost:3306/company \\
--username root \\
-P \\
--table employees \\
--target-dir /sqoop/employees \\
--num-mappers 1

Enter the MySQL password when prompted.
If using a separate MySQL user, replace root with that username.

Verify:
hdfs dfs -ls /sqoop/employees
hdfs dfs -cat /sqoop/employees/part-m-00000

6. IMPORT SELECTED COLUMNS
--------------------------
sqoop import \\
--connect jdbc:mysql://localhost:3306/company \\
--username root \\
-P \\
--table employees \\
--columns "id,name" \\
--target-dir /sqoop/selected \\
--num-mappers 1

7. IMPORT SELECTED ROWS USING WHERE
-----------------------------------
sqoop import \\
--connect jdbc:mysql://localhost:3306/company \\
--username root \\
-P \\
--table employees \\
--where "salary > 45000" \\
--target-dir /sqoop/high_salary \\
--num-mappers 1

8. IMPORT WITH COMPRESSION
--------------------------
sqoop import \\
--connect jdbc:mysql://localhost:3306/company \\
--username root \\
-P \\
--table employees \\
--target-dir /sqoop/compressed \\
--compress \\
--compression-codec org.apache.hadoop.io.compress.GzipCodec \\
--num-mappers 1

9. EXPORT DATA FROM HDFS TO MYSQL
---------------------------------
Login to MySQL:
sudo mysql

Create destination table:
USE company;

CREATE TABLE employees_export (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    department VARCHAR(50),
    salary INT
);

Exit MySQL:
EXIT;

Create tab-delimited local file:
mkdir -p ~/sqoop_lab
printf '6\\tPeter\\tIT\\t65000\\n7\\tMary\\tHR\\t48000\\n' > ~/sqoop_lab/new_employees.txt

Upload file to HDFS:
hdfs dfs -mkdir -p /sqoop/export_input
hdfs dfs -put ~/sqoop_lab/new_employees.txt /sqoop/export_input/

Export:
sqoop export \\
--connect jdbc:mysql://localhost:3306/company \\
--username root \\
-P \\
--table employees_export \\
--export-dir /sqoop/export_input \\
--input-fields-terminated-by '\\t' \\
--num-mappers 1

10. VERIFY EXPORT IN MYSQL
---------------------------
sudo mysql

At mysql>:
USE company;
SELECT * FROM employees_export;

11. IMPORTANT SQOOP OPTIONS
---------------------------
sqoop import – import table from database to Hadoop
sqoop export – export HDFS data to database
--columns – select columns
--where – filter rows
--target-dir – specify HDFS destination
-P – prompt for password
--compress – compress imported data
--num-mappers – number of mappers
""")
