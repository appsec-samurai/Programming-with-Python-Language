# Author: KEDAR BHARTIYA[appsec-samurai]
# Description: This program illustrate the functionality of
# reading a file which contains a JSON object.

import json

# Opening JSON file
json_file = open('emp_details.json', )

# returns JSON object as a dictionary
emp_data_dict = json.load(json_file)

# Iterating through the json list
print("Details of employees is as follows:")
for emp in emp_data_dict['emp_details']:
    print(emp)

# Closing file
json_file.close()
