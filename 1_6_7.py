# classes is dict of pairs child:[parents]
classes = {}

def add (child, parents):
    if classes.get(child) == None:
        classes.update({child:[]})
    for parent in parents:
        classes[child].append(parent)

def isParent(parent, child):
    parents = classes.get(child)
    if parent in parents or parent == child:
        return True
    elif parents == None:
        return False
    else:
        answer = False
        for i in parents:
            answer = answer or isParent(parent, i)
        return answer

# First input value is number of pending commands
n = int(input())
for i in range(n):
    # var can be either parent namespace or variable name
    child, *parents = input().split()
    if len(parents) > 0:
        parents.remove(":")
    add(child, parents)

# Number of pending commands
n = int(input())
for i in range(n):
    parent, child = input().split()
    if isParent(parent, child):
        print("Yes")
    else:
        print("No")
