"""
Extract the whatsup data by using regular expressions
"""

import re
import os


class Watsup_data:
    def __init__(self):
        """
        initializing the constructor
        """
        self.data = []
    def read_watsup_data(self):
        """
        :return: list of dictionaries
        """
        watsup_file = "F:/My project/watsup_file.txt"

        # Read WhatsApp file
        if os.path.exists(watsup_file):
            file_data = open(watsup_file, 'r', encoding="utf8")
            f = file_data.read()
        # Get date
        date_regex = re.compile(r'(\d+/\d+/\d+)')
        date = date_regex.findall(f)
        # print(date)

        # Get time
        time_regex = re.compile(r'(24:00|2[0-3]:[0-5][0-9]|[0-1][0-9]:[0-5][0-9])')
        time = time_regex.findall(f)
        # print(time)

        # Get Users
        user_regex = re.compile(r'[9786]\d{9}')
        user = user_regex.findall(f)
        # print(user)

        # Get Message
        message_regex = re.compile(r"[a-z].*")
        message = message_regex.findall(f)
        # print(message)

        # appending details to dictionary

        for w, x, y, z in zip(date, time, user, message):
            self.data.append({"date": str(w), "time": str(x), "user":str(y), "message": str(z)})
        return self.data


x = Watsup_data()
y = x.read_watsup_data()
print("The watsup data:", x.data)
print("The first user", x.data[0])
print("The 2nd user", x.data[1])
print("The 10th user", x.data[5])





