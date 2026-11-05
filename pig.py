print("""
APACHE PIG PRACTICAL – PIG LATIN COMMANDS
=========================================

1. CHECK INSTALLATION (Ubuntu Terminal)
---------------------------------------
java -version
hadoop version
pig -version

2. OPEN PIG IN LOCAL MODE
-------------------------
pig -x local

The prompt should look like:
grunt>

Pig Latin commands below are typed at grunt>, NOT in Ubuntu Terminal.
Open another terminal tab with Ctrl + Shift + T for file commands.

3. CREATE AGRICULTURE DATASET (Ubuntu Terminal)
-----------------------------------------------
mkdir -p ~/pig_lab
cd ~/pig_lab
nano crop_production.csv

Enter:
Maharashtra,Pune,Rice,100,500
Maharashtra,Nashik,Wheat,200,800
Gujarat,Ahmedabad,Cotton,300,900
Gujarat,Surat,Rice,150,600
Karnataka,Bangalore,Coffee,250,750
Karnataka,Mysore,Rice,100,450

Save: Ctrl + O, Enter, Ctrl + X

Check Ubuntu username:
whoami

4. PART 1 – AGRICULTURE QUERIES (grunt>)
----------------------------------------
Replace USERNAME in paths with your Ubuntu username.

Load:
agriculture = LOAD '/home/USERNAME/pig_lab/crop_production.csv' USING PigStorage(',') AS (state:chararray, district:chararray, crop:chararray, area:int, production:int);

Display:
DUMP agriculture;

Describe schema:
DESCRIBE agriculture;

Group state-wise:
grouped = GROUP agriculture BY state;
DUMP grouped;

Sort by production, highest first:
sorted = ORDER agriculture BY production DESC;
top = LIMIT sorted 5;
DUMP top;

Store output:
STORE top INTO '/home/USERNAME/pig_lab/data_top.txt' USING PigStorage(',');

Verify in Ubuntu Terminal:
cat ~/pig_lab/data_top.txt

5. OPTIONAL – TRANSFER OUTPUT TO HDFS
-------------------------------------
Exit Pig:
quit;

Check Hadoop services:
jps

Create HDFS directory:
hdfs dfs -mkdir -p /pig_output

Upload:
hdfs dfs -put ~/pig_lab/data_top.txt /pig_output/

Verify:
hdfs dfs -ls /pig_output
hdfs dfs -cat /pig_output/data_top.txt

6. PART 2 – BASIC PIG LATIN QUERIES
-----------------------------------
Create sales dataset in Ubuntu Terminal:
cd ~/pig_lab
nano sales.csv

Enter:
Maharashtra,1000
Gujarat,1500
Karnataka,2000
Maharashtra,2500
Gujarat,3000

Save and open Pig:
pig -x local

At grunt> (replace USERNAME):
sales = LOAD '/home/USERNAME/pig_lab/sales.csv' USING PigStorage(',') AS (state:chararray, amount:int);

Describe:
DESCRIBE sales;

Filter amount greater than 1500:
high_sales = FILTER sales BY amount > 1500;
DUMP high_sales;

Group by state:
grouped = GROUP sales BY state;
DUMP grouped;

Count orders state-wise:
counts = FOREACH grouped GENERATE group AS state, COUNT(sales) AS total_orders;
DUMP counts;

Calculate total sales state-wise:
totals = FOREACH grouped GENERATE group AS state, SUM(sales.amount) AS total_sales;
DUMP totals;

Calculate average order amount:
average = FOREACH grouped GENERATE group AS state, AVG(sales.amount) AS avg_amount;
DUMP average;

Store results:
STORE totals INTO '/home/USERNAME/pig_lab/sales_output' USING PigStorage(',');

7. IMPORTANT PIG COMMANDS
-------------------------
LOAD – load data
DUMP – display output
DESCRIBE – display schema
GROUP – group records
FILTER – select matching records
FOREACH – process records/groups
GENERATE – select or calculate fields
COUNT – count records
SUM – calculate total
AVG – calculate average
ORDER – sort
LIMIT – restrict number of records
STORE – save output
""")
