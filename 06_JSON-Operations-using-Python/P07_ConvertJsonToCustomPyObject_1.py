# Author: KEDAR BHARTIYA[appsec-samurai]
# Description: This program illustrate the functionality of
# converting JSON to a custoum python object.


# importing the module
import json
from collections import namedtuple

# creating the data
json_data = '{"name" : "Custom_Py_Object", "id" : 1, "location" : "Pune"}'

# making the object
py_obj = json.loads(json_data, object_hook=lambda _dict: namedtuple('X', _dict.keys())(*_dict.values()))

# accessing the JSON data as an object
print("accessing the data as an object")
print(py_obj.name, py_obj.id, py_obj.location)
