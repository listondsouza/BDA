print("""
PYTHON PRACTICAL – BLOOM FILTER (STUDENT ID REGISTRATION CHECKER)
=================================================================

1. CHECK REQUIREMENTS (Ubuntu Terminal)
----------------------------------------
python3 --version
pip3 --version
python3 -c "import hashlib; print('Available')"

hashlib is built into Python. No separate installation is required.

2. CREATE AND OPEN THE PYTHON FILE
----------------------------------
mkdir -p ~/bloom
cd ~/bloom
nano bloom.py

3. TYPE THIS PROGRAM INTO bloom.py
----------------------------------
import hashlib

class BloomFilter:
    def __init__(self, size):
        self.size = size
        self.bit_array = [0] * size

    def get_hashes(self, item):
        hashes = []
        for i in range(3):
            value = item + str(i)
            hash_value = int(hashlib.md5(value.encode()).hexdigest(), 16)
            index = hash_value % self.size
            hashes.append(index)
        return hashes

    def insert(self, student_id):
        positions = self.get_hashes(student_id)
        for index in positions:
            self.bit_array[index] = 1
        print("Student ID inserted successfully")

    def search(self, student_id):
        positions = self.get_hashes(student_id)
        for index in positions:
            if self.bit_array[index] == 0:
                return "Definitely Not Registered"
        return "Possibly Registered"

# Main program
bf = BloomFilter(100)

bf.insert("2023120045")
bf.insert("2023120032")
bf.insert("2023120047")

print(bf.search("2023120045"))
print(bf.search("2023120099"))

print("Bit Array:")
print(bf.bit_array)

4. SAVE AND RUN
---------------
In nano:
Ctrl + O, Enter, Ctrl + X

Run:
python3 bloom.py

5. EXPECTED OUTPUT (wording/order)
----------------------------------
Student ID inserted successfully
Student ID inserted successfully
Student ID inserted successfully
Possibly Registered
Definitely Not Registered
Bit Array: [ ... ]

The exact bit array positions depend on the hash values.

6. HOW THE CHECK WORKS
----------------------
- The bit array initially contains 0s.
- Hash functions generate bit positions for an ID.
- Insert changes those positions to 1.
- Search checks the same positions.
- If any checked bit is 0: definitely absent.
- If all checked bits are 1: possibly present.

A Bloom Filter can produce a false positive, but normally does not produce a false negative for an inserted item.
""")
