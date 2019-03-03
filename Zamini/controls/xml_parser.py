import xml.etree.ElementTree as ET

def readXml(fileame):
    tree = ET.parse(fileame)
    root = tree.getroot()

    return root
