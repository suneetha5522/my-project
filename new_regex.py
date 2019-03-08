import re
import os


watsup_file = "F:/My project/watsup_file.txt"

# Read WhatsApp file
if os.path.exists(watsup_file):
    file_data = open(watsup_file, 'r', encoding="utf8")
    f = file_data.read()
# Get date
date_regex = re.compile(r'(\d+/\d+/\d+)')
date = date_regex.findall(f)
#print(date)

# Get time
time_regex=re.compile(r'(24:00|2[0-3]:[0-5][0-9]|[0-1][0-9]:[0-5][0-9])')
time = time_regex.findall(f)
#print(time)

# Get Users
user_regex = re.compile(r'[9786]\d{9}')
user = user_regex.findall(f)
#print(user)

# Get Message
message_regex = re.compile(r"[a-z].*")
message = message_regex.findall(f)
#print(message)

#appending data to
data = []
for w, x, y, z in zip(date, time, user, message):
    data.append([str(w), str(x), str(y), str(z)])
print("The total whatsup data:", data)


print("Date of 1st watsup chat", data[0][0])
print("time of the chat", data[0][1])
print("phone number of the chat", data[0][2])
print("sender message:", data[0][3])







