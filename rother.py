print("""
R PRACTICAL – DATASET ANALYSIS AND MANIPULATION COMMANDS
========================================================

1. CHECK AND OPEN R (Ubuntu Terminal)
-------------------------------------
R --version
R

If R is not installed:
sudo apt update
sudo apt install r-base -y

2. CREATE THE SAMPLE DATASET (inside R)
---------------------------------------
student <- data.frame(
  Student_ID = 1:15,
  Gender = c("Male","Female","Male","Female","Male","Female","Male","Female","Male","Female","Male","Female","Male","Female","Male"),
  Study_Hours = c(2,4,3,5,1,3,4,2,5,4,3,5,2,3,4),
  Attendance = c(72,85,80,92,65,78,88,70,95,86,76,94,68,82,89),
  Assignment_Score = c(65,78,72,88,55,75,82,68,91,85,70,90,60,77,84),
  Internal_Marks = c(60,82,70,90,52,73,80,64,92,84,68,91,58,75,81),
  Final_Marks = c(62,84,73,91,50,76,83,65,94,86,71,93,59,78,85)
)

3. FIVE DATASET ANALYSIS COMMANDS
---------------------------------
1) Display complete dataset:
print(student)

2) Display dataset structure (column names and data types):
str(student)

3) Display summary statistics:
summary(student)

4) Display first six records:
head(student)

5) Count male and female students:
table(student$Gender)

4. ADDITIONAL USEFUL COMMANDS
-----------------------------
Number of rows:
nrow(student)

Number of columns:
ncol(student)

Column names:
names(student)

Students scoring more than 80:
student[student$Final_Marks > 80, ]

Average attendance:
mean(student$Attendance)

5. EXIT R
---------
q()

If asked whether to save the workspace, type:
n

IMPORTANT: These commands are typed inside R, not directly in Ubuntu Terminal.
""")
