import xml.etree.ElementTree as ET

grocerylist = ["milk:2:cups", "flour:4:cups"]

grocerylistxml = ET.Element('grocerylist')
for i in range(len(grocerylist)):
    ok = ET.SubElement(grocerylistxml, "ingredient")
    ok.text = str(grocerylist[i])


mygrocerylist = ET.tostring(grocerylistxml)
myfile = open("grocerylist.xml", "w")
myfile.write(str(mygrocerylist))