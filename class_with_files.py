"""
Create a class for read a file,write and append
"""
class My_file:

    def write_data(self):
        """
        open the file and write the data
        :return: boolean True
        """
        f = open("data.txt","w+")
        for each in range(0, 6):
           f.write("This is line %d\r\n" % each)
        f.close()
        return True
    def read_data(self):
        """
        "Reading the opened file"
        :return: boolean, True
        """
        f = open("data.txt", "r")
        text = f.read(5)
        print("Reading data", text)
        f.close()
        return True

    def append_data(self):
        """
        appending the date to file
        :return:
        """
        f = open("data.txt", "a+")
        for each in range(6, 11):
           f.write("appended line %d\r\n" % each)
        f.close()
        return True


x = My_file()
y = x.write_data()
z = x.read_data()
a = x.append_data()



