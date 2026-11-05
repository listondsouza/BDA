print("""
R PRACTICAL – BASIC MATHEMATICAL AND STATISTICAL COMMANDS
=========================================================

1. CHECK AND OPEN R (Ubuntu Terminal)
-------------------------------------
R --version
R

If R is not installed:
sudo apt update
sudo apt install r-base -y

The R prompt looks like: >

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

3. FIVE BASIC COMMANDS
----------------------
Addition:
10 + 20

Mean / average:
mean(student$Final_Marks)

Median:
median(student$Final_Marks)

Standard deviation:
sd(student$Final_Marks)

Minimum and maximum:
min(student$Final_Marks)
max(student$Final_Marks)

4. OTHER USEFUL MATHEMATICAL COMMANDS
-------------------------------------
sum(student$Final_Marks)
length(student$Final_Marks)
sqrt(25)
round(mean(student$Final_Marks), 2)

5. EXIT R
---------
q()

If asked whether to save the workspace, type:
n

IMPORTANT: These commands are typed inside R, not directly in Ubuntu Terminal.
""")
