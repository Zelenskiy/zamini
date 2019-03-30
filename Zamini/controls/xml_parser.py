import xml.etree.ElementTree as ET

def readXml(filename):
    #        open in binary mode ↓
    # with open(filename, 'rb') as f:
    #     e = ET.fromstring(f.read())
    #     tree = ET.parse(e)
    #     root = tree.getroot()
    #     return root
    tree = ET.parse(filename)
    root = tree.getroot()

    return root
