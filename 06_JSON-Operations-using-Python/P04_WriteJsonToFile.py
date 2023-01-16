# Author: KEDAR BHARTIYA[appsec-samurai]
# Description: This program illustrate the functionality of
# writing a JSON objects to a file.

import json

import json

emp_dict = {
    "name": "Kedar",
    "languages": ["Python", "GoLang", "Shell"],
    "married": True,
    "age": 30
}

with open('emp_details.txt', 'w') as json_file:
    print("Writing data into file..!")
    json.dump(emp_dict, json_file)
    print("Writing data into file successfully..!")
