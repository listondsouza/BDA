print("""
R PRACTICAL – FIVE VISUALIZATION COMMANDS
=========================================

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
All commands below are typed inside R, not Ubuntu Terminal.


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
    -> Creates a dataset of 15 students.


3. FIVE MAIN VISUALIZATION COMMANDS
-----------------------------------

1) BAR CHART – Gender Distribution
----------------------------------
barplot(
  table(student$Gender),
  main = "Gender Distribution",
  xlab = "Gender",
  ylab = "Number of Students",
  col = "skyblue"
)
    -> Displays the number of Male and Female students.

table(student$Gender)
    -> Counts students in each gender category.

barplot(table(student$Gender), col = "red")
    -> Creates a simple red bar chart.


2) HISTOGRAM – Final Marks Distribution
---------------------------------------
hist(
  student$Final_Marks,
  main = "Final Marks Distribution",
  xlab = "Final Marks",
  ylab = "Frequency",
  col = "skyblue",
  border = "black"
)
    -> Displays the frequency distribution of final marks.
    -> Shows how marks are spread across intervals.

hist(student$Final_Marks, breaks = 5)
    -> Divides marks into approximately 5 intervals.


3) SCATTER PLOT – Study Hours vs Final Marks
--------------------------------------------
plot(
  student$Study_Hours,
  student$Final_Marks,
  main = "Study Hours vs Final Marks",
  xlab = "Study Hours",
  ylab = "Final Marks",
  pch = 19,
  col = "blue"
)
    -> Shows the relationship between study hours and final marks.
    -> Each dot represents one student.

pch = 19
    -> Uses solid circular points.

plot(student$Attendance, student$Final_Marks)
    -> Shows relationship between attendance and final marks.


4) PIE CHART – Gender Distribution
----------------------------------
pie(
  table(student$Gender),
  main = "Gender Distribution",
  col = c("pink", "skyblue")
)
    -> Displays gender distribution as portions of a circle.
    -> Shows the proportion of each category.

pie(table(student$Gender))
    -> Creates a simple pie chart.


5) BOX PLOT – Final Marks
-------------------------
boxplot(
  student$Final_Marks,
  main = "Final Marks Boxplot",
  ylab = "Marks",
  col = "lightgreen"
)
    -> Displays the distribution of marks using:
       Minimum, Q1, Median, Q3 and Maximum.
    -> Also helps identify possible outliers.

boxplot(student$Attendance)
    -> Displays attendance distribution.


4. ADDITIONAL USEFUL VISUALIZATION COMMANDS
-------------------------------------------

6) LINE GRAPH
-------------
plot(
  student$Student_ID,
  student$Final_Marks,
  type = "l",
  main = "Student Marks Line Graph",
  xlab = "Student ID",
  ylab = "Final Marks",
  col = "blue"
)
    -> Displays changes in marks across student IDs.
    -> type = "l" means line graph.


7) DENSITY PLOT
---------------
plot(
  density(student$Final_Marks),
  main = "Density Plot of Final Marks",
  xlab = "Final Marks",
  col = "red"
)
    -> Displays a smooth representation of data distribution.


8) MULTIPLE HISTOGRAMS
----------------------
hist(student$Attendance, col = "orange",
     main = "Attendance Distribution",
     xlab = "Attendance")
    -> Displays attendance frequency distribution.


5. GRAPH CUSTOMIZATION COMMANDS
-------------------------------

main = "Title"
    -> Sets graph title.

xlab = "X Axis"
    -> Sets X-axis label.

ylab = "Y Axis"
    -> Sets Y-axis label.

col = "red"
    -> Changes graph colour.

border = "black"
    -> Changes histogram/bar borders.

pch = 19
    -> Changes scatter plot point style.

type = "l"
    -> Displays a line graph.

type = "p"
    -> Displays points only.

type = "b"
    -> Displays both points and lines.

cex = 1.5
    -> Changes point or text size.

las = 1
    -> Makes axis labels horizontal.


6. DISPLAY MULTIPLE GRAPHS
--------------------------
par(mfrow = c(2,2))
    -> Divides plotting area into 2 rows and 2 columns.

par(mfrow = c(1,2))
    -> Displays 2 graphs side by side.

par(mfrow = c(1,1))
    -> Returns to a single graph layout.


7. SAVE GRAPH AS IMAGE
----------------------
png("student_graph.png")
    -> Starts saving graph as a PNG image.

barplot(table(student$Gender))
    -> Draws the graph.

dev.off()
    -> Closes the graphics device and saves the image.


8. EXIT R
---------
q()
    -> Exits R console.

If asked whether to save workspace:
Type n.


QUICK COMMAND REMINDER
----------------------
BAR CHART       -> barplot()
HISTOGRAM       -> hist()
SCATTER PLOT    -> plot(x, y)
PIE CHART       -> pie()
BOX PLOT        -> boxplot()
LINE GRAPH      -> plot(x, y, type = "l")
DENSITY PLOT    -> density()

COUNT DATA      -> table()
GRAPH TITLE     -> main
X AXIS LABEL    -> xlab
Y AXIS LABEL    -> ylab
GRAPH COLOUR    -> col
POINT STYLE     -> pch
LINE TYPE       -> type
MULTIPLE GRAPHS -> par(mfrow = c(2,2))
SAVE GRAPH      -> png()
CLOSE GRAPH     -> dev.off()

IMPORTANT:
1. barplot() is mainly used for categorical data.
2. hist() is used for numerical data distribution.
3. plot(x,y) is used to show the relationship between
   two numerical variables.
4. pie() shows proportions.
5. boxplot() shows spread, median and possible outliers.
""")
