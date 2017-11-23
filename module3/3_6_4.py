from xml.etree import ElementTree

#tree = ElementTree.parse("example.xml")
#string = "<cube color=\"blue\"><cube color=\"red\"><cube color=\"green\"></cube></cube><cube color=\"red\"></cube></cube>"

def walkTree(root, depth):
    global red
    global green
    global blue
    depth += 1
    color = root.attrib.get("color")
    #print("root.attrib = ", root.attrib)
    if color == "red":
        red += depth
    elif color == "green":
        green += depth
    elif color == "blue":
        blue += depth
    #print("depth = ", depth)
    #print(red, green, blue)
    for child in root:
        #print("child.attrib = ", child.attrib)
        #global red
        #global green
        #global blue
        #color = child.attrib.get("color")
        #if color == "red":
        #    red += depth
        #elif color == "green":
        #    green += depth
        #elif color == "blue":
        #    blue += depth
        #print("depth = ", depth)
        #print(red, green, blue)
        walkTree(child, depth)

root = ElementTree.fromstring(input())
#root = ElementTree.fromstring(string)
tree = ElementTree.ElementTree(root)

depth = 0
red = 0
green = 0
blue = 0

walkTree(root, depth)
#print("depth = ", depth)
print(red, green, blue)
