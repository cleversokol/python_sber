import json
import operator

def children(parent):
    childs = classes.get(parent)
    #print("children func")
    #print("classes = ", classes)
    #print("parent = ", parent)
    #print("childs = ", childs)
    #print("value = ", value)
    if childs:
        for child in childs:
            value.append(child)
            children(child)
        #print("were childs")

classes = {}
answer = {}
j = json.loads(input())
for i in j:
    child = i["name"]
    parents = i["parents"]

    #print("child = ", child)
    #print("parents = ", parents)
    if classes.get(child) == None:
        classes.update({child:[]})
    for parent in parents:
        #print(parent)
        if classes.get(parent) == None:
            classes.update({parent:[]})
        classes[parent].append(child)

#print("befoe classes = ", classes)
for parent in classes:
    #print("FOR parent = ", parent)
    value = []
    #print("1")
    children(parent)
    #print("2")
    answer.update({parent:value})
#print("answer = ", answer)
for key in answer:
    #print(answer.get(key))
    #print(len(set(answer.get(key))))
    value = len(set(answer.get(key)))
    answer.update({key:value})
sorted_classes = sorted(answer.items(), key=operator.itemgetter(0))
for i in sorted_classes:
    print(i[0], ":", i[1]+1)
#print("answer = ", answer)
