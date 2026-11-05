print("""
MONGODB PRACTICAL – CRUD OPERATIONS
===================================

1. CHECK INSTALLATION (Ubuntu Terminal)
---------------------------------------
sudo systemctl status mongod
mongod --version
mongosh --version

If installed but stopped:
sudo systemctl start mongod

2. OPEN MONGODB
---------------
mongosh

Everything below is typed inside the mongosh prompt, NOT Ubuntu Terminal.

3. CREATE DATABASE AND COLLECTION
----------------------------------
show dbs
use college
db.createCollection("students")
show collections

4. INSERT RECORDS
-----------------
Insert one:
db.students.insertOne({roll: 1, name: "Liston", department: "Computer", year: 4, email: "liston@gmail.com", marks: 85, status: "Active"})

Insert multiple:
db.students.insertMany([
  {roll: 2, name: "John", department: "IT", year: 3, marks: 75, status: "Active"},
  {roll: 3, name: "David", department: "Computer", year: 4, marks: 90, status: "Active"},
  {roll: 4, name: "Sam", department: "Computer", year: 3, marks: 65, status: "Inactive"}
])

5. DISPLAY AND SEARCH
---------------------
db.students.find()
db.students.find().pretty()
db.students.find({name: "Liston"})
db.students.find({roll: 2})
db.students.find({marks: {$gt: 80}})
db.students.find({marks: {$lt: 80}})
db.students.find({marks: {$gte: 80}})

6. UPDATE
---------
Update one:
db.students.updateOne({roll: 1}, {$set: {marks: 95}})
db.students.find({roll: 1})

Update many:
db.students.updateMany({department: "Computer"}, {$set: {status: "Verified"}})

7. DELETE
---------
db.students.deleteOne({roll: 4})
db.students.deleteMany({status: "Inactive"})

8. COUNT AND DATABASE INFORMATION
----------------------------------
db.students.countDocuments()
db.stats()
show dbs
show collections

9. EXIT
-------
exit

QUICK COMMAND REMINDER
----------------------
Create/select database: use college
Create collection: db.createCollection("students")
Insert one/many: insertOne(), insertMany()
Read/search: find()
Update: updateOne(), updateMany()
Delete: deleteOne(), deleteMany()
Count: countDocuments()
""")
