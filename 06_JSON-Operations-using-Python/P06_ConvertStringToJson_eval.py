# Author: KEDAR BHARTIYA[appsec-samurai]
# Description: This program illustrate the functionality of
# converting string to JSON using eval function.


# Initializing json object string
ini_string = """{'kedar': 1, 'sayali' : 5, 'amar' : 10, 'aditya' : 15}"""

# printing initial string
print("initial dictionary as a string", ini_string)
print("type of ini_string object", type(ini_string))

# converting string to json
json_data = eval(ini_string)

# printing final result
print("final dictionary after conversion", str(json_data))
print("type of final_dictionary", type(json_data))
