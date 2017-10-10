# exceptions is dict of pairs child:[parents]
exceptions = {}

def add (child, parents):
    if exceptions.get(child) == None:
        exceptions.update({child:[]})
    for parent in parents:
        exceptions[child].append(parent)

def isParent(parent, child):
    parents = exceptions.get(child)
    if parent in parents:
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
previous = []
for i in range(n):
    exception = input()
    if exception in previous:
        print(exception)
    else:
        for parent in previous:
            if isParent(parent, exception):
                print(exception)
                # We need to print exception only one, despite we have more than one answers
                break
        previous.append(exception)
