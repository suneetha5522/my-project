"""
What is exactly r+?
 r+ mode:- Opens a file for both reading and writing
"""

with open('data.txt', 'r+') as my_file:
    my_file.write('Success!\n')
    my_file.write('Bravo!\n')
    print(my_file.read())
