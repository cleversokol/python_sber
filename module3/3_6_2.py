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
module1 = next(greg.iter("module1"))
print(module1, module1.text)
module1.text = str(float(module1.text)+30)

certificate = greg[2]
certificate.set("type", "with distinction")

description = ElementTree.Element("description")
description.text = "Showed excellent skills during the course"
greg.append(description)

tree.write("example_modified2.xml")

description = greg.find("description")
greg.remove(description)