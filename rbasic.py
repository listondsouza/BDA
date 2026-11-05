print("""
R PRACTICAL – BASIC MATHEMATICAL AND STATISTICAL COMMANDS
=========================================================

1. CHECK AND OPEN R (Ubuntu Terminal)
-------------------------------------
R --version
    -> Checks installed R version.

R
    -> Opens R console.

If R is not installed:
sudo apt update
sudo apt install r-base -y

IMPORTANT:
Commands below are typed inside R, not Ubuntu Terminal.
R prompt looks like: >


2. CREATE THE SAMPLE DATASET
----------------------------
student <- data.frame(
  Student_ID = 1:15,
  Gender = c("Male","Female","Male","Female","Male","Female","Male","Female","Male","Female","Male","Female","Male","Female","Male"),
  Study_Hours = c(2,4,3,5,1,3,4,2,5,4,3,5,2,3,4),
  Attendance = c(72,85,80,92,65,78,88,70,95,86,76,94,68,82,89),
  Assignment_Score = c(65,78,72,88,55,75,82,68,91,85,70,90,60,77,84),
  Internal_Marks = c(60,82,70,90,52,73,80,64,92,84,68,91,58,75,81),
  Final_Marks = c(62,84,73,91,50,76,83,65,94,86,71,93,59,78,85)
)
    -> Creates a student dataset with 15 records.


3. BASIC MATHEMATICAL COMMANDS
------------------------------
10 + 20
    -> Addition.

20 - 10
    -> Subtraction.

10 * 5
    -> Multiplication.

20 / 4
    -> Division.

10 %% 3
    -> Remainder (modulus).

10 %/% 3
    -> Integer division.

2 ^ 3
    -> Power (2 raised to 3).

sqrt(25)
    -> Square root.

abs(-15)
    -> Absolute value (removes negative sign).

round(12.567, 2)
    -> Rounds value to 2 decimal places.

ceiling(12.3)
    -> Rounds UP to the next integer.

floor(12.9)
    -> Rounds DOWN to the previous integer.


4. FIVE BASIC STATISTICAL COMMANDS
----------------------------------
mean(student$Final_Marks)
    -> Calculates AVERAGE marks.

median(student$Final_Marks)
    -> Calculates MIDDLE value after sorting.

sd(student$Final_Marks)
    -> Calculates STANDARD DEVIATION (spread of values).

min(student$Final_Marks)
    -> Finds the LOWEST marks.

max(student$Final_Marks)
    -> Finds the HIGHEST marks.

var(student$Final_Marks)
    -> Calculates variance (squared spread of values).

sum(student$Final_Marks)
    -> Calculates total marks.

length(student$Final_Marks)
    -> Counts the number of values.

range(student$Final_Marks)
    -> Displays minimum and maximum values.

summary(student$Final_Marks)
    -> Displays minimum, 1st quartile, median, mean,
       3rd quartile and maximum.


5. OTHER STATISTICAL FUNCTIONS
------------------------------
quantile(student$Final_Marks)
    -> Calculates quartiles (0%, 25%, 50%, 75%, 100%).

IQR(student$Final_Marks)
    -> Calculates interquartile range (Q3 - Q1).

which.max(student$Final_Marks)
    -> Gives the position of the highest marks.

which.min(student$Final_Marks)
    -> Gives the position of the lowest marks.

sort(student$Final_Marks)
    -> Sorts marks in ascending order.

sort(student$Final_Marks, decreasing = TRUE)
    -> Sorts marks in descending order.


6. DATASET INFORMATION
----------------------
student
    -> Displays the complete dataset.

head(student)
    -> Displays first 6 records.

head(student, 10)
    -> Displays first 10 records.

tail(student)
    -> Displays last 6 records.

str(student)
    -> Displays dataset structure and data types.

dim(student)
    -> Displays number of rows and columns.

nrow(student)
    -> Displays number of rows.

ncol(student)
    -> Displays number of columns.

names(student)
    -> Displays column names.

colnames(student)
    -> Displays column names.

class(student)
    -> Displays the object's class.

summary(student)
    -> Displays statistical summary of all columns.


7. ACCESSING DATA
-----------------
student$Final_Marks
    -> Displays only Final_Marks column.

student$Gender
    -> Displays only Gender column.

student[1, ]
    -> Displays first row.

student[1:5, ]
    -> Displays first 5 rows.

student[, "Final_Marks"]
    -> Displays Final_Marks column.

student[1:5, c("Gender", "Final_Marks")]
    -> Displays selected rows and columns.


8. FILTERING DATA
-----------------
subset(student, Final_Marks > 80)
    -> Displays students scoring MORE THAN 80.

subset(student, Final_Marks < 80)
    -> Displays students scoring LESS THAN 80.

subset(student, Final_Marks >= 80)
    -> Displays students scoring 80 OR MORE.

subset(student, Final_Marks <= 80)
    -> Displays students scoring 80 OR LESS.

subset(student, Gender == "Female")
    -> Displays only female students.

subset(student, Gender == "Male")
    -> Displays only male students.

subset(student, Attendance > 80 & Final_Marks > 80)
    -> Displays students with attendance AND final marks
       greater than 80.

subset(student, Gender == "Female" | Final_Marks > 85)
    -> Displays female students OR students scoring
       more than 85.


9. COUNTING AND FREQUENCY
-------------------------
table(student$Gender)
    -> Counts male and female students.

table(student$Gender, student$Final_Marks > 80)
    -> Creates a frequency table by gender and marks condition.

unique(student$Gender)
    -> Displays unique gender values.

length(unique(student$Gender))
    -> Counts the number of unique gender values.


10. SORTING DATA
----------------
student[order(student$Final_Marks), ]
    -> Sorts complete dataset by marks ASCENDING.

student[order(-student$Final_Marks), ]
    -> Sorts complete dataset by marks DESCENDING.

student[order(student$Attendance), ]
    -> Sorts students by attendance in ascending order.


11. COLUMN-WISE STATISTICS
--------------------------
mean(student$Attendance)
    -> Calculates average attendance.

mean(student$Study_Hours)
    -> Calculates average study hours.

mean(student$Assignment_Score)
    -> Calculates average assignment score.

max(student$Attendance)
    -> Finds highest attendance.

min(student$Study_Hours)
    -> Finds lowest study hours.

sd(student$Internal_Marks)
    -> Calculates standard deviation of internal marks.


12. APPLY FUNCTIONS
-------------------
colMeans(student[c("Study_Hours", "Attendance", "Final_Marks")])
    -> Calculates mean of selected numeric columns.

sapply(student[c("Study_Hours", "Attendance", "Final_Marks")], mean)
    -> Applies mean function to each selected column.

sapply(student[c("Study_Hours", "Attendance", "Final_Marks")], sd)
    -> Calculates standard deviation of each selected column.

lapply(student[c("Study_Hours", "Attendance", "Final_Marks")], max)
    -> Finds maximum value in each selected column.


13. ADDING AND MODIFYING COLUMNS
--------------------------------
student$Result <- ifelse(student$Final_Marks >= 40, "Pass", "Fail")
    -> Creates a new Result column based on marks.

student$Bonus_Marks <- student$Final_Marks + 5
    -> Creates a new column by adding 5 marks.

student$Percentage <- student$Final_Marks
    -> Creates a Percentage column using final marks.

student$Final_Marks[1] <- 95
    -> Changes the first student's final marks to 95.


14. MISSING VALUE COMMANDS
--------------------------
is.na(student)
    -> Checks for missing values.

colSums(is.na(student))
    -> Counts missing values in each column.

sum(is.na(student))
    -> Counts total missing values.

na.omit(student)
    -> Removes rows containing missing values.

mean(student$Final_Marks, na.rm = TRUE)
    -> Calculates mean while ignoring missing values.


15. EXIT R
----------
q()
    -> Exits R console.

If asked whether to save workspace:
Type n
    -> Exits without saving workspace.


QUICK COMMAND REMINDER
----------------------
ADDITION              -> +
SUBTRACTION           -> -
MULTIPLICATION        -> *
DIVISION              -> /
REMAINDER             -> %%
POWER                 -> ^
SQUARE ROOT           -> sqrt()
ROUND                 -> round()

AVERAGE               -> mean()
MEDIAN                -> median()
STANDARD DEVIATION    -> sd()
VARIANCE              -> var()
MINIMUM               -> min()
MAXIMUM               -> max()
TOTAL                 -> sum()
COUNT VALUES          -> length()
QUARTILES             -> quantile()
SUMMARY               -> summary()

FIRST 6 ROWS          -> head()
LAST 6 ROWS           -> tail()
DATA STRUCTURE        -> str()
ROWS AND COLUMNS      -> dim()
NUMBER OF ROWS        -> nrow()
NUMBER OF COLUMNS     -> ncol()
COLUMN NAMES          -> names()
FILTER                -> subset()
FREQUENCY             -> table()
UNIQUE VALUES         -> unique()
SORT ASCENDING        -> order()
APPLY FUNCTION        -> sapply()
MISSING VALUES        -> is.na()
REMOVE MISSING ROWS   -> na.omit()

IMPORTANT:
Use $ to access a particular column.
Example: student$Final_Marks

Use <- to assign or store a value.
Example: average <- mean(student$Final_Marks)

Use # to write comments in R.
""")
