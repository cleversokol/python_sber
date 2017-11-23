from xml.etree import ElementTree

tree = ElementTree.parse("example.xml")
root = tree.getroot()

print(root)
print(root.tag, root.attrib)
print(root[0][0].text)

for element in root.iter("scores"):
    print(element)
    score_sum = 0
    for child in element:
        score_sum += float(child.text)
    print(score_sum)

tree.write("example_copy.xml")

greg = root[0]
