# classes is dict of pairs parent:child
classes = []

def add (child, *parents):
    for parent in parents:
        classes.append()

def isParent(parent, child):
    if parent == child:
        print("Yes")
    elif parent,child in classes:
        print("Yes")
    else:
        print("No")

    list = variables.get(namespace)
    if var in list:
        return namespace
    elif namespace == "global":
        return "None"
    else:
        namespace = namespaces.get(namespace)
        return get(namespace, var)

# First input value is number of pending commands
n = int(input())
for i in range(n):
    # var can be either parent namespace or variable name
    child, *parents = input().split()
    add(child, *parents)

# Number of pending commands
n = int(input())
for i in range(n):
    parent, child = input().split()
    isParent(parent, child)
