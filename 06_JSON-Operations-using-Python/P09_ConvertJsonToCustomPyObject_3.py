# Author: KEDAR BHARTIYA[appsec-samurai]
# Description: This program illustrate the functionality of
# converting JSON to a custoum python object using "SimpleNamespace".


# importing the module
import json

try:
    from types import SimpleNamespace as Namespace
except ImportError:
    from argparse import Namespace

# creating the json data
json_data = '{"name" : "Custom_Namespace", "id" : 3, "location" : "Bangalore"}'

# creating the object
py_obj = json.loads(json_data, object_hook=lambda _dict: Namespace(**_dict))

# accessing the JSON data as an object
print("accessing the JSON data as an object")
print(py_obj.name, py_obj.id, py_obj.location)
