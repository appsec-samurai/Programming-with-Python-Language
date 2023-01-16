# Author: KEDAR BHARTIYA[appsec-samurai]
# Description: This program illustrate the functionality of
# converting JSON to XML file format.

import json as JS
import xml.etree.ElementTree as ET

# Opening JSON file in read mode
with open("quiz_details.json", "r") as json_file:
    # loading json file data to variable json_data
    json_data = JS.load(json_file)

    # Building the root element of the xml file
    root = ET.Element("quiz")

    # Building the sub root elements
    sub_root = ET.SubElement(root, "sport")

    # Building sub element of sub root
    Q1 = ET.SubElement(sub_root, "q1")
    ET.SubElement(Q1, "question")
    quest_text = json_data["quiz"]["sport"]["q1"]["question"]

    # Building multiple sub elements with name "options" to hold different values
    # Xml elements cannot hold integer values so we need to convert them to string
