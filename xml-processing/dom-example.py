import xml.etree.ElementTree as ET
from xml.dom import minidom
import os


cwd = os.getcwd()[0:-14]
docs = ET.parse(cwd + "CysticFibrosis2/data/cf79.xml")
docs = docs.getroot()

def prettify(elem):
    rough_string = ET.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

autores = ET.Element('autores')

for child in docs:
    for autor in child.iter('AUTHOR'):
        #print(autor.text)
        autorR = ET.SubElement(autores, "autor")
        autorR.text = autor.text
    #ET.dump(autores)

#print(prettify(autores))

save_path_file = "autores.xml"

with open(save_path_file, "w") as f:
    f.write(prettify(autores))