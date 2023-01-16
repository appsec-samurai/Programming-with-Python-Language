# Author: KEDAR BHARTIYA[appsec-samurai]
# Description: This program illustrate the functionality of
# converting JSON to a custoum python object using "object_hook".

# importing the module
import json
from collections import namedtuple


# Create custom_decoder function
def custom_decoder(data_dict):
    return namedtuple('X', data_dict.keys())(*data_dict.values())


# creating the json data
json_data = '{"name" : "Custom_Decoder", "id" : 2, "location" : "Mumbai"}'

# creating the object
py_obj = json.loads(json_data, object_hook=custom_decoder)

# accessing the JSON data as an object
print("accessing the JSON data as an object")
print(py_obj.name, py_obj.id, py_obj.location)
