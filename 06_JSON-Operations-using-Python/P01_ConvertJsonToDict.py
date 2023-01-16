# Author: KEDAR BHARTIYA[appsec-samurai]
# Description: This program illustrate the functionality of
# converting JSON to Dictionary in Python.

import json

# JSON string
emp_details = '{"id":"101", "name": "Kedar", "department":"Engineering"}'

# Convert string to Python dict
emp_details__dict = json.loads(emp_details)
print("JSON string after converting to Python dictionary\n", emp_details__dict)

print("Name of Employee in dictionary\n", emp_details__dict['name'])

