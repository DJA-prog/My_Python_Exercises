from xml.etree import ElementTree as ET

# Assume that we have an existing XML document with one "data" child
doc = ET.parse("history1.xml")
root = doc.getroot()

# Create 2 new "data" elements
data1 = ET.Element("calculation", {"id": "3", "date": "27-06-2021", "time": "17-14-141", "equation": "2+3", "answer": "5"})

# Append the new "data" elements to the root element of the XML document
root.append(data1)

doc.write('history1.xml')