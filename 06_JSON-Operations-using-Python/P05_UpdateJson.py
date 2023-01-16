# Author: KEDAR BHARTIYA[appsec-samurai]
# Description: This program illustrate the functionality of
# updating a JSON object.

import json

# JSON data
json_data = '{ "organization":"GeeksForGeeks","city": "Noida", "country": "India"}'

# python object to be appended
append_value = {"pin": 110096}

# parsing JSON string:
json_string = json.loads(json_data)

# appending the data
json_string.update(append_value)

# the result is a JSON string:
print("Json after appending the new value")
print(json.dumps(json_string))
