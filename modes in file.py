"""
problem Statement:- how many modes are there in files with examples:-
What is a file? :- It is used to permanently store data in a non-volatile memory

file operation:-
1. Open a file
2. Read or write (perform operation)
3. Close the file

Types of Operating modes:-

r: Opens a file for reading only
r+: Opens a file for both reading and writing
w: Opens a file for writing only
w+: Open a file for writing and reading.
a: Opens a file for appending
a+: Opens a file for both appending and reading
"""
"""
1.Open a file:- This function returns a file object, also called a handle, as it is used to read or modify the file 
accordingly.
"""
f = open("sample_file.txt", "w+")   # "w+" will create a file if it does not exist in library
z = open("sample_file.txt", "w")    # "w" will not create a file it will only open the file
print("create and open the file", f)
print("Open the file", z)

"""
2. Read or write :- it will perform operations like reading and writing
"""
for each in range(1, 6):
    f.write("This is line %d\r\n" % (each + 1))

f.write("This is 1st file\n")
f.write("This is 2nd file\n")
f.write("This is 3rd file\n")

"""
3. close Operation:- it will closes the file after performing operations
"""
f.close()

"""Reading a file :-  It reads the entire file and returns it contents in the form of a string """

f = open("Sample_file.txt", 'r')
text = f.read(15)
print("The read line is:", text)
f.close()

""" Reading lines ([size]):- It reads the first line of the file i.e till a newline character"""

f = open("Sample_file.txt", 'r')
text = f.readlines(20)
print("The readlines are:", text)
f.close()

"""readlines([sizehint]):- It reads the entire file line by line and updates each line to a list which is returned"""

f = open("Sample_file.txt", 'r')
text = f.readlines()
print("The readlines are:",text)
f.close()

""" Reading and Writing a file :- """
f = open("Sample_file.txt", 'r+')
lines = f.read() 
f.write(lines) 
f.close()

"""Writing and Reading a file"""

f = open("Sample_file.txt", 'w+')
lines = f.read()
f.write(lines)
f.close()

""" tell(): This method gives you the current offset of the file pointer in a file"""

# Telling the file object position
f = open("Sample_file.txt", 'r')
lines = f.read(10)

# tell() 
print("The tell method",f.tell())
f.close()

"""seek(offset, from_where): This method can help you change the position of a file pointer in a file"""

# Setting the file object position
f = open("Sample_file.txt", 'r')
x = f.read(10)
print("setting the file object position", x)

# seek()
print(f.seek(2))
x = f.read(10)
print("The seek method", x)
f.close()

"""flush(): Flush the internal buffer, like stdio‘s fflush(). It has no return value. 
close() automatically flushes the data but if you want to flush the data before 
closing the file then you can use this method """
# Clearing the internal buffer before closing the file
f = open("Sample_file.txt", 'r')
x = f.read(10)

# flush()
f.flush()
print("Flush Method", f.read())
f.close()

"""fileno(): Returns the integer file descriptor that is used by the underlying implementation to 
request I/O operations from the operating system"""
# Getting the integer file descriptor
f = open("Sample_file.txt", 'r')

# fileno()
print("The file number", f.fileno())
f.close()

""" isatty(): Returns True if the file is connected to a device and False if not"""
# Checks if file is connected to a tty(-like) device
f = open("Sample_file.txt", 'r')
print(f.isatty())
f.close()

"""next(): It is used when a file is used as an iterator. The method is 
called repeatedly.  This method returns the next input line or raises StopIteration"""

"""truncate([size]): Truncate the file’s size. If the optional size argument is present, the file is truncated to
(at most) that size. The size defaults to the current position. The current file position is not changed. Note 
that if a specified size exceeds the file’s current size, the result is platform-dependent: possibilities 
include that the file may remain unchanged, increase to the specified size as if zero-filled,
or increase to the specified size with undefined new content."""

