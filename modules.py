import math
from datetime import datetime
import time


def add(x, y):
    """
    :param x: variable
    :param y: variable
    :return: addition
    """
    return x+y


def mul(x, y):
    """
    :param x:  variable
    :param y: variabl
    :return: multiplication
    """
    return x*y

def modulus(x, y):
   """
   :param x: variable
   :param y: variable
   :return: modulus
   """
   return x/y


print("addition with ceil function", math.ceil(add(7.45, 8.01)))
print("addition with floor function", math.floor(add(4.56, 6.67)))
print("multiplication of numbers", math.fabs(mul(4.5, 6.7)))
print("modulus of numbers", math.trunc(modulus(78, 12)))

# converting date string into date:-
date_time_str = '2019-02-22 08:15:27.243860'
date_time_obj = datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S.%f')

print('Date:', date_time_obj.date())
print('Time:', date_time_obj.time())
print('Date-time:', date_time_obj)

# finding the current date time:-
current_date = datetime.now()
print("current date and time", current_date.strftime("%Y-%m-%d %H:%M:%S"))
print("current date and time with single directive", current_date.strftime("%c"))
print("Current date with AM or PM", current_date.strftime("%I:%M:%S %p"))
print("current date with week name and  month name", current_date.strftime("%a, %b %d, %Y"))
print("current date with full week and month name", current_date.strftime("%A, %B %d, %Y"))

# converting the  unix time-stamp into datetime
dateStr = datetime.fromtimestamp(1615419007).strftime("%A, %B %d, %Y %I:%M:%S %p")
print("Datetime stamp", dateStr)

# converting  datetime to to unix time stamp
date_obj = datetime(2015, 10, 10, 10, 10)
print("Unix Timestamp: ", time.mktime(date_obj.timetuple()))




