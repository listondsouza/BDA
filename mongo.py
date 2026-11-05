print("""
MONGODB PRACTICAL – CRUD OPERATIONS
===================================

1. CHECK INSTALLATION (Ubuntu Terminal)
---------------------------------------
sudo systemctl status mongod
    -> Checks whether MongoDB service is running.

mongod --version
    -> Displays MongoDB server version.

mongosh --version
    -> Displays MongoDB Shell version.

If installed but stopped:
sudo systemctl start mongod
    -> Starts MongoDB service.


2. OPEN MONGODB
---------------
mongosh
    -> Opens MongoDB Shell.

IMPORTANT:
Everything below is typed inside mongosh, NOT Ubuntu Terminal.


3. CREATE DATABASE AND COLLECTION
----------------------------------
show dbs
    -> Displays all databases.

use college
    -> Creates or switches to the college database.

db
    -> Displays the currently selected database.

db.createCollection("students")
    -> Creates a collection named students.

show collections
    -> Displays all collections in the current database.


4. INSERT RECORDS
-----------------
Insert one record:
db.students.insertOne({
    roll: 1,
    name: "Liston",
    department: "Computer",
    year: 4,
    email: "liston@gmail.com",
    marks: 85,
    status: "Active"
})
    -> Inserts one student record.

Insert multiple records:
db.students.insertMany([
    {roll: 2, name: "John", department: "IT", year: 3, marks: 75, status: "Active"},
    {roll: 3, name: "David", department: "Computer", year: 4, marks: 90, status: "Active"},
    {roll: 4, name: "Sam", department: "Computer", year: 3, marks: 65, status: "Inactive"},
    {roll: 5, name: "Alex", department: "IT", year: 4, marks: 80, status: "Active"}
])
    -> Inserts multiple student records at once.


5. DISPLAY AND SEARCH (READ)
----------------------------
db.students.find()
    -> Displays all student records.

db.students.find().pretty()
    -> Displays records in formatted/readable form.

db.students.findOne()
    -> Displays only the first matching record.

db.students.find({name: "Liston"})
    -> Searches for a student whose name is Liston.

db.students.find({roll: 2})
    -> Searches for a student with roll number 2.

db.students.find({department: "Computer"})
    -> Displays students from Computer department.

db.students.find({status: "Active"})
    -> Displays students with Active status.


6. COMPARISON OPERATORS
----------------------
db.students.find({marks: {$gt: 80}})
    -> Finds students scoring MORE THAN 80.

db.students.find({marks: {$lt: 80}})
    -> Finds students scoring LESS THAN 80.

db.students.find({marks: {$gte: 80}})
    -> Finds students scoring 80 OR MORE.

db.students.find({marks: {$lte: 80}})
    -> Finds students scoring 80 OR LESS.

db.students.find({marks: {$eq: 80}})
    -> Finds students scoring EXACTLY 80.

db.students.find({marks: {$ne: 80}})
    -> Finds students whose marks are NOT 80.

db.students.find({marks: {$in: [75, 85, 90]}})
    -> Finds students scoring 75 OR 85 OR 90.

db.students.find({marks: {$nin: [75, 85]}})
    -> Finds students whose marks are NOT 75 or 85.

REMEMBER:
$gt  = Greater Than
$lt  = Less Than
$gte = Greater Than or Equal To
$lte = Less Than or Equal To
$eq  = Equal To
$ne  = Not Equal To
$in  = Matches any value in the list
$nin = Does not match any value in the list


7. LOGICAL OPERATORS
-------------------
db.students.find({$and: [{marks: {$gt: 70}}, {department: "Computer"}]})
    -> Finds Computer students scoring MORE THAN 70.

db.students.find({$or: [{department: "IT"}, {marks: {$gt: 85}}]})
    -> Finds IT students OR students scoring more than 85.

db.students.find({$nor: [{status: "Inactive"}, {marks: {$lt: 40}}]})
    -> Finds records that match NEITHER condition.

db.students.find({marks: {$not: {$gt: 80}}})
    -> Finds students whose marks are NOT greater than 80.


8. DISPLAY SELECTED FIELDS (PROJECTION)
--------------------------------------
db.students.find({}, {name: 1, marks: 1})
    -> Displays only name and marks.

db.students.find({}, {_id: 0, name: 1, marks: 1})
    -> Displays name and marks without the _id field.

db.students.find({}, {email: 0})
    -> Displays all fields except email.


9. SORTING AND LIMITING
-----------------------
db.students.find().sort({marks: 1})
    -> Sorts marks in ASCENDING order (lowest to highest).

db.students.find().sort({marks: -1})
    -> Sorts marks in DESCENDING order (highest to lowest).

db.students.find().limit(3)
    -> Displays only the first 3 records.

db.students.find().skip(2)
    -> Skips the first 2 records.

db.students.find().sort({marks: -1}).limit(1)
    -> Displays the student with the highest marks.


10. UPDATE
----------
Update one:
db.students.updateOne({roll: 1}, {$set: {marks: 95}})
    -> Updates marks to 95 for the student with roll number 1.

Update many:
db.students.updateMany({department: "Computer"}, {$set: {status: "Verified"}})
    -> Updates status to Verified for all Computer students.

Increase marks:
db.students.updateOne({roll: 2}, {$inc: {marks: 5}})
    -> Increases marks by 5.

Decrease marks:
db.students.updateOne({roll: 2}, {$inc: {marks: -5}})
    -> Decreases marks by 5.

Add a new field:
db.students.updateOne({roll: 1}, {$set: {city: "Mumbai"}})
    -> Adds or updates the city field.

Remove a field:
db.students.updateOne({roll: 1}, {$unset: {city: ""}})
    -> Removes the city field.

Rename a field:
db.students.updateOne({roll: 1}, {$rename: {department: "branch"}})
    -> Renames department field to branch.

Check updated record:
db.students.find({roll: 1})
    -> Displays the updated student record.


11. DELETE
----------
db.students.deleteOne({roll: 4})
    -> Deletes one student with roll number 4.

db.students.deleteMany({status: "Inactive"})
    -> Deletes all students with Inactive status.

db.students.deleteMany({marks: {$lt: 40}})
    -> Deletes all students scoring less than 40.

db.students.deleteMany({})
    -> Deletes ALL records in the collection. Use carefully!


12. COUNT AND BASIC STATISTICS
------------------------------
db.students.countDocuments()
    -> Counts all student records.

db.students.countDocuments({department: "Computer"})
    -> Counts Computer department students.

db.students.countDocuments({marks: {$gt: 80}})
    -> Counts students scoring more than 80.

db.students.distinct("department")
    -> Displays unique department names.

db.students.distinct("status")
    -> Displays unique student statuses.


13. AGGREGATION – AVERAGE, SUM, MAX, MIN
---------------------------------------
Average marks:
db.students.aggregate([
    {$group: {_id: null, averageMarks: {$avg: "$marks"}}}
])
    -> Calculates the average marks of all students.

Total marks:
db.students.aggregate([
    {$group: {_id: null, totalMarks: {$sum: "$marks"}}}
])
    -> Calculates the sum of all marks.

Maximum marks:
db.students.aggregate([
    {$group: {_id: null, highestMarks: {$max: "$marks"}}}
])
    -> Finds the highest marks.

Minimum marks:
db.students.aggregate([
    {$group: {_id: null, lowestMarks: {$min: "$marks"}}}
])
    -> Finds the lowest marks.

Number of students:
db.students.aggregate([
    {$group: {_id: null, totalStudents: {$sum: 1}}}
])
    -> Counts the number of student records.

Average marks department-wise:
db.students.aggregate([
    {$group: {_id: "$department", averageMarks: {$avg: "$marks"}}}
])
    -> Calculates average marks separately for each department.

Count students department-wise:
db.students.aggregate([
    {$group: {_id: "$department", totalStudents: {$sum: 1}}}
])
    -> Counts students in each department.

Sort department-wise averages:
db.students.aggregate([
    {$group: {_id: "$department", averageMarks: {$avg: "$marks"}}},
    {$sort: {averageMarks: -1}}
])
    -> Displays departments from highest average to lowest.


14. AGGREGATION – MATCH, GROUP, SORT
------------------------------------
db.students.aggregate([
    {$match: {marks: {$gt: 70}}}
])
    -> Filters students scoring more than 70.

db.students.aggregate([
    {$match: {department: "Computer"}},
    {$group: {_id: "$department", averageMarks: {$avg: "$marks"}}}
])
    -> Calculates average marks of Computer students only.

db.students.aggregate([
    {$group: {_id: "$department", total: {$sum: 1}}},
    {$sort: {total: -1}}
])
    -> Counts students department-wise and sorts by count.


15. DATABASE INFORMATION
------------------------
db.stats()
    -> Displays statistics of the current database.

db.students.stats()
    -> Displays statistics of the students collection.

db.getName()
    -> Displays the current database name.

show dbs
    -> Displays all databases.

show collections
    -> Displays all collections.


16. DROP DATABASE AND COLLECTION
-------------------------------
db.students.drop()
    -> Deletes the entire students collection.

db.dropDatabase()
    -> Deletes the currently selected database.
       USE CAREFULLY!


17. EXIT
--------
exit
    -> Exits MongoDB Shell and returns to Ubuntu Terminal.


QUICK COMMAND REMINDER
----------------------
CREATE DATABASE       -> use college
CREATE COLLECTION     -> db.createCollection("students")
INSERT ONE            -> insertOne()
INSERT MANY           -> insertMany()
DISPLAY ALL           -> find()
SEARCH                -> find({condition})
GREATER THAN          -> $gt
LESS THAN             -> $lt
GREATER/EQUAL         -> $gte
LESS/EQUAL            -> $lte
NOT EQUAL             -> $ne
AND                   -> $and
OR                    -> $or
ASCENDING SORT        -> sort({marks: 1})
DESCENDING SORT       -> sort({marks: -1})
LIMIT                 -> limit()
SKIP                  -> skip()
UPDATE ONE            -> updateOne()
UPDATE MANY           -> updateMany()
INCREASE VALUE        -> $inc
ADD/CHANGE FIELD      -> $set
REMOVE FIELD          -> $unset
DELETE ONE            -> deleteOne()
DELETE MANY           -> deleteMany()
COUNT                 -> countDocuments()
UNIQUE VALUES         -> distinct()
AVERAGE               -> $avg
TOTAL/SUM             -> $sum
MAXIMUM               -> $max
MINIMUM               -> $min
FILTER AGGREGATION    -> $match
GROUP AGGREGATION     -> $group
EXIT                  -> exit

IMPORTANT:
$avg, $sum, $max and $min are aggregation operators.
Use them inside db.students.aggregate([...]).
""")
