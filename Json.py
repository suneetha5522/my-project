"""
JSON is a syntax for exchanging data.
JSON encoding or serialization:-
The process of encoding JSON is usually called serialization. This term refers to the transformation of
data into a series of bytes (hence serial) to be stored or transmitted across a network.
JSON decoding or deserialization:-
deserialization is the reciprocal process of decoding data that has been stored or delivered in the JSON standard
"""
import json

# converting JSON to python with load method:-

x = '{"name": "charan", "languages": ["English", "Telugu"], "age": 23}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print("The JSON dictionary", y)
print("The age of the person", y["age"])


# Converting Python Object into JSON:-
a = {"name": "charan", "age": 30, "city": "hyd"}
b = json.dumps(a)
print("JSON format", b)



"""
Json with class examples
"""

class Json:

    def __init__(self, json_object):
        """
           constructor - initialising the object
        """
        self.json_object = json_object

    def json_loads(self):
        """
          convert string to python object
        :return: data , json data
        """
        json_string = json.loads(self.json_object)
        return json_string

    def json_dump(self):
        """
        convert python object to json
        :return: string, json string
        """

        python_object = json.dumps(self.json_object)
        return python_object


x = Json('{"name":"suneetha", "age":23}')
y = Json({"name": "charan", "age": 45})

a = x.json_loads()
print(f'reads complete value of file {a}')
print(f'reads  single value of file : {a["age"]}')

b = y.json_dump()
print(f'reading  complete value of the file {b}')



















