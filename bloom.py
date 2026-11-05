print("""
PYTHON PRACTICAL – BLOOM FILTER
(STUDENT VALUE PRESENCE CHECKER)
=================================

AIM:
To implement a simple Bloom Filter using a bit array
and two hash functions to check whether a value is
possibly present or definitely not present.


================================================
1. CHECK REQUIREMENTS (UBUNTU TERMINAL)
================================================

Open Ubuntu Terminal:
Ctrl + Alt + T

Check Python:
python3 --version

-> Checks whether Python 3 is installed.

Check pip:
pip3 --version

-> Checks whether Python package manager is installed.

Check hashlib:
python3 -c "import hashlib; print('Available')"

-> Checks whether hashlib is available.
-> Not required for this new program, because we
   are using simple mathematical hash functions.

IMPORTANT:
No external Python library is required.
The program uses only built-in Python functionality.


================================================
2. CREATE AND OPEN PROJECT FOLDER
================================================

Go to home directory:
cd ~

-> Moves to the home directory.

Create folder:
mkdir -p bloom

-> Creates a folder named bloom.

Open folder:
cd ~/bloom

-> Enters the bloom folder.

Check location:
pwd

-> Displays current directory.

Check files:
ls

-> Displays files inside the folder.


================================================
3. CREATE PYTHON FILE
================================================

Run:
nano bloom.py

-> Opens the nano text editor.
-> We will write our Python program here.

TYPE THE FOLLOWING CODE:


# Simple Bloom Filter a=12, b=23, c=21

# Step 1: Create an array of 10 zeros
bit_array = [0] * 10

# Step 2: Two simple hash functions
def hash1(x):
    return x % 10

def hash2(x):
    return (x // 10) % 10

# Step 3: Insert two values
a = int(input("Enter first value (12): "))
b = int(input("Enter second value (23): "))

# Insert A
bit_array[hash1(a)] = 1
bit_array[hash2(a)] = 1

# Insert B
bit_array[hash1(b)] = 1
bit_array[hash2(b)] = 1

# Step 4: Display updated array
print("\\nUpdated Bit Array:")
print(bit_array)

# Step 5: Search values continuously
while True:
    x = input("\\nEnter value to search (or q to quit): ")

    if x.lower() == "q":
        break

    x = int(x)

    # Check both hash positions
    if bit_array[hash1(x)] == 1 and bit_array[hash2(x)] == 1:
        print("Possibly Present")
    else:
        print("Definitely Not Present")


================================================
4. SAVE THE PYTHON FILE
================================================

In nano:

1. Press Ctrl + O.
2. Press Enter.
3. Press Ctrl + X.

-> Saves the file and exits the editor.

Check file:
ls

Expected:
bloom.py

Display code:
cat bloom.py

-> Displays the saved Python program.


================================================
5. RUN THE PROGRAM
================================================

Run:
python3 bloom.py

-> Executes the Bloom Filter program.

Enter first value:
12

Enter second value:
23

The program inserts both values into the bit array.


================================================
6. UNDERSTAND THE TWO HASH FUNCTIONS
================================================

HASH FUNCTION 1:

def hash1(x):
    return x % 10

-> Returns the last digit/remainder after division by 10.

Examples:

hash1(12) = 12 % 10 = 2
hash1(23) = 23 % 10 = 3
hash1(21) = 21 % 10 = 1


HASH FUNCTION 2:

def hash2(x):
    return (x // 10) % 10

-> First performs integer division by 10.
-> Then calculates remainder after division by 10.

Examples:

hash2(12) = (12 // 10) % 10
          = 1 % 10
          = 1

hash2(23) = (23 // 10) % 10
          = 2 % 10
          = 2

hash2(21) = (21 // 10) % 10
          = 2 % 10
          = 2


================================================
7. UNDERSTAND INSERTION
================================================

Initially:

bit_array = [0,0,0,0,0,0,0,0,0,0]

Insert first value A = 12:

hash1(12) = 2
hash2(12) = 1

Set positions 2 and 1 to 1.

Array becomes:

[0,1,1,0,0,0,0,0,0,0]


Insert second value B = 23:

hash1(23) = 3
hash2(23) = 2

Set positions 3 and 2 to 1.

Array becomes:

[0,1,1,1,0,0,0,0,0,0]

IMPORTANT:
If a position is already 1, it remains 1.


================================================
8. UNDERSTAND SEARCHING
================================================

Suppose we search for 12.

hash1(12) = 2
hash2(12) = 1

Check:
bit_array[2] = 1
bit_array[1] = 1

Both positions are 1.

Output:
Possibly Present


Suppose we search for 21.

hash1(21) = 1
hash2(21) = 2

Check:
bit_array[1] = 1
bit_array[2] = 1

Both positions are 1.

Output:
Possibly Present

IMPORTANT:
21 was never inserted!
This is an example of a FALSE POSITIVE.

The Bloom Filter says possibly present, but the value
is actually absent.


Suppose we search for 45.

hash1(45) = 5
hash2(45) = 4

Check:
bit_array[5] = 0
bit_array[4] = 0

At least one position is 0.

Output:
Definitely Not Present


================================================
9. SAMPLE EXECUTION
================================================

Run:
python3 bloom.py

INPUT:

Enter first value (12): 12
Enter second value (23): 23

OUTPUT:

Updated Bit Array:
[0, 1, 1, 1, 0, 0, 0, 0, 0, 0]

Enter value to search (or q to quit): 12
Possibly Present

Enter value to search (or q to quit): 23
Possibly Present

Enter value to search (or q to quit): 21
Possibly Present

Enter value to search (or q to quit): 45
Definitely Not Present

Enter value to search (or q to quit): q

-> q terminates the search loop.


================================================
10. EXPLANATION OF PYTHON COMMANDS
================================================

bit_array = [0] * 10
-> Creates a list containing 10 zeros.

def hash1(x):
-> Defines the first hash function.

x % 10
-> Returns remainder after division by 10.

x // 10
-> Performs integer division.

def hash2(x):
-> Defines the second hash function.

int(input())
-> Accepts user input and converts it into an integer.

bit_array[index] = 1
-> Changes the specified array position to 1.

while True:
-> Repeats the search process continuously.

input()
-> Accepts a value from the user.

x.lower()
-> Converts input into lowercase.

break
-> Exits the loop.

and
-> Checks whether both conditions are true.

if
-> Executes code when a condition is true.

else
-> Executes code when the condition is false.

print()
-> Displays output.


================================================
11. COMMON COMMANDS FOR UBUNTU
================================================

CHECK PYTHON:
python3 --version

CREATE FOLDER:
mkdir -p bloom

OPEN FOLDER:
cd ~/bloom

CREATE FILE:
nano bloom.py

DISPLAY FILE:
cat bloom.py

RUN PROGRAM:
python3 bloom.py

CLEAR TERMINAL:
clear

GO BACK:
cd ..

GO HOME:
cd ~

EXIT TERMINAL:
exit


================================================
12. IMPORTANT VIVA QUESTIONS
================================================

Q1. What is a Bloom Filter?

Ans:
A Bloom Filter is a space-efficient probabilistic
data structure used to check whether an element
is possibly present or definitely absent.

Q2. What is a bit array?

Ans:
An array containing only 0s and 1s.

Q3. What is a hash function?

Ans:
A function that converts an input value into an
array index.

Q4. How many hash functions are used here?

Ans:
Two hash functions.

Q5. What is the size of the bit array?

Ans:
10 positions.

Q6. What does 0 represent?

Ans:
The position has not been set by an insertion.

Q7. What does 1 represent?

Ans:
The position has been set during insertion.

Q8. What is a false positive?

Ans:
When the Bloom Filter says an element is possibly
present even though it was never inserted.

Q9. Can a Bloom Filter produce a false negative?

Ans:
Not for an inserted item, provided the bit array
has not been incorrectly modified.

Q10. What does % mean?

Ans:
Modulus operator. It returns the remainder.

Q11. What does // mean?

Ans:
Floor division. It returns the integer quotient.

Q12. Why are two hash functions used?

Ans:
To generate two different positions in the bit array.

Q13. What does Possibly Present mean?

Ans:
Both calculated bit positions contain 1.
The element may or may not actually exist.

Q14. What does Definitely Not Present mean?

Ans:
At least one calculated bit position contains 0.
The element was not inserted into this filter.


================================================
QUICK REVISION
================================================

BIT ARRAY:
bit_array = [0] * 10

HASH FUNCTION 1:
x % 10

HASH FUNCTION 2:
(x // 10) % 10

INSERT:
bit_array[hash1(x)] = 1
bit_array[hash2(x)] = 1

SEARCH:
Check whether both positions are 1.

BOTH POSITIONS 1:
Possibly Present

ANY POSITION 0:
Definitely Not Present

EXIT LOOP:
q

RUN:
python3 bloom.py

IMPORTANT:
A Bloom Filter can give a false positive.
It does not guarantee that a possibly present
element actually exists.

END OF PRACTICAL
""")
