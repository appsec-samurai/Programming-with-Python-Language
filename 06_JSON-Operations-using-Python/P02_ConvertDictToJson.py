# Author: KEDAR BHARTIYA[appsec-samurai]
# Description: This program illustrate the functionality of
# converting Dictionary to JSON in Python.

import json

# Data to be converted in JSON
emp_dict = {
    "id": "101",
    "name": "Kedar",
    "department": "Engineering"
}

# Serializing json
json_object = json.dumps(emp_dict, indent=4)
print("JSON string after conversion\n", json_object)
