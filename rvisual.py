print("""
R PRACTICAL – FIVE VISUALIZATION COMMANDS
=========================================

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

3. FIVE VISUALIZATION COMMANDS
------------------------------
Optional single-plot layout:
par(mfrow = c(1,1))

1) BAR CHART – Gender distribution:
barplot(
  table(student$Gender),
  main = "Gender Distribution",
  xlab = "Gender",
  ylab = "Number of Students"
)

2) HISTOGRAM – Final marks distribution:
hist(
  student$Final_Marks,
  main = "Final Marks Distribution",
  xlab = "Final Marks",
  col = "skyblue"
)

3) SCATTER PLOT – Study hours vs final marks:
plot(
  student$Study_Hours,
  student$Final_Marks,
  main = "Study Hours vs Final Marks",
  xlab = "Study Hours",
  ylab = "Final Marks",
  pch = 19
)

4) PIE CHART – Gender distribution:
pie(
  table(student$Gender),
  main = "Gender Distribution"
)

5) BOX PLOT – Final marks:
boxplot(
  student$Final_Marks,
  main = "Final Marks Boxplot",
  ylab = "Marks"
)

4. EXIT R
---------
q()

If asked whether to save the workspace, type:
n

IMPORTANT: These commands are typed inside R, not directly in Ubuntu Terminal.
""")
